# Flask Portfolio - Local Testing Checklist

**MUST COMPLETE BEFORE DEPLOYING TO RENDER**

This checklist verifies everything works correctly in your local environment before pushing to production.

---

## ✅ PHASE 1: ENVIRONMENT SETUP (5 minutes)

- [ ] **1.1** Delete old virtual environment
  ```bash
  rm -rf env
  ```
  OR on Windows:
  ```bash
  rmdir /s /q env
  ```

- [ ] **1.2** Delete cache files
  ```bash
  rm -rf __pycache__
  rm -rf backend/__pycache__
  ```
  OR on Windows:
  ```bash
  for /d /r . %d in (__pycache__) do @if exist "%d" rmdir /s /q "%d"
  ```

- [ ] **1.3** Delete old database (will be recreated)
  ```bash
  rm backend/portfolio.db
  ```
  OR on Windows:
  ```bash
  del backend\portfolio.db
  ```

- [ ] **1.4** Create new virtual environment
  ```bash
  python -m venv env
  ```
  ✓ Should create env/ folder

- [ ] **1.5** Activate virtual environment
  
  **Windows:**
  ```bash
  env\Scripts\activate
  ```
  
  **Mac/Linux:**
  ```bash
  source env/bin/activate
  ```
  
  ✓ You should see (env) at start of terminal prompt

- [ ] **1.6** Verify correct Python is active
  ```bash
  python --version
  ```
  ✓ Should be Python 3.8+ (3.10+ recommended)
  ✓ Should NOT show global Python path

---

## ✅ PHASE 2: DEPENDENCIES (3 minutes)

- [ ] **2.1** Upgrade pip
  ```bash
  python -m pip install --upgrade pip
  ```

- [ ] **2.2** Install requirements
  ```bash
  pip install -r requirements.txt
  ```
  
  Expected output:
  ```
  Successfully installed Flask-3.0.0 Flask-Cors-4.0.0 Flask-Mail-0.9.1 gunicorn-21.2.0 python-dotenv-1.0.0
  ```
  
  ❌ If it fails:
  - Check requirements.txt has correct versions
  - Try: `pip install -r requirements.txt --force-reinstall`

- [ ] **2.3** Verify Flask installed correctly
  ```bash
  python -c "import flask; print(flask.__version__)"
  ```
  ✓ Should print: 3.0.0

- [ ] **2.4** Verify Flask-Mail installed correctly
  ```bash
  python -c "from flask_mail import Mail; print('Flask-Mail OK')"
  ```
  ✓ Should print: Flask-Mail OK
  ❌ If error: requirements.txt missing Flask-Mail

---

## ✅ PHASE 3: CONFIGURATION (2 minutes)

- [ ] **3.1** Create .env file
  ```bash
  cp .env.example .env
  ```
  
  OR manually create .env with minimum content:
  ```
  SECRET_KEY=dev-key-for-testing
  MAIL_USERNAME=your-test@gmail.com
  MAIL_PASSWORD=your-test-password
  MAIL_SERVER=smtp.gmail.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  RECIPIENT_EMAIL=your-test@gmail.com
  FLASK_ENV=development
  FLASK_DEBUG=False
  ```

- [ ] **3.2** Verify folder structure
  ```bash
  ls -la
  ```
  
  Should see:
  ```
  app.py                 ✓
  requirements.txt       ✓
  .env                   ✓
  templates/             ✓
  static/                ✓
  backend/               ✓
  ```

- [ ] **3.3** Verify template files exist
  ```bash
  ls templates/
  ```
  ✓ Should show: index.html

- [ ] **3.4** Verify CSS/JS files exist
  ```bash
  ls static/css/
  ls static/js/
  ```
  ✓ Should show: style.css and main.js

- [ ] **3.5** Verify assets folder
  ```bash
  ls static/assets/
  ```
  ✓ Should show: profile.jpg, projects/, (and optionally resume PDF)

---

## ✅ PHASE 4: APP STARTUP (3 minutes)

- [ ] **4.1** Start Flask server
  ```bash
  python app.py
  ```
  
  ✓ Expected output:
  ```
  ================================================================================
  Starting Flask Portfolio Application
  ================================================================================
  Template directory: C:\...\portfolio\templates
  Static directory: C:\...\portfolio\static
  Base URL: http://localhost:5000
  Debug mode: False
  ================================================================================
  WARNING in app.run(). This is a development server. Do not use it in production.
   * Running on http://0.0.0.0:5000
  ```
  
  ✓ No import errors
  ✓ No module not found errors
  ✓ No database errors
  
  ❌ If errors:
  - Check Python is in virtual environment
  - Check all dependencies installed
  - Check .env file exists

- [ ] **4.2** Server is accessible
  - In another terminal, try:
    ```bash
    curl http://localhost:5000/
    ```
  - ✓ Should return HTML content
  - ❌ If connection refused: Flask didn't start properly

- [ ] **4.3** Keep server running
  - Leave Flask running in a terminal for remaining tests
  - DO NOT close this terminal

---

## ✅ PHASE 5: HTML/UI LOADING (5 minutes)

- [ ] **5.1** Open portfolio in browser
  - Go to: http://localhost:5000
  - ✓ Should see portfolio webpage with styling
  - ❌ If white blank page: CSS not loading
  - ❌ If layout broken: JavaScript not loading

- [ ] **5.2** Check page title
  - Browser tab should show: "Sandesh Bhatta | Portfolio"
  - ✓ Means HTML template rendered correctly

- [ ] **5.3** Check browser console for errors
  - Open DevTools: F12 or Right-click → Inspect
  - Go to Console tab
  - ✓ Should be NO red error messages
  - ❌ If red errors: JavaScript error in main.js or html

- [ ] **5.4** Check Network tab for file status
  - Open DevTools: F12
  - Go to Network tab
  - Reload page: F5
  - Look for these requests and their status:
    ```
    index.html          Status 200 ✓
    style.css           Status 200 ✓
    main.js             Status 200 ✓
    profile.jpg         Status 200 ✓
    ```
  
  ❌ If any 404s:
  - CSS path issue in HTML
  - Static folder not configured
  - Check that HTML uses {{ url_for('static', filename='...') }}

- [ ] **5.5** Verify page elements visible
  - [ ] Navigation bar visible at top
  - [ ] Hero section with title
  - [ ] About section
  - [ ] Skills section
  - [ ] Projects section
  - [ ] Contact form at bottom
  - [ ] Dark/Light theme toggle (if you have it)

- [ ] **5.6** Test theme toggle (if applicable)
  - Click dark/light toggle button
  - ✓ Page should change color scheme
  - ✓ Preference should persist on reload

---

## ✅ PHASE 6: API ENDPOINTS (5 minutes)

Open a NEW terminal (keep Flask running in first terminal)

- [ ] **6.1** Test health endpoint
  ```bash
  curl http://localhost:5000/api/health
  ```
  
  ✓ Expected response:
  ```json
  {"status": "healthy", "timestamp": "2026-01-14T..."}
  ```
  
  ❌ If 404: Flask route not found
  ❌ If error: Check logging output in first terminal

- [ ] **6.2** Test projects endpoint
  ```bash
  curl http://localhost:5000/api/projects
  ```
  
  ✓ Expected response:
  ```json
  []
  ```
  (Empty list if no projects, but valid JSON)
  
  ❌ If directory listing appears: Static folder misconfigured
  ❌ If 404: Flask route not found
  ❌ If not JSON: Projects endpoint has error

- [ ] **6.3** Test stats endpoint
  ```bash
  curl http://localhost:5000/api/stats
  ```
  
  ✓ Expected response:
  ```json
  {"total_contacts": 0, "total_resume_downloads": 0}
  ```
  
  ❌ If error: Database not initialized

- [ ] **6.4** Verify database was created
  ```bash
  ls backend/
  ```
  
  ✓ Should show: portfolio.db (created after first run)

---

## ✅ PHASE 7: CONTACT FORM (5 minutes)

Back in browser at http://localhost:5000

- [ ] **7.1** Locate contact form
  - Scroll to bottom of portfolio
  - Should see contact form with fields:
    - Name
    - Email
    - Subject
    - Message
    - Submit button

- [ ] **7.2** Fill out contact form
  ```
  Name: Test User
  Email: test@example.com
  Subject: Test Message
  Message: This is a test message
  ```

- [ ] **7.3** Submit form
  - Click "Send" or "Submit" button
  - ✓ Should see success message
  - ✓ Form should clear
  
  ❌ If error: Check terminal where Flask is running for error logs

- [ ] **7.4** Verify contact was saved
  ```bash
  sqlite3 backend/portfolio.db "SELECT * FROM contacts;"
  ```
  
  ✓ Should show your test contact
  
  ❌ If nothing: Database save failed

- [ ] **7.5** Check Flask logs
  - Look at first terminal where Flask is running
  - Should see: "Contact saved: ID=..." or "Email sent for contact..."
  - ✓ Confirms backend processed the request

---

## ✅ PHASE 8: RESUME DOWNLOAD (3 minutes)

- [ ] **8.1** Find resume download link
  - In portfolio, find "Download Resume" button
  - OR API endpoint: GET /api/download-resume

- [ ] **8.2** Click resume download
  - ✓ File should download
  - ✓ Check Downloads folder for "Sandesh_Bhatta_Resume.pdf"
  
  ❌ If 404: Resume file not found at static/assets/Sandesh_Bhatta_Resume.pdf

- [ ] **8.3** Verify download was tracked (optional)
  ```bash
  sqlite3 backend/portfolio.db "SELECT * FROM resume_downloads;"
  ```
  
  ✓ Should show one entry

---

## ✅ PHASE 9: ERROR HANDLING (5 minutes)

Test that errors are handled gracefully

- [ ] **9.1** Test invalid route
  ```bash
  curl http://localhost:5000/this-doesnt-exist
  ```
  
  ✓ Should return 404 JSON response
  ✓ Should NOT crash Flask

- [ ] **9.2** Test malformed contact request
  ```bash
  curl -X POST http://localhost:5000/api/contact \
    -H "Content-Type: application/json" \
    -d '{"name": "", "email": ""}'
  ```
  
  ✓ Should return 400 with error message
  ✓ Should NOT crash Flask

- [ ] **9.3** Check Flask is still running
  ```bash
  curl http://localhost:5000/api/health
  ```
  
  ✓ Should still work after errors

---

## ✅ PHASE 10: DEPLOYMENT READINESS (5 minutes)

Last checks before pushing to Render

- [ ] **10.1** Verify no .env file will be committed
  ```bash
  cat .gitignore | grep ".env"
  ```
  
  ✓ Should show: .env (in .gitignore)
  
  ```bash
  git status
  ```
  
  ✓ Should NOT show .env in changes
  ❌ If .env shows in git: Add to .gitignore immediately

- [ ] **10.2** Verify no hardcoded secrets
  ```bash
  grep -r "bhattasandesh148@gmail.com" --include="*.py"
  ```
  
  ❌ If found: Remove and use environment variable instead

- [ ] **10.3** Verify static files will be included
  ```bash
  git status
  ```
  
  ✓ Should show new files in:
  - static/css/
  - static/js/
  - static/assets/
  - templates/

- [ ] **10.4** Test gunicorn (production server)
  
  Stop Flask: Ctrl+C in first terminal
  
  ```bash
  gunicorn app:app
  ```
  
  ✓ Should start without errors
  ✓ Should show: "Listening on 0.0.0.0:8000"
  
  Try in browser: http://localhost:8000
  ✓ Should work same as Flask development server
  
  Stop gunicorn: Ctrl+C

- [ ] **10.5** Test with gunicorn config
  ```bash
  gunicorn app:app --workers=1 --bind=0.0.0.0:5000
  ```
  
  ✓ Should start on port 5000
  ✓ Should handle requests

---

## ✅ FINAL CHECKLIST

Before deploying to Render:

- [ ] All tests in phases 1-10 passed
- [ ] No import errors
- [ ] No 404 on CSS/JS
- [ ] HTML page loads with styling
- [ ] API endpoints return JSON (not errors)
- [ ] Contact form works
- [ ] Database created and stores data
- [ ] Error handling works (doesn't crash)
- [ ] No secrets in code
- [ ] .env in .gitignore
- [ ] Gunicorn works
- [ ] Code committed to GitHub

---

## 🚀 DEPLOYMENT

Once all tests pass:

```bash
git add .
git commit -m "Flask portfolio - ready for Render deployment"
git push origin main
```

Then:
1. Go to render.com/dashboard
2. Create new Web Service
3. Deploy!

---

## 🆘 TROUBLESHOOTING QUICK REFERENCE

| Problem | Cause | Fix |
|---------|-------|-----|
| Flask won't start | Virtual env not activated | `source env/bin/activate` or `env\Scripts\activate` |
| ModuleNotFoundError | Dependency missing | `pip install -r requirements.txt` |
| 404 on CSS/JS | Wrong path in HTML | Use `{{ url_for('static', filename='...') }}` |
| White blank page | Static folder not configured | Check app.py has proper Flask() config |
| Contact form doesn't send | Email credentials wrong | Check .env has correct MAIL_USERNAME/PASSWORD |
| Database locked | SQLite issue | Database will auto-unlock on Render (use PostgreSQL) |
| Gunicorn won't start | Flask errors | Check Flask runs first without errors |

---

**THIS CHECKLIST IS COMPLETE AND PRODUCTION-READY**

Follow every step before deploying. Your portfolio will work perfectly on Render if all tests pass locally.

