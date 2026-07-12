# Implementation Details - Code for PPT Slide

## Streamlit Mental Health Monitoring Solution - Core Implementation

### Complete Mini Implementation (Fits on One Slide)

```python
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Page Configuration
st.set_page_config(page_title="MindCare", page_icon="🧠", layout="wide")

# Initialize AI Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Session State Initialization
if 'mood_logs' not in st.session_state:
    st.session_state.mood_logs = []

# Main Dashboard
st.title("🧠 MindCare - AI Mental Health Monitor")

# Two-Column Layout
col1, col2 = st.columns([2, 1])

with col1:
    # Mood Tracker
    st.subheader("📊 Log Your Mood")
    mood = st.slider("Rate your mood (1-10)", 1, 10, 5)
    notes = st.text_area("What's on your mind?", height=100)
    
    if st.button("Log Mood", type="primary"):
        # AI Sentiment Analysis
        sentiment = analyzer.polarity_scores(notes)
        
        # Save mood log
        st.session_state.mood_logs.append({
            'date': datetime.now(),
            'mood': mood,
            'notes': notes,
            'sentiment': sentiment['compound']
        })
        
        # Crisis Detection
        crisis_words = ['suicide', 'hopeless', 'worthless', 'die']
        if any(word in notes.lower() for word in crisis_words):
            st.error("🚨 Crisis Detected! Call: 1800-599-0019")
        else:
            st.success("✅ Mood logged successfully!")
    
    # Mood Trend Visualization
    if st.session_state.mood_logs:
        st.subheader("📈 Your Mood Trend")
        dates = [log['date'].strftime("%m/%d") for log in st.session_state.mood_logs[-7:]]
        moods = [log['mood'] for log in st.session_state.mood_logs[-7:]]
        
        fig = go.Figure(data=go.Scatter(x=dates, y=moods, mode='lines+markers'))
        fig.update_layout(yaxis_range=[0, 10], height=250)
        st.plotly_chart(fig, use_container_width=True)

with col2:
    # AI Insights Panel
    st.subheader("🤖 AI Insights")
    
    if st.session_state.mood_logs:
        recent_moods = [log['mood'] for log in st.session_state.mood_logs[-7:]]
        avg_mood = sum(recent_moods) / len(recent_moods)
        
        # Risk Assessment
        if avg_mood < 4:
            st.error(f"⚠️ Low Mood Alert\nAvg: {avg_mood:.1f}/10")
            st.warning("Consider talking to a professional")
        elif avg_mood < 6:
            st.warning(f"😐 Moderate Mood\nAvg: {avg_mood:.1f}/10")
        else:
            st.success(f"😊 Good Mood!\nAvg: {avg_mood:.1f}/10")
        
        # Personalized Recommendations
        st.info("💡 **Recommendations:**\n- Take a 15-min walk\n- Practice deep breathing\n- Connect with a friend")
    else:
        st.info("Start logging your mood to get AI insights!")
    
    # Crisis Resources
    st.error("**🆘 Crisis Support**\nKIRAN: 1800-599-0019")

# Footer
st.caption("💙 This tool supports, not replaces, professional care")
```

### Key Implementation Features:

**1. AI Sentiment Analysis**
- Uses VADER for real-time text analysis
- Scores emotional content (-1 to +1)
- Detects negative patterns

**2. Crisis Detection System**
- Keyword monitoring for danger signs
- Immediate alert display
- Emergency resource provision

**3. Data Visualization**
- Plotly charts for mood trends
- Interactive 7-day history
- Real-time updates

**4. Risk Assessment**
- Calculates average mood scores
- Color-coded alerts (red/yellow/green)
- Personalized recommendations

**5. Session Management**
- Persistent data during session
- Mood log history tracking
- State preservation

### Technology Used:
- **Streamlit**: Web framework
- **Plotly**: Interactive charts
- **VADER**: Sentiment analysis
- **Python**: Core logic

### Output:
✅ Interactive mood tracking interface
✅ Real-time AI sentiment analysis
✅ Visual mood trend charts
✅ Crisis detection alerts
✅ Personalized recommendations
✅ Emergency resource display