# 🔧 Troubleshooting Guide - MindCare Streamlit App

## Common Issues and Solutions

### 1. Journal Input Not Clearing ✅ FIXED

**Issue**: Text area doesn't clear after saving entry

**Solution**: Updated to use session state flag for clearing input. The journal now properly clears after saving.

**What was changed**:
- Added `clear_input` flag in session state
- Properly manages text area value
- Clears on both Save and Clear button clicks

---

### 2. Image Not Loading ✅ FIXED

**Issue**: Placeholder image URL not loading in sidebar

**Solution**: Replaced external image with emoji-based logo using HTML/CSS

**What was changed**:
- Removed `st.image()` with external URL
- Added HTML div with large emoji (🧠)
- No external dependencies needed

---

### 3. Sentiment Analysis Import Errors

**Issue**: `ModuleNotFoundError: No module named 'vaderSentiment'` or `'textblob'`

**Solution**: 

```bash
# Install missing packages
pip install vaderSentiment textblob

# Or install all requirements
pip install -r requirements.txt
```

**Fallback**: The journal now includes a simple fallback sentiment analysis if libraries aren't installed.

---

### 4. Streamlit Not Found

**Issue**: `streamlit: command not found`

**Solution**:

```bash
# Install streamlit
pip install streamlit

# Or use the run script
./run.sh
```

---

### 5. Port Already in Use

**Issue**: `Port 8501 is already in use`

**Solution**:

```bash
# Option 1: Use different port
streamlit run Home.py --server.port 8502

# Option 2: Kill existing process
lsof -ti:8501 | xargs kill -9
```

---

### 6. Session State Issues

**Issue**: Data not persisting or unexpected behavior

**Solution**:

1. Clear browser cache
2. Use incognito/private mode
3. Restart Streamlit server
4. Check browser console for errors

---

### 7. Plotly Charts Not Showing

**Issue**: Charts not rendering on Dashboard

**Solution**:

```bash
# Install plotly
pip install plotly

# Verify installation
python -c "import plotly; print(plotly.__version__)"
```

---

### 8. TextBlob Download Error

**Issue**: `LookupError: Resource punkt not found`

**Solution**:

```python
# Run in Python
import nltk
nltk.download('punkt')
nltk.download('brown')
```

Or add to your code:

```python
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
```

---

### 9. Slow Performance

**Issue**: App is slow or laggy

**Solutions**:

1. **Use caching**:
```python
@st.cache_data
def load_data():
    # Your data loading code
    pass
```

2. **Reduce reruns**:
- Use `st.form()` for multiple inputs
- Minimize `st.rerun()` calls

3. **Optimize imports**:
- Move heavy imports inside functions
- Use lazy loading

---

### 10. Chat History Not Saving

**Issue**: Chat messages disappear on page refresh

**Solution**: This is expected behavior with session state. For persistence:

```python
# Add to your code
import json

# Save to file
with open('chat_history.json', 'w') as f:
    json.dump(st.session_state.chat_messages, f)

# Load from file
try:
    with open('chat_history.json', 'r') as f:
        st.session_state.chat_messages = json.load(f)
except FileNotFoundError:
    st.session_state.chat_messages = []
```

---

## Quick Fixes

### Reset Everything

```bash
# Clear Streamlit cache
streamlit cache clear

# Remove session state (restart app)
# Or add this button in your app:
if st.button("Reset All Data"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
```

### Check Installation

```bash
# Verify all packages
pip list | grep -E "streamlit|plotly|vader|textblob"

# Should show:
# streamlit         1.29.0
# plotly            5.18.0
# vaderSentiment    3.3.2
# textblob          0.17.1
```

### Update All Packages

```bash
pip install --upgrade -r requirements.txt
```

---

## Running the App

### Method 1: Simple (Recommended)

```bash
cd ~/Desktop/mental-health-ai/streamlit-app
./run.sh
```

### Method 2: Direct

```bash
cd ~/Desktop/mental-health-ai/streamlit-app
streamlit run Home.py
```

### Method 3: Custom Port

```bash
streamlit run Home.py --server.port 8502
```

### Method 4: Network Access

```bash
streamlit run Home.py --server.address 0.0.0.0
```

---

## Debugging Tips

### Enable Debug Mode

Add to your code:

```python
import streamlit as st

# Show session state
with st.expander("Debug: Session State"):
    st.write(st.session_state)
```

### Check Logs

```bash
# Streamlit logs are in terminal
# Look for errors in red text
```

### Browser Console

1. Open browser DevTools (F12)
2. Check Console tab for JavaScript errors
3. Check Network tab for failed requests

---

## Known Limitations

1. **Session State**: Data doesn't persist after browser refresh
2. **No Authentication**: Single-user mode only
3. **Local Storage**: All data stored in memory
4. **No Database**: Need to add for production use

---

## Getting Help

### Check Documentation

- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Forum](https://discuss.streamlit.io/)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

### Common Error Messages

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Install missing package with pip |
| `Port already in use` | Use different port or kill process |
| `Session state error` | Clear cache and restart |
| `Import error` | Check Python version (need 3.8+) |

---

## Performance Optimization

### 1. Use Caching

```python
@st.cache_data
def expensive_computation():
    # Your code here
    pass
```

### 2. Lazy Loading

```python
# Load only when needed
if st.button("Analyze"):
    from heavy_module import analyze
    result = analyze()
```

### 3. Minimize Reruns

```python
# Use forms to batch inputs
with st.form("my_form"):
    input1 = st.text_input("Input 1")
    input2 = st.text_input("Input 2")
    submitted = st.form_submit_button("Submit")
```

---

## Still Having Issues?

1. **Check Python version**: `python --version` (need 3.8+)
2. **Update pip**: `pip install --upgrade pip`
3. **Reinstall everything**: 
   ```bash
   pip uninstall -r requirements.txt -y
   pip install -r requirements.txt
   ```
4. **Try virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## Contact & Support

For additional help:
- Check the main README.md
- Review code comments
- Test with minimal example first

**Remember**: This is a development version. For production use, add proper database, authentication, and error handling.