import axios from 'axios';

// API base URL - change this to your backend URL
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for handling errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// API Service Methods
const apiService = {
  // Health Check
  healthCheck: async () => {
    const response = await api.get('/health');
    return response.data;
  },

  // User Management
  registerUser: async (userData) => {
    const response = await api.post('/api/users/register', userData);
    return response.data;
  },

  getUserProfile: async (userId) => {
    const response = await api.get(`/api/users/${userId}`);
    return response.data;
  },

  // Mood Tracking
  logMood: async (moodData) => {
    const response = await api.post('/api/mood/log', moodData);
    return response.data;
  },

  getMoodHistory: async (userId, days = 7) => {
    const response = await api.get(`/api/mood/history/${userId}`, {
      params: { days },
    });
    return response.data;
  },

  // Journal
  createJournalEntry: async (entryData) => {
    const response = await api.post('/api/journal/entry', entryData);
    return response.data;
  },

  getJournalEntries: async (userId, limit = 10) => {
    const response = await api.get(`/api/journal/entries/${userId}`, {
      params: { limit },
    });
    return response.data;
  },

  // AI Analysis
  analyzeSentiment: async (text) => {
    const response = await api.post('/api/analyze/sentiment', null, {
      params: { text },
    });
    return response.data;
  },

  assessRisk: async (userId) => {
    const response = await api.get(`/api/analyze/risk/${userId}`);
    return response.data;
  },

  // Recommendations
  getRecommendations: async (userId) => {
    const response = await api.get(`/api/recommendations/${userId}`);
    return response.data;
  },

  // Chatbot
  sendChatMessage: async (message, userId) => {
    const response = await api.post('/api/chat', null, {
      params: { message, user_id: userId },
    });
    return response.data;
  },
};

export default apiService;

// Made with Bob
