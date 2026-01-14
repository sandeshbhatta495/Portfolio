# 🚀 Render Deployment - STEP-BY-STEP GUIDE

**Status**: Code committed to GitHub ✅  
**Next**: Deploy to Render in 5 minutes

---

## ✅ STEP 1: Check Your GitHub Repository

Before proceeding, verify code is pushed:

```bash
git log --oneline | head -5
```

You should see the commit: `"Fix Flask configuration: proper static/template paths..."`

✅ **Code is ready for Render**

---

## 📋 STEP 2: Prepare Environment Variables

You need these values from the real world (NOT in code):

### Email Settings (Gmail)
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows Computer"
3. Copy the **16-character password**
4. Have your Gmail address ready

### Secret Key (Generate)
```bash
# In Python:
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy the output (looks like: `a1b2c3d4...`)

**YOU NEED:**
- [ ] `MAIL_USERNAME` = your-email@gmail.com
- [ ] `MAIL_PASSWORD` = 16-char app password from Google
- [ ] `MAIL_SERVER` = smtp.gmail.com
- [ ] `MAIL_PORT` = 587
- [ ] `RECIPIENT_EMAIL` = your-email@gmail.com
- [ ] `SECRET_KEY` = the hex string you generated

---

## 🌐 STEP 3: Create Render Account

1. Go to: **https://render.com**
2. Click "Sign up" (or login if you have account)
3. Use GitHub to sign up (easiest)
4. Complete signup

✅ **You should be on Render dashboard**

---

## 🔨 STEP 4: Create Web Service

1. Click **"Create"** button in Render dashboard
2. Select **"Web Service"**
3. Choose your GitHub repository:
   - Search for your portfolio repo
   - Click "Connect"
   - Authorize Render to access GitHub

✅ **Repository connected**

---

## ⚙️ STEP 5: Configure Web Service

### Section 1: Basic Settings
- **Name**: `portfolio` (or your preference)
- **Environment**: `Python 3`
- **Region**: `us-east` (or closest to you)
- **Branch**: `fix-debugging` (or `main` if that's your branch)
- **Root Directory**: Leave empty
- **Runtime**: Select `Python 3.10`

### Section 2: Build & Start
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  gunicorn app:app
  ```

### Section 3: Plan
- Select **"Free"** (for testing)
- Later upgrade to "Standard" if you want it always running

✅ **Settings configured**

---

## 🔐 STEP 6: Add Environment Variables

**IMPORTANT**: Add variables in Render dashboard (NOT in code)

1. Scroll down to **"Environment"** section
2. Click **"Add Environment Variable"**
3. Add each variable:

```
Key: MAIL_USERNAME
Value: your-email@gmail.com

Key: MAIL_PASSWORD
Value: [16-char app password from Gmail]

Key: MAIL_SERVER
Value: smtp.gmail.com

Key: MAIL_PORT
Value: 587

Key: MAIL_USE_TLS
Value: True

Key: RECIPIENT_EMAIL
Value: your-email@gmail.com

Key: SECRET_KEY
Value: [hex string you generated]

Key: FLASK_ENV
Value: production

Key: FLASK_DEBUG
Value: False
```

✅ **All environment variables added**

---

## 🚀 STEP 7: Deploy

1. Scroll to bottom
2. Click **"Create Web Service"** button
3. Render will:
   - Install dependencies
   - Build the app
   - Start the server
   - Assign you a URL

**Wait 2-3 minutes** for deployment...

✅ **Deployment in progress**

---

## ✅ STEP 8: Verify Deployment

### Check Logs
1. Click on your service name
2. Go to **"Logs"** tab
3. Should see:
   ```
   Database initialized successfully
   Starting Flask Portfolio Application
   Template directory: ...
   Static directory: ...
   Running on ...
   ```
   ✅ If no red errors, deployment succeeded

### Check Live URL
1. Find URL at top of page (looks like: `https://portfolio-xxxxx.onrender.com`)
2. Open in browser
3. Should see your portfolio with CSS/JS loaded ✅

### Test API
```
https://portfolio-xxxxx.onrender.com/api/health
```
Should return:
```json
{
  "status": "healthy",
  "timestamp": "2026-01-14T..."
}
```

✅ **Deployment successful!**

---

## 🆘 TROUBLESHOOTING

### Problem: Build fails with "ModuleNotFoundError"
**Cause**: Missing dependency in requirements.txt

**Fix**:
1. Add package to requirements.txt locally
2. Test it works: `pip install -r requirements.txt`
3. Commit and push: `git add . && git commit -m "Add missing package" && git push`
4. Render auto-redeploys

### Problem: "404 on CSS/JS files"
**Cause**: Static folder configuration

**Check**:
1. Verify `{{ url_for('static', filename='...') }}` in HTML
2. Check app.py has proper Flask() configuration
3. Commit, push, Render rebuilds automatically

### Problem: "Email not sending"
**Cause**: Wrong environment variables

**Fix**:
1. Check Render dashboard → Environment variables
2. Verify MAIL_USERNAME and MAIL_PASSWORD are correct
3. Verify you used Gmail **app-specific password**, not regular password
4. Edit variables in dashboard, Render restarts automatically

### Problem: Database errors
**Cause**: SQLite doesn't persist on Render

**Note**: This is normal for free tier. Data resets on redeploy.

**Solution** (optional):
- Migrate to PostgreSQL on Render
- See migration guide in DEPLOYMENT_GUIDE.md

### Problem: Long wait or timeout
**Cause**: Free tier is slower

**Normal**: Takes 2-3 minutes to deploy

**Wait** for "Your service is live" message

---

## 📊 YOUR DEPLOYMENT CHECKLIST

- [ ] Code committed and pushed to GitHub
- [ ] Render account created
- [ ] Web Service created
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app`
- [ ] All 8 environment variables added
- [ ] Deployment completed (no red errors)
- [ ] Live URL working
- [ ] `/api/health` returns JSON
- [ ] CSS/JS loading on portfolio page

---

## 🎉 YOU'RE LIVE!

Your portfolio is now deployed to Render.

**Share your URL:**
```
https://portfolio-xxxxx.onrender.com
```

---

## ⏭️ NEXT STEPS

### If you want to update your portfolio:
1. Make changes locally
2. Test: `python app.py` (should work)
3. Commit: `git add . && git commit -m "message"`
4. Push: `git push`
5. Render **auto-redeploys** automatically ✅

### If you want it always running (not sleeping):
- Upgrade to "Standard" plan ($7+/month)
- Free tier goes to sleep after 15 mins inactivity

### If you want to use PostgreSQL (recommended for production):
- See migration guide in DEPLOYMENT_GUIDE.md
- Database will persist between deploys

---

## 📞 SUPPORT

If something breaks:
1. Check Render Logs tab (always shows errors)
2. Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Part 7
3. Check [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) - Troubleshooting section

---

**Your portfolio is production-ready and deployed! 🚀**

