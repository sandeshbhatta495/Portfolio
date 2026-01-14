"""
Flask Portfolio Application - Production-Ready Configuration

This app properly handles:
- Static files (CSS, JS, images) served from /static
- Templates (HTML) rendered from /templates
- API endpoints for backend functionality
- Environment-based configuration
- Proper error logging
"""

from flask import Flask, request, jsonify, send_file, render_template, url_for
from flask_cors import CORS
from flask_mail import Mail, Message
import os
import json
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from backend.database import Database

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# CONFIGURATION - EXPLICIT AND CLEAR
# ============================================================================

# Get absolute paths - CRITICAL for both local and production environments
BASE_DIR = Path(__file__).parent.absolute()
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'

# Create Flask app with EXPLICIT paths - no guessing
app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),  # Convert Path to string for Flask
    static_folder=str(STATIC_DIR),       # Flask needs string paths
    static_url_path='/static'            # URL prefix for static files
)

# ============================================================================
# SECURITY & CONFIGURATION
# ============================================================================

# Secret key - get from environment, fallback only for local development
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'dev-secret-key-change-in-production-DO-NOT-USE-IN-PROD'
)
app.config['SECRET_KEY'] = SECRET_KEY

# ============================================================================
# EMAIL CONFIGURATION - From Environment Variables
# ============================================================================

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', True)
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Get recipient email from environment - NOT hardcoded
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'default@example.com')

# ============================================================================
# LOGGING - For Production Error Visibility
# ============================================================================

# Create logger for application debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# INITIALIZE SERVICES
# ============================================================================

# Email service
mail = Mail(app)

# Database
try:
    db = Database()
    logger.info("Database initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize database: {e}", exc_info=True)
    db = None

# Enable CORS for API endpoints
CORS(app, resources={r"/api/*": {"origins": "*"}})



# ============================================================================
# ROUTES - TEMPLATING
# ============================================================================

@app.route('/')
def home():
    """
    Serve the main portfolio page
    
    Flask renders: templates/index.html (Jinja2 template)
    HTML in template uses: {{ url_for('static', filename='...') }}
    This generates correct /static/... URLs
    """
    try:
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering template: {e}", exc_info=True)
        return jsonify({'error': 'Failed to load portfolio'}), 500


# ============================================================================
# ROUTES - API ENDPOINTS
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment verification"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/contact', methods=['POST'])
def contact():
    """
    Handle contact form submissions
    
    Expected JSON:
    {
        "name": "John Doe",
        "email": "john@example.com",
        "subject": "Hello",
        "message": "Your message here"
    }
    """
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f'Missing required field: {field}'}), 400

        name = data['name'].strip()
        email = data['email'].strip()
        subject = data['subject'].strip()
        message = data['message'].strip()

        # Save to database
        if db:
            contact_id = db.save_contact(name, email, subject, message)
            logger.info(f"Contact saved: ID={contact_id}, Email={email}")
        else:
            logger.warning("Database not available, contact not saved")

        # Send email notification
        try:
            if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
                msg = Message(
                    subject=f'Portfolio Contact: {subject}',
                    recipients=[RECIPIENT_EMAIL],
                    body=f"""
New contact form submission:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
Sent from Portfolio Website
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    """
                )
                mail.send(msg)
                logger.info(f"Email sent for contact from {email}")
            else:
                logger.warning("Email not configured, skipping email send")
        except Exception as email_error:
            logger.error(f"Email sending failed: {email_error}", exc_info=True)
            # Continue even if email fails - contact is still saved in DB

        return jsonify({
            'success': True,
            'message': 'Message sent successfully!'
        }), 200

    except Exception as e:
        logger.error(f"Error in contact endpoint: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/download-resume', methods=['GET'])
def download_resume():
    """
    Handle resume download requests
    
    Tracks downloads in database and serves PDF
    """
    try:
        # Use Path for better path handling
        resume_path = STATIC_DIR / 'assets' / 'Sandesh_Bhatta_Resume.pdf'

        # Check if resume exists
        if not resume_path.exists():
            logger.error(f"Resume not found: {resume_path}")
            return jsonify({'error': 'Resume file not found'}), 404

        # Track download
        if db:
            try:
                client_ip = request.remote_addr
                user_agent = request.headers.get('User-Agent', 'Unknown')
                db.track_resume_download(client_ip, user_agent)
                logger.info(f"Resume downloaded from IP: {client_ip}")
            except Exception as track_error:
                logger.warning(f"Failed to track download: {track_error}")
                # Continue even if tracking fails

        # Serve the file
        return send_file(
            str(resume_path),
            as_attachment=True,
            download_name='Sandesh_Bhatta_Resume.pdf',
            mimetype='application/pdf'
        )

    except Exception as e:
        logger.error(f"Error in download-resume endpoint: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get portfolio statistics"""
    try:
        if not db:
            return jsonify({'error': 'Database not available'}), 503

        stats = db.get_stats()
        return jsonify(stats), 200

    except Exception as e:
        logger.error(f"Error in stats endpoint: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    Get all projects from static/assets/projects directory
    
    Merges directory listing with metadata from projects.json
    Returns JSON array of project objects
    """
    try:
        # Build paths to projects directory and metadata file
        projects_dir = BASE_DIR / 'static' / 'assets' / 'projects'
        projects_json_path = BASE_DIR / 'backend' / 'projects.json'

        # Check if projects directory exists
        if not projects_dir.exists():
            logger.warning(f"Projects directory not found: {projects_dir}")
            return jsonify([]), 200  # Return empty array, not error

        # Load metadata from projects.json if it exists
        project_metadata = {}
        if projects_json_path.exists():
            try:
                with open(projects_json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for proj in data.get('projects', []):
                        project_metadata[proj['filename']] = proj
                logger.info(f"Loaded metadata for {len(project_metadata)} projects")
            except Exception as json_error:
                logger.error(f"Error loading projects.json: {json_error}")
                # Continue without metadata

        projects = []
        supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

        # Scan directory for project files/directories
        for item in projects_dir.iterdir():
            filename = item.name

            # Handle directories
            if item.is_dir():
                if filename in project_metadata:
                    metadata = project_metadata[filename]
                    project = {
                        'title': metadata.get('title', filename.replace('-', ' ').replace('_', ' ').title()),
                        'image': f'/static/assets/projects/{filename}',
                        'description': metadata.get('description', f'Project: {filename}'),
                        'tags': metadata.get('tags', []),
                        'category': metadata.get('category', 'all'),
                        'github': metadata.get('github', 'https://github.com')
                    }
                    projects.append(project)
                continue

            # Handle image files
            _, ext = item.suffix, item.suffix
            if ext.lower() not in supported_extensions:
                continue

            # Build the image path for frontend
            image_path = f'/static/assets/projects/{filename}'

            # Use metadata if available, otherwise create basic entry
            if filename in project_metadata:
                metadata = project_metadata[filename]
                project = {
                    'title': metadata.get('title', item.stem.replace('-', ' ').replace('_', ' ').title()),
                    'image': image_path,
                    'description': metadata.get('description', ''),
                    'tags': metadata.get('tags', []),
                    'category': metadata.get('category', 'all'),
                    'github': metadata.get('github', 'https://github.com')
                }
            else:
                project = {
                    'title': item.stem.replace('-', ' ').replace('_', ' ').title(),
                    'image': image_path,
                    'description': '',
                    'tags': [],
                    'category': 'all',
                    'github': 'https://github.com'
                }

            projects.append(project)

        # Sort by title for consistent ordering
        projects.sort(key=lambda x: x['title'])

        logger.info(f"Returning {len(projects)} projects")
        return jsonify(projects), 200

    except Exception as e:
        logger.error(f"Error in projects endpoint: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500



# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}", exc_info=True)
    return jsonify({'error': 'Internal server error'}), 500


# ============================================================================
# APPLICATION STARTUP
# ============================================================================

if __name__ == '__main__':
    logger.info("=" * 80)
    logger.info("Starting Flask Portfolio Application")
    logger.info("=" * 80)
    logger.info(f"Template directory: {TEMPLATE_DIR}")
    logger.info(f"Static directory: {STATIC_DIR}")
    logger.info(f"Base URL: http://localhost:5000")
    logger.info(f"Debug mode: {app.debug}")
    logger.info("=" * 80)

    # Run Flask development server
    # For production, use: gunicorn app:app
    app.run(
        debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true',
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000))
    )