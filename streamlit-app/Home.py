import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="MindCare - AI Mental Health Monitoring",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': 'User',
        'mood_logs': [],
        'journal_entries': [],
        'chat_history': [],
        'current_streak': 7,
        'total_logs': 45
    }

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 5rem;">🧠</div>
        </div>
    """, unsafe_allow_html=True)
    st.title("🧠 MindCare")
    st.caption("AI Mental Health Monitoring")
    
    st.divider()
    
    st.markdown(f"### Welcome, {st.session_state.user_data['name']}! 👋")
    
    st.metric("Current Streak", f"{st.session_state.user_data['current_streak']} days 🔥")
    st.metric("Total Mood Logs", st.session_state.user_data['total_logs'])
    
    st.divider()
    
    st.error("**🚨 Crisis Support (India)**")
    st.markdown("**KIRAN: 1800-599-0019**")
    st.caption("Mental Health Helpline - 24/7")
    st.markdown("**Vandrevala: 1860-2662-345**")
    st.caption("Free counseling - 24/7")

# Main content
st.title("Dashboard 📊")
st.markdown("### Your Mental Health Overview")

# Alert for high risk
if st.session_state.get('risk_level') == 'high':
    st.error("⚠️ **URGENT**: We're concerned about your well-being. Please contact a mental health professional or call KIRAN: 1800-599-0019 immediately.")

# Metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="metric-card">
            <h3 style="color: #6366f1;">😊 Mental Health Status</h3>
            <h2 style="color: #10b981;">Low Risk</h2>
            <p style="color: #6b7280;">Based on recent activity</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <h3 style="color: #6366f1;">📝 This Week</h3>
            <p><strong>Journal Entries:</strong> 5</p>
            <p><strong>Mood Logs:</strong> 7</p>
            <p><strong>Avg Mood:</strong> 7.2/10</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <h3 style="color: #6366f1;">🔥 Current Streak</h3>
            <h2 style="color: #f59e0b;">7 Days</h2>
            <p style="color: #6b7280;">Keep up the great work!</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="metric-card">
            <h3 style="color: #6366f1;">🏆 Achievements</h3>
            <p>✅ 7-day streak</p>
            <p>✅ 45 mood logs</p>
            <p>✅ 23 journal entries</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Mood trend chart
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Mood Trend (Last 7 Days)")
    
    # Sample data
    dates = [(datetime.now() - timedelta(days=i)).strftime("%a") for i in range(6, -1, -1)]
    mood_scores = [6, 7, 6.5, 8, 7.5, 8, 7]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=mood_scores,
        mode='lines+markers',
        line=dict(color='#6366f1', width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor='rgba(99, 102, 241, 0.1)'
    ))
    
    fig.update_layout(
        xaxis_title="Day",
        yaxis_title="Mood Score",
        yaxis=dict(range=[0, 10]),
        height=300,
        margin=dict(l=0, r=0, t=0, b=0),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💡 Today's Recommendations")
    
    st.info("**Morning Walk**\nTake a 20-minute walk in nature")
    st.success("**Breathing Exercise**\n5-minute guided meditation")
    st.warning("**Stay Connected**\nReach out to a friend today")

st.divider()

# Quick actions
st.subheader("⚡ Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 Log Mood", use_container_width=True):
        st.switch_page("pages/1_Mood_Tracker.py")

with col2:
    if st.button("📝 Write Journal", use_container_width=True):
        st.switch_page("pages/2_Journal.py")

with col3:
    if st.button("💬 Chat with AI", use_container_width=True):
        st.switch_page("pages/3_AI_Chat.py")

with col4:
    if st.button("📚 View Resources", use_container_width=True):
        st.switch_page("pages/4_Resources.py")

st.divider()

# Recent activity
st.subheader("📋 Recent Activity")

tab1, tab2 = st.tabs(["Mood Logs", "Journal Entries"])

with tab1:
    # Sample mood logs - using markdown to avoid PyArrow issues
    st.markdown("""
    | Date | Mood | Notes |
    |------|------|-------|
    | 2024-01-15 | 8/10 | Great day at work! |
    | 2024-01-14 | 7/10 | Feeling good overall |
    | 2024-01-13 | 7.5/10 | A bit tired but okay |
    | 2024-01-12 | 6/10 | Stressful day |
    | 2024-01-11 | 8/10 | Excellent mood today |
    """)

with tab2:
    # Sample journal entries
    st.markdown("**Today** - *Feeling grateful*")
    st.caption("Had a productive day and accomplished my goals...")
    st.divider()
    st.markdown("**Yesterday** - *Reflection*")
    st.caption("Thinking about my progress and growth...")

# Footer
st.divider()
st.caption("💙 Remember: This is a support tool. For professional help, contact a mental health provider.")
st.caption("🚨 Emergency (India): KIRAN 1800-599-0019 | Vandrevala 1860-2662-345 | Police 100")

# Made with Bob
