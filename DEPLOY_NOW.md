# 🚀 DEPLOY NOW - QUICK SUMMARY

## ✅ DONE
- Code is committed to GitHub ✅
- All files fixed and ready ✅
- Flask tested locally (runs perfectly) ✅

## 📋 DO THIS NOW (5 minutes)

### 1. Collect Information
You'll need:
- [ ] Gmail address (for contact form emails)
- [ ] Gmail app-specific password (from myaccount.google.com/apppasswords)
- [ ] A name for your portfolio service (e.g., "portfolio", "sandesh-portfolio")

### 2. Go to Render
Open: **https://render.com**
- Sign up with GitHub
- Go to dashboard

### 3. Create Web Service
- Click "Create" → "Web Service"
- Select your GitHub repository
- Connect

### 4. Configure (Copy-Paste These)

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn app:app
```

### 5. Add Environment Variables (Important!)

Add these in Render dashboard:

| Key | Value |
|-----|-------|
| MAIL_USERNAME | your-email@gmail.com |
| MAIL_PASSWORD | [16-char app password] |
| MAIL_SERVER | smtp.gmail.com |
| MAIL_PORT | 587 |
| MAIL_USE_TLS | True |
| RECIPIENT_EMAIL | your-email@gmail.com |
| SECRET_KEY | [generate with: python -c "import secrets; print(secrets.token_hex(32))"] |
| FLASK_ENV | production |
| FLASK_DEBUG | False |

### 6. Deploy
Click "Create Web Service"

Wait 2-3 minutes...

### 7. Test
1. Find your URL (top of page)
2. Open in browser
3. Should see portfolio with CSS/JS ✅
4. Test API: `https://your-url/api/health`

---

## 📞 NEED HELP?

Read: **[RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)** (detailed 8-step guide)

---

**THAT'S IT! Your portfolio will be live in 5 minutes! 🎉**

