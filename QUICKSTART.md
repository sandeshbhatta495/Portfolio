# Quick Start Guide

## 🚀 Get Your Portfolio Running in 3 Steps

### Step 1: Install Python Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start the Backend Server
```bash
python app.py
```
You should see: `Server running at http://localhost:5000`

### Step 3: Open the Website
Simply double-click `index.html` or open it in your browser.

---

## 📧 Email Configuration (Optional)

To enable contact form emails:

1. **For Gmail users:**
   - Go to https://myaccount.google.com/apppasswords
   - Generate an app password
   - Edit `backend/app.py` lines 12-14:
   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-16-char-app-password'
   app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
   ```

2. **Test the contact form** by submitting a message

---

## 📄 Add Your Resume

1. Save your resume as PDF
2. Copy it to: `portfolio/assets/Sandesh_Bhatta_Resume.pdf`
3. The download button will automatically work!

---

## 🎨 Customize Your Portfolio

### Update Your Information
Edit `index.html` and search for:
- Your name: "Sandesh Bhatta"
- Your email: "bhattasandesh148@gmail.com"
- Your LinkedIn/GitHub URLs

### Change Colors
Edit `css/style.css` (lines 2-10) to change the color scheme:
```css
:root {
    --primary-color: #6366f1;  /* Change this! */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Add Your Photo
Replace `assets/profile.jpg` with your own photo

---

## 🌐 Deploy Your Portfolio

### Free Hosting Options:

**GitHub Pages (Recommended for Frontend)**
1. Create a GitHub repository
2. Push your code
3. Go to Settings → Pages
4. Select main branch
5. Your site will be live at `username.github.io/repo-name`

**Backend Hosting:**
- **PythonAnywhere** (Free tier available)
- **Heroku** (Easy deployment)
- **Render** (Modern platform)

---

## ✅ Checklist

- [ ] Backend server running
- [ ] Website opens in browser
- [ ] Dark/Light theme toggle works
- [ ] All sections visible
- [ ] Contact form configured (optional)
- [ ] Resume added (optional)
- [ ] Personal info updated
- [ ] Profile photo added

---

## 🆘 Troubleshooting

**Backend won't start?**
- Make sure Python 3.8+ is installed
- Run: `pip install -r requirements.txt`

**Contact form not working?**
- Check if backend is running at http://localhost:5000
- Check browser console for errors (F12)

**Images not showing?**
- Make sure images are in the `assets` folder
- Check file names match exactly

---

## 📞 Need Help?

Check the full README.md for detailed documentation!
