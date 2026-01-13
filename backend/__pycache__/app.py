from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_mail import Mail, Message
import os
from datetime import datetime
from database import Database

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bhattasandesh148@gmail.com'  # Change this
app.config['MAIL_PASSWORD'] = '@SANDESH BHATTA1'  # Change this
app.config['MAIL_DEFAULT_SENDER'] = 'bhattasandesh148@gmail.com'  # Change this

mail = Mail(app)
db = Database()

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
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
        db.save_contact(name, email, subject, message)
        
        # Send email notification
        try:
            msg = Message(
                subject=f'Portfolio Contact: {subject}',
                recipients=['bhattasandesh148@gmail.com'],  # Your email
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
        except Exception as e:
            print(f"Email sending failed: {e}")
            # Continue even if email fails
        
        return jsonify({
            'success': True,
            'message': 'Message sent successfully!'
        }), 200
        
    except Exception as e:
        print(f"Error in contact endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/download-resume', methods=['GET'])
def download_resume():
    """Handle resume download requests"""
    try:
        resume_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'Sandesh_Bhatta_Resume.pdf')
        
        if not os.path.exists(resume_path):
            return jsonify({'error': 'Resume file not found'}), 404
        
        # Track download
        db.track_resume_download()
        
        return send_file(
            resume_path,
            as_attachment=True,
            download_name='Sandesh_Bhatta_Resume.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"Error in download-resume endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get portfolio statistics"""
    try:
        stats = db.get_stats()
        return jsonify(stats), 200
    except Exception as e:
        print(f"Error in stats endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all projects by scanning the assets/projects directory and merging with metadata"""
    try:
        import json
        
        projects_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'projects')
        projects_json_path = os.path.join(os.path.dirname(__file__), 'projects.json')
        
        if not os.path.exists(projects_dir):
            return jsonify({'error': 'Projects directory not found'}), 404
        
        # Load project metadata from JSON
        project_metadata = {}
        if os.path.exists(projects_json_path):
            try:
                with open(projects_json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Create a dictionary mapping filename to metadata
                    for proj in data.get('projects', []):
                        project_metadata[proj['filename']] = proj
            except Exception as e:
                print(f"Error loading projects.json: {e}")
        
        projects = []
        supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
        
        # Scan directory for image files
        for filename in os.listdir(projects_dir):
            file_path = os.path.join(projects_dir, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                # Check if it's a directory without extension (like 'n8n automation' or 'suduko solver')
                # Try to find an image inside or use the directory name
                if filename in project_metadata:
                    # Use metadata for this directory
                    metadata = project_metadata[filename]
                    project = {
                        'title': metadata.get('title', filename.replace('-', ' ').replace('_', ' ').title()),
                        'image': f'assets/projects/{filename}',  # Will need to handle this
                        'description': metadata.get('description', f'Project: {filename}'),
                        'tags': metadata.get('tags', []),
                        'category': metadata.get('category', 'all'),
                        'github': metadata.get('github', 'https://github.com/sandeshbhatta495')
                    }
                    projects.append(project)
                continue
            
            # Get file extension
            _, ext = os.path.splitext(filename)
            if ext.lower() not in supported_extensions:
                continue
            
            # Build relative path for frontend
            image_path = f'assets/projects/{filename}'
            
            # Check if we have metadata for this file
            if filename in project_metadata:
                metadata = project_metadata[filename]
                project = {
                    'title': metadata.get('title', os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()),
                    'image': image_path,
                    'description': metadata.get('description', f'Project: {metadata.get("title", filename)}'),
                    'tags': metadata.get('tags', []),
                    'category': metadata.get('category', 'all'),
                    'github': metadata.get('github', 'https://github.com/sandeshbhatta495')
                }
            else:
                # Fallback to basic info if no metadata found
                title = os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()
                project = {
                    'title': title,
                    'image': image_path,
                    'description': f'Project: {title}',
                    'tags': [],
                    'category': 'all',
                    'github': 'https://github.com/sandeshbhatta495'
                }
            
            projects.append(project)
        
        # Sort projects by title
        projects.sort(key=lambda x: x['title'])
        
        return jsonify(projects), 200
        
    except Exception as e:
        print(f"Error in projects endpoint: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    print("Starting Flask server...")
    print("Server running at http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=True, host='0.0.0.0', port=5000)
