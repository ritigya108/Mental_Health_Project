from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Mental Health AI Monitoring API",
    description="AI-powered mental health monitoring and support system",
    version="1.0.0"
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class MoodEntry(BaseModel):
    user_id: str
    mood_score: int  # 1-10 scale
    notes: Optional[str] = None
    timestamp: Optional[datetime] = None

class JournalEntry(BaseModel):
    user_id: str
    content: str
    timestamp: Optional[datetime] = None

class SentimentResponse(BaseModel):
    sentiment: str
    score: float
    risk_level: str
    recommendations: List[str]

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str
    age: Optional[int] = None
    emergency_contact: Optional[str] = None

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Mental Health AI Monitoring API",
        "status": "active",
        "version": "1.0.0"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

# Mood tracking endpoints
@app.post("/api/mood/log")
async def log_mood(entry: MoodEntry):
    """Log a mood entry for a user"""
    # TODO: Save to database
    return {
        "message": "Mood logged successfully",
        "entry": entry,
        "timestamp": datetime.now()
    }

@app.get("/api/mood/history/{user_id}")
async def get_mood_history(user_id: str, days: int = 7):
    """Get mood history for a user"""
    # TODO: Fetch from database
    return {
        "user_id": user_id,
        "days": days,
        "entries": []  # Placeholder
    }

# Journal endpoints
@app.post("/api/journal/entry")
async def create_journal_entry(entry: JournalEntry):
    """Create a new journal entry with AI sentiment analysis"""
    # TODO: Implement sentiment analysis
    # TODO: Save to database
    return {
        "message": "Journal entry created",
        "entry": entry,
        "analysis": {
            "sentiment": "neutral",
            "score": 0.5,
            "risk_level": "low"
        }
    }

@app.get("/api/journal/entries/{user_id}")
async def get_journal_entries(user_id: str, limit: int = 10):
    """Get journal entries for a user"""
    # TODO: Fetch from database
    return {
        "user_id": user_id,
        "entries": []  # Placeholder
    }

# AI Analysis endpoints
@app.post("/api/analyze/sentiment")
async def analyze_sentiment(text: str):
    """Analyze sentiment of text using AI"""
    # TODO: Implement AI sentiment analysis
    return {
        "text": text,
        "sentiment": "neutral",
        "score": 0.5,
        "confidence": 0.8
    }

@app.get("/api/analyze/risk/{user_id}")
async def assess_risk(user_id: str):
    """Assess mental health risk level for a user"""
    # TODO: Implement risk assessment algorithm
    return {
        "user_id": user_id,
        "risk_level": "low",
        "factors": [],
        "recommendations": [
            "Continue regular check-ins",
            "Maintain healthy sleep schedule",
            "Practice mindfulness exercises"
        ]
    }

# User management endpoints
@app.post("/api/users/register")
async def register_user(user: UserProfile):
    """Register a new user"""
    # TODO: Implement user registration with password hashing
    return {
        "message": "User registered successfully",
        "user_id": user.user_id
    }

@app.get("/api/users/{user_id}")
async def get_user_profile(user_id: str):
    """Get user profile"""
    # TODO: Fetch from database
    return {
        "user_id": user_id,
        "profile": {}  # Placeholder
    }

# Recommendations endpoint
@app.get("/api/recommendations/{user_id}")
async def get_recommendations(user_id: str):
    """Get personalized mental health recommendations"""
    # TODO: Implement AI-based recommendation engine
    return {
        "user_id": user_id,
        "recommendations": [
            {
                "type": "exercise",
                "title": "Morning Walk",
                "description": "Take a 20-minute walk in nature",
                "priority": "high"
            },
            {
                "type": "meditation",
                "title": "Breathing Exercise",
                "description": "5-minute guided breathing meditation",
                "priority": "medium"
            },
            {
                "type": "resource",
                "title": "Mental Health Hotline",
                "description": "24/7 support available",
                "priority": "info"
            }
        ]
    }

# Chatbot endpoint
@app.post("/api/chat")
async def chat(message: str, user_id: str):
    """Chat with AI mental health assistant"""
    # TODO: Implement chatbot using LangChain/OpenAI
    return {
        "user_message": message,
        "bot_response": "I'm here to listen. How are you feeling today?",
        "timestamp": datetime.now()
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# Made with Bob
