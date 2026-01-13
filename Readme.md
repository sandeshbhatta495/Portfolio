# Sandesh Bhatta - Portfolio Website

A modern, professional portfolio website showcasing my projects, skills, and experience as an Electronics, Communication & IT Engineering student.

## ✨ Features

### Modern Design
- 🎨 **Glassmorphism UI** - Beautiful glass-morphic design elements
- 🌓 **Dark/Light Theme** - Toggle between themes with persistent preference
- 📱 **Fully Responsive** - Optimized for all devices (mobile, tablet, desktop)
- ✨ **Smooth Animations** - Scroll reveal, typing effects, and particle background
- 🎯 **Interactive Elements** - Hover effects, transitions, and micro-animations

### Sections
- 🏠 **Hero** - Eye-catching introduction with typing animation
- 👤 **About** - Personal background and what drives me
- 💼 **Experience** - Timeline of education and achievements
- 🛠️ **Skills** - Categorized skills with progress bars and filters
- 🚀 **Projects** - Filterable project showcase with GitHub links
- 🎓 **Certifications** - Carousel of licenses and certifications
- 📧 **Contact** - Working contact form with backend integration

### Backend Features
- 🐍 **Python Flask API** - RESTful backend server
- 📧 **Email Notifications** - Automatic email alerts for contact form submissions
- 💾 **SQLite Database** - Store contacts and track resume downloads
- 📄 **Resume Download** - Download resume with analytics tracking
- 📊 **Statistics** - Track portfolio engagement

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or download the repository**
   ```bash
   cd portfolio
   ```

2. **Install Python dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure email settings** (Optional but recommended)
   
   Edit `backend/app.py` and update the email configuration:
   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'
   app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
   ```

   For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an app password: https://myaccount.google.com/apppasswords

4. **Add your resume** (Optional)
   
   Place your resume PDF in the `assets` folder:
   ```
   portfolio/assets/Sandesh_Bhatta_Resume.pdf
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   python app.py
   ```
   The server will start at `http://localhost:5000`

2. **Open the frontend**
   
   Simply open `index.html` in your web browser, or use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server -p 8000
   ```
   Then visit `http://localhost:8000`

## 📁 Project Structure

```
portfolio/
├── index.html              # Main HTML file
├── css/
│   └── style.css          # Styles with glassmorphism and themes
├── js/
│   └── script.js          # Interactive features and animations
├── assets/
│   ├── profile.jpg        # Profile picture
│   ├── Sandesh_Bhatta_Resume.pdf  # Resume file
│   └── projects/          # Project screenshots
├── backend/
│   ├── app.py            # Flask application
│   ├── database.py       # Database operations
│   ├── config.py         # Configuration
│   ├── requirements.txt  # Python dependencies
│   └── portfolio.db      # SQLite database (auto-created)
└── README.md             # This file
```

## 🎨 Customization

### Colors & Theme
Edit CSS variables in `css/style.css`:
```css
:root {
    --primary-color: #6366f1;
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* ... more variables */
}
```

### Content
- Update personal information in `index.html`
- Modify projects, skills, and certifications
- Replace profile picture in `assets/profile.jpg`

### Backend
- Configure email settings in `backend/app.py`
- Adjust database schema in `backend/database.py`
- Set environment variables for production

## 🌐 Deployment

### Frontend
Deploy to any static hosting service:
- **GitHub Pages** - Free hosting for static sites
- **Netlify** - Automatic deployments from Git
- **Vercel** - Fast and easy deployment
- **Cloudflare Pages** - Global CDN

### Backend
Deploy the Flask backend to:
- **Heroku** - Easy Python app deployment
- **PythonAnywhere** - Python-specific hosting
- **DigitalOcean** - VPS with full control
- **AWS/Google Cloud** - Scalable cloud platforms

**Important:** Update CORS settings in `backend/app.py` for production:
```python
CORS(app, origins=['https://your-domain.com'])
```

## 📧 Email Configuration

For the contact form to work, you need to configure email settings:

### Gmail Setup
1. Enable 2-factor authentication on your Google account
2. Generate an app password: https://myaccount.google.com/apppasswords
3. Update `backend/app.py` with your credentials

### Alternative Email Providers
- **SendGrid** - Free tier available
- **Mailgun** - Good for developers
- **AWS SES** - Scalable email service

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **JavaScript (ES6+)** - Interactive features
- **Font Awesome** - Icons
- **Google Fonts** - Typography (Inter, Outfit)

### Backend
- **Python 3** - Programming language
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Flask-Mail** - Email integration
- **SQLite** - Database

## 📊 Features Breakdown

### Particle Background
Animated particle system with connecting lines that adapts to theme

### Typing Animation
Dynamic typing effect in hero section cycling through multiple phrases

### Scroll Reveal
Elements fade in and slide up as you scroll down the page

### Skills Filter
Interactive filtering system for different skill categories

### Projects Filter
Filter projects by category (All, Python, Hardware, Web)

### Certifications Carousel
Responsive carousel showing certifications with navigation controls

### Contact Form
Full-featured contact form with:
- Client-side validation
- Backend API integration
- Email notifications
- Database storage
- Success/error feedback

### Resume Download
Track resume downloads with analytics

## 🔒 Security Notes

- Never commit sensitive credentials to version control
- Use environment variables for production secrets
- Implement rate limiting for API endpoints
- Validate and sanitize all user inputs
- Use HTTPS in production
- Keep dependencies updated

## 📝 License

This project is open source and available for personal and commercial use.

## 👤 Contact

**Sandesh Bhatta**
- Email: bhattasandesh148@gmail.com
- LinkedIn: [linkedin.com/in/sandesh-bhatta](https://linkedin.com/in/sandesh-bhatta)
- GitHub: [github.com/sandeshbhatta](https://github.com/sandeshbhatta)

## 🙏 Acknowledgments

- Design inspiration from modern portfolio trends
- Icons from Font Awesome
- Fonts from Google Fonts
- Color gradients from UI Gradients

---

**Built with ❤️ using HTML, CSS, JavaScript & Python**
