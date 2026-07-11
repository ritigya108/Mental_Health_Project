~# 🚀 Quick Start Guide - MindCare AI Mental Health Monitoring

Get your AI-based mental health monitoring solution up and running in minutes!

## 📋 Prerequisites Checklist

Before you begin, make sure you have:
- ✅ Python 3.8 or higher installed
- ✅ Node.js 16 or higher installed
- ✅ Terminal/Command Prompt access
- ✅ Text editor (VS Code recommended)

## 🎯 Step-by-Step Setup

### Step 1: Backend Setup (5 minutes)

Open your terminal and run these commands:

```bash
# Navigate to the backend directory
cd ~/Desktop/mental-health-ai/backend

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install all required packages
pip install -r requirements.txt

# Copy environment configuration
cp .env.example .env

# Initialize the database
python -c "from database import init_db; init_db()"

# Start the backend server
python main.py
```

✅ **Backend is ready!** You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Keep this terminal window open and running.

### Step 2: Frontend Setup (3 minutes)

Open a **NEW** terminal window and run:

```bash
# Navigate to the frontend directory
cd ~/Desktop/mental-health-ai/frontend

# Install all dependencies
npm install

# Start the React development server
npm start
```

✅ **Frontend is ready!** Your browser should automatically open to:
```
http://localhost:3000
```

## 🎉 You're All Set!

Your application is now running:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🧪 Test Your Setup

1. **Open your browser** to http://localhost:3000
2. **Navigate to Dashboard** - You should see the main dashboard
3. **Try Mood Tracker** - Click "Mood Tracker" in the sidebar
4. **Log a mood** - Select a mood and add notes
5. **Check API docs** - Visit http://localhost:8000/docs

## 🔧 Common Issues & Solutions

### Issue: "Command not found: python3"
**Solution**: Try `python` instead of `python3`, or install Python from python.org

### Issue: "Command not found: npm"
**Solution**: Install Node.js from nodejs.org

### Issue: Port 8000 already in use
**Solution**: 
```bash
# Find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

### Issue: Port 3000 already in use
**Solution**: The terminal will ask if you want to use a different port. Type 'Y' and press Enter.

### Issue: Module import errors in backend
**Solution**: Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # Run this in the backend directory
```

### Issue: React dependencies not installing
**Solution**: Clear npm cache and try again:
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

## 📱 Using the Application

### 1. Dashboard
- View your mental health overview
- See mood trends
- Get personalized recommendations

### 2. Mood Tracker
- Log your daily mood (1-10 scale)
- Add notes about your feelings
- Track patterns over time

### 3. Journal (Coming Soon)
- Write journal entries
- Get AI sentiment analysis
- Review past entries

### 4. AI Chat (Coming Soon)
- Chat with AI assistant
- Get support and guidance
- Ask mental health questions

### 5. Resources (Coming Soon)
- Access mental health resources
- Find crisis hotlines
- Learn coping strategies

## 🛠️ Development Tips

### Backend Development
```bash
# Always activate virtual environment first
cd backend
source venv/bin/activate

# Run with auto-reload
uvicorn main:app --reload

# View logs
# Check terminal output for API requests
```

### Frontend Development
```bash
# Run in development mode
npm start

# Build for production
npm run build

# Run tests
npm test
```

## 📊 Next Steps

1. **Explore the codebase**
   - Backend: `backend/main.py` - API routes
   - Frontend: `frontend/src/App.js` - Main app
   - AI: `backend/ai_analyzer.py` - Sentiment analysis

2. **Customize the application**
   - Modify colors in `frontend/src/App.js` (theme section)
   - Add new API endpoints in `backend/main.py`
   - Create new pages in `frontend/src/pages/`

3. **Add features**
   - Implement user authentication
   - Complete the journal page
   - Build the chatbot interface
   - Add more AI models

4. **Deploy to production**
   - Set up a cloud database (PostgreSQL)
   - Deploy backend to Heroku/AWS/DigitalOcean
   - Deploy frontend to Vercel/Netlify
   - Configure environment variables

## 🆘 Getting Help

- **Check the main README**: `README.md` for detailed documentation
- **Backend docs**: `backend/README.md`
- **API documentation**: http://localhost:8000/docs (when running)
- **React docs**: https://react.dev/
- **FastAPI docs**: https://fastapi.tiangolo.com/

## ⚠️ Important Reminders

1. **This is a support tool**, not a replacement for professional mental health care
2. **Keep your virtual environment activated** when working on the backend
3. **Both servers must be running** for the app to work properly
4. **Don't commit sensitive data** (like API keys) to version control
5. **In crisis situations**, call 988 (US) or your local emergency number

## 🎓 Learning Resources

- **Python/FastAPI**: https://fastapi.tiangolo.com/tutorial/
- **React**: https://react.dev/learn
- **Material-UI**: https://mui.com/material-ui/getting-started/
- **AI/ML**: https://huggingface.co/course/chapter1/1

---

**Happy Coding! 🚀**

If you encounter any issues not covered here, check the main README.md or create an issue on GitHub.