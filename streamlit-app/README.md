# 🧠 MindCare - Streamlit Version

AI-powered mental health monitoring application built with Streamlit.

## 🌟 Features

- **📊 Dashboard** - Overview of your mental health status with charts and metrics
- **😊 Mood Tracker** - Log daily mood with interactive slider and emoji visualization
- **📝 Journal** - Write entries with real-time AI sentiment analysis
- **💬 AI Chat** - Intelligent chatbot for mental health support
- **📚 Resources** - Crisis hotlines, articles, videos, and exercises
- **👤 Profile** - Manage your account and settings

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd streamlit-app
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run Home.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 📁 Project Structure

```
streamlit-app/
├── Home.py                      # Main dashboard page
├── pages/
│   ├── 1_Mood_Tracker.py       # Mood logging interface
│   ├── 2_Journal.py            # Journal with AI analysis
│   ├── 3_AI_Chat.py            # Chatbot interface
│   ├── 4_Resources.py          # Mental health resources
│   └── 5_Profile.py            # User profile and settings
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🎯 How to Use

### Dashboard (Home)
- View your mental health overview
- See mood trends with interactive charts
- Check current streak and statistics
- Quick access to all features

### Mood Tracker
- Rate your mood from 1-10
- Add optional notes
- View mood history
- Quick emoji selection

### Journal
- Write journal entries
- Get instant AI sentiment analysis
- View past entries with sentiment scores
- Track emotional patterns

### AI Chat
- Chat with AI mental health companion
- Get support for anxiety, stress, depression
- Crisis detection and intervention
- Quick response buttons

### Resources
- Access crisis hotlines (988, Crisis Text Line)
- Read educational articles
- Watch helpful videos
- Try practical exercises

### Profile
- Update personal information
- Manage notification settings
- View your statistics
- Security settings

## 🔧 Configuration

### Customization

You can customize the app by modifying:
- **Theme**: Edit `.streamlit/config.toml` (create if doesn't exist)
- **Colors**: Modify CSS in each page file
- **Content**: Update text and resources in page files

### Example config.toml

```toml
[theme]
primaryColor = "#6366f1"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## 🤖 AI Features

### Sentiment Analysis
- **VADER**: Rule-based sentiment analysis
- **TextBlob**: Pattern-based sentiment analysis
- **Combined Score**: Average of multiple models

### Crisis Detection
Automatically detects concerning keywords:
- Suicide-related terms
- Self-harm indicators
- Severe depression markers

## 📊 Data Storage

Currently uses Streamlit's session state for data storage. For production:
- Add database integration (SQLite, PostgreSQL)
- Implement user authentication
- Add data persistence

## ⚠️ Important Notes

1. **Not a Replacement**: This app is a support tool, not a replacement for professional mental health care
2. **Crisis Support**: Always call 988 (US) or local emergency services in crisis
3. **Privacy**: Data is stored locally in session state (not persistent)
4. **Development**: This is a development version, not production-ready

## 🔒 Security Considerations

For production deployment:
- [ ] Add user authentication
- [ ] Implement HTTPS
- [ ] Add database encryption
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Follow HIPAA/GDPR compliance

## 🚀 Deployment

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Local Network

```bash
streamlit run Home.py --server.address 0.0.0.0
```

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "Home.py"]
```

## 📝 Development

### Adding New Pages

1. Create new file in `pages/` directory
2. Name it with number prefix: `6_New_Page.py`
3. Add page configuration:
```python
import streamlit as st
st.set_page_config(page_title="New Page", page_icon="🎯")
```

### Modifying AI Responses

Edit the `get_bot_response()` function in `3_AI_Chat.py`

## 🐛 Troubleshooting

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Port Already in Use
```bash
streamlit run Home.py --server.port 8502
```

### Session State Issues
Clear browser cache or use incognito mode

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Mental Health Resources](https://www.nami.org/)

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Database integration
- User authentication
- More AI models
- Mobile optimization
- Additional features

## 📄 License

Educational and support purposes. Consult legal counsel for healthcare data regulations.

## 🆘 Support

**Crisis Resources:**
- **988** - Suicide & Crisis Lifeline (US)
- **741741** - Crisis Text Line (Text HOME)
- **911** - Emergency Services

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Mental health professionals for guidance
- Open-source AI/ML community

---

**Remember: Your mental health matters. This tool is here to support you, but professional help is always available when you need it.** 💙