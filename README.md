# 🧠 MindCare - AI-Based Mental Health Monitoring Solution

An intelligent mental health monitoring and support system powered by AI, designed to help users track their mental well-being, identify patterns, and receive personalized recommendations.

## 🌟 Features

### Core Features
- 📊 **Mood Tracking**: Daily mood logging with visual trends and analytics
- 📝 **AI-Powered Journal**: Sentiment analysis on journal entries using NLP
- 🤖 **Intelligent Chatbot**: AI assistant for mental health support
- ⚠️ **Crisis Detection**: Automatic detection of concerning keywords and patterns
- 📈 **Risk Assessment**: Multi-factor mental health risk evaluation
- 💡 **Personalized Recommendations**: AI-generated suggestions based on user data
- 📚 **Resource Library**: Curated mental health resources and hotlines
- 👤 **User Profiles**: Secure user management with emergency contacts

### AI/ML Capabilities
- Sentiment analysis using multiple models (VADER, TextBlob, Transformers)
- Pattern recognition in mood and behavior
- Predictive risk assessment
- Natural language processing for journal analysis
- Crisis keyword detection

## 🏗️ Architecture

```
mental-health-ai/
├── backend/                 # FastAPI Backend
│   ├── main.py             # API routes and application
│   ├── models.py           # Database models
│   ├── database.py         # Database configuration
│   ├── ai_analyzer.py      # AI/ML sentiment analysis
│   ├── requirements.txt    # Python dependencies
│   └── README.md           # Backend documentation
│
└── frontend/               # React Frontend
    ├── public/             # Static files
    ├── src/
    │   ├── components/     # Reusable components
    │   ├── pages/          # Page components
    │   ├── services/       # API services
    │   └── utils/          # Utility functions
    ├── package.json        # Node dependencies
    └── README.md           # Frontend documentation
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **pip** (Python package manager)
- **npm** or **yarn** (Node package manager)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd mental-health-ai/backend
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database**
   ```bash
   python -c "from database import init_db; init_db()"
   ```

6. **Run the server**
   ```bash
   python main.py
   # Or: uvicorn main:app --reload
   ```

   Backend will be available at: `http://localhost:8000`
   API Docs: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd mental-health-ai/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # Or: yarn install
   ```

3. **Start development server**
   ```bash
   npm start
   # Or: yarn start
   ```

   Frontend will be available at: `http://localhost:3000`

## 📱 Usage

### For Users

1. **Access the application** at `http://localhost:3000`
2. **Create an account** or log in
3. **Log your mood** daily using the mood tracker
4. **Write journal entries** to track your thoughts
5. **Chat with the AI** for support and guidance
6. **View your dashboard** to see trends and insights
7. **Access resources** for additional help

### For Developers

1. **Backend API Documentation**: Visit `http://localhost:8000/docs` for interactive API documentation
2. **Modify AI models**: Edit `backend/ai_analyzer.py` to customize sentiment analysis
3. **Add new features**: Follow the existing code structure in both backend and frontend
4. **Test endpoints**: Use the Swagger UI or tools like Postman

## 🔧 Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **AI/ML Libraries**:
  - Transformers (Hugging Face)
  - VADER Sentiment Analysis
  - TextBlob
  - scikit-learn
  - PyTorch
- **Authentication**: JWT tokens
- **API Documentation**: Swagger/OpenAPI

### Frontend
- **Framework**: React 18
- **UI Library**: Material-UI (MUI)
- **Routing**: React Router v6
- **Charts**: Recharts
- **HTTP Client**: Axios
- **State Management**: React Hooks

## 📊 API Endpoints

### Health & Status
- `GET /` - Root endpoint
- `GET /health` - Health check

### User Management
- `POST /api/users/register` - Register new user
- `GET /api/users/{user_id}` - Get user profile

### Mood Tracking
- `POST /api/mood/log` - Log mood entry
- `GET /api/mood/history/{user_id}` - Get mood history

### Journal
- `POST /api/journal/entry` - Create journal entry
- `GET /api/journal/entries/{user_id}` - Get journal entries

### AI Analysis
- `POST /api/analyze/sentiment` - Analyze text sentiment
- `GET /api/analyze/risk/{user_id}` - Assess mental health risk

### Recommendations
- `GET /api/recommendations/{user_id}` - Get personalized recommendations

### Chatbot
- `POST /api/chat` - Chat with AI assistant

## 🔒 Security & Privacy

- All health data is encrypted
- JWT-based authentication
- HTTPS in production (recommended)
- No data sharing with third parties
- Compliance considerations for HIPAA/GDPR
- Emergency contact system for crisis situations

## ⚠️ Important Disclaimer

**This application is a support tool and NOT a replacement for professional mental health care.**

- Always consult qualified mental health professionals for serious concerns
- In case of emergency, call your local emergency number or crisis hotline
- US Crisis Hotline: 988 (Suicide & Crisis Lifeline)
- This tool should complement, not replace, professional treatment

## 🛣️ Roadmap

### Phase 1: Foundation ✅
- [x] Project structure setup
- [x] Backend API with FastAPI
- [x] Frontend with React
- [x] Basic mood tracking
- [x] AI sentiment analysis

### Phase 2: Core Features (In Progress)
- [ ] User authentication system
- [ ] Complete journal functionality
- [ ] Enhanced AI chatbot
- [ ] Data visualization improvements
- [ ] Mobile responsiveness

### Phase 3: Advanced Features
- [ ] Machine learning model training
- [ ] Predictive analytics
- [ ] Integration with wearables
- [ ] Therapist portal
- [ ] Group support features

### Phase 4: Production
- [ ] Security audit
- [ ] Performance optimization
- [ ] Cloud deployment
- [ ] Mobile app (React Native)
- [ ] HIPAA compliance

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React code
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PRs

## 🐛 Known Issues

- Authentication not yet implemented (using mock user ID)
- Some pages are placeholders (Journal, Chat, Resources, Profile)
- AI models need fine-tuning for better accuracy
- Database migrations not set up

## 📚 Resources

### Mental Health Resources
- National Suicide Prevention Lifeline: 988 (US)
- Crisis Text Line: Text HOME to 741741
- NAMI (National Alliance on Mental Illness): https://www.nami.org/
- Mental Health America: https://www.mhanational.org/

### Technical Documentation
- FastAPI: https://fastapi.tiangolo.com/
- React: https://react.dev/
- Material-UI: https://mui.com/
- Transformers: https://huggingface.co/docs/transformers

## 📄 License

This project is for educational and support purposes. Please consult with legal counsel regarding healthcare data regulations in your jurisdiction.

## 👥 Team

- **Developer**: Your Name
- **Project Type**: AI-Based Mental Health Monitoring Solution
- **Status**: In Development

## 📞 Support

For questions or support:
- Open an issue on GitHub
- Email: support@mindcare.example.com (placeholder)

## 🙏 Acknowledgments

- Mental health professionals who provided guidance
- Open-source AI/ML community
- All contributors and testers

---

**Remember**: Your mental health matters. This tool is here to support you, but professional help is always available when you need it. 💙