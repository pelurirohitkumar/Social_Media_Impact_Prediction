import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# ----------------------------
# Custom CSS & Theme
# ----------------------------
def inject_custom_css():
    st.markdown("""
    <style>
        /* Variables & Base */
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --success-color: #10b981;
            --danger-color: #ef4444;
            --warning-color: #f59e0b;
            --dark-bg: #0f172a;
            --card-bg: #1e293b;
            --border-color: #334155;
        }
        
        /* Main Container */
        .stMainBlockContainer {
            background: linear-gradient(135deg, #0f172a 0%, #1a1f3a 50%, #0f172a 100%);
            color: #e2e8f0;
        }
        
        /* Header Styling */
        .main-header {
            background: var(--primary-gradient);
            padding: 2.5rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            box-shadow: 0 25px 50px -12px rgba(102, 126, 234, 0.4);
            text-align: center;
        }
        
        .main-header h1 {
            font-size: 3rem;
            font-weight: 800;
            color: white;
            margin: 0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            letter-spacing: -1px;
        }
        
        .main-header p {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            margin-top: 0.5rem;
            font-weight: 300;
        }
        
        /* Section Headers */
        .section-header {
            font-size: 1.5rem;
            font-weight: 700;
            color: #e2e8f0;
            margin: 2rem 0 1.5rem 0;
            padding-bottom: 1rem;
            border-bottom: 2px solid var(--border-color);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* Input Container */
        .input-container {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .input-container:hover {
            border-color: #667eea;
            box-shadow: 0 15px 40px -5px rgba(102, 126, 234, 0.2);
        }
        
        /* Input Group */
        .input-group {
            margin-bottom: 1.5rem;
        }
        
        .input-group label {
            display: block;
            color: #cbd5e1;
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }
        
        /* Enhanced Label Styling */
        .input-label {
            font-size: 1.1rem;
            font-weight: 800;
            color: #e2e8f0;
            display: block;
            margin-bottom: 0.75rem;
            margin-top: 1rem;
            padding-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 2px solid #667eea;
        }
        
        .section-subheading {
            font-size: 1.4rem;
            font-weight: 800;
            color: #e2e8f0;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 3px solid;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* Prediction Button */
        .predict-button {
            background: var(--primary-gradient);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 12px;
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            width: 100%;
            margin-top: 2rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px -5px rgba(102, 126, 234, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .predict-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 40px -5px rgba(102, 126, 234, 0.4);
        }
        
        .predict-button:active {
            transform: translateY(0);
        }
        
        /* Result Container */
        .result-container {
            background: var(--card-bg);
            border: 2px solid var(--border-color);
            border-radius: 15px;
            padding: 2.5rem;
            margin-top: 2rem;
            animation: slideUp 0.5s ease;
            box-shadow: 0 20px 50px -12px rgba(0, 0, 0, 0.4);
        }
        
        .result-positive {
            border-color: var(--success-color);
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
        }
        
        .result-negative {
            border-color: var(--danger-color);
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
        }
        
        .result-neutral {
            border-color: var(--warning-color);
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
        }
        
        .result-title {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .result-message {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #cbd5e1;
        }
        
        .result-emoji {
            font-size: 4rem;
            display: block;
            margin-bottom: 1rem;
        }
        
        /* Sidebar */
        .sidebar-content {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 15px;
            padding: 1.5rem;
            margin-top: 2rem;
        }
        
        .sidebar-title {
            color: #cbd5e1;
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .sidebar-text {
            color: #94a3b8;
            line-height: 1.6;
            font-size: 0.95rem;
        }
        
        /* Column Layout */
        .col-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        @media (max-width: 768px) {
            .col-container {
                grid-template-columns: 1fr;
            }
        }
        
        /* Animations */
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        /* Streamlit overrides */
        .stNumberInput > div > div > input {
            background-color: #0f172a !important;
            color: #e2e8f0 !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
        }
        
        .stSelectbox > div > div > select {
            background-color: #0f172a !important;
            color: #e2e8f0 !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
        }
        
        .stButton > button {
            background: var(--primary-gradient) !important;
            color: white !important;
            padding: 0.75rem 2rem !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
            border: none !important;
            width: 100% !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 15px 40px -5px rgba(102, 126, 234, 0.4) !important;
        }
        
        /* Success/Error/Info Messages */
        .stSuccess, .stError, .stInfo {
            border-radius: 12px !important;
            border-left: 4px solid !important;
        }
        
        .stSuccess {
            background-color: rgba(16, 185, 129, 0.1) !important;
            border-left-color: var(--success-color) !important;
        }
        
        .stError {
            background-color: rgba(239, 68, 68, 0.1) !important;
            border-left-color: var(--danger-color) !important;
        }
        
        .stInfo {
            background-color: rgba(245, 158, 11, 0.1) !important;
            border-left-color: var(--warning-color) !important;
        }
        
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            animation: fadeIn 0.6s ease;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            color: #667eea;
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            font-size: 0.85rem;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
        }
        
        /* Divider */
        .divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border-color), transparent);
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

# ----------------------------
# Load model + preprocessor
# ----------------------------
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        data = pickle.load(f)
    return data

data = load_model()
model = data["model"]
preprocessor = data["preprocessor"]

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Social Media Impact Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()

# ----------------------------
# Header
# ----------------------------
st.markdown("""
<div class="main-header">
    <h1>📱 Social Media Impact Predictor</h1>
    <p>Advanced Analytics for Student Digital Wellness</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Main Content
# ----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="section-header">📋 Student Profile</div>', unsafe_allow_html=True)
    
    # Personal Information Section
    st.markdown("""
    <div class="input-container">
        <div style="font-size: 1.4rem; font-weight: 800; color: #e2e8f0; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 2px solid #667eea;">
            👤 Personal Information
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_1a, col_1b = st.columns(2)
    with col_1a:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">📅 AGE</span>', unsafe_allow_html=True)
        age = st.number_input("Age", min_value=10, max_value=60, value=20, key="age", label_visibility="collapsed")
    with col_1b:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">👥 GENDER</span>', unsafe_allow_html=True)
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender", label_visibility="collapsed")
    
    # Usage & Health Section
    st.markdown("""
    <div style="margin-top: 2rem;"></div>
    <div class="input-container">
        <div style="font-size: 1.4rem; font-weight: 800; color: #e2e8f0; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 2px solid #f093fb;">
            ⏱️ Digital Usage & Wellness
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_2a, col_2b = st.columns(2)
    with col_2a:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">📱 DAILY SCREEN TIME</span>', unsafe_allow_html=True)
        usage = st.number_input("Avg Daily Usage (hours)", min_value=0.0, max_value=24.0, value=3.0, step=0.5, key="usage", label_visibility="collapsed")
    with col_2b:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">😴 SLEEP QUALITY</span>', unsafe_allow_html=True)
        sleep = st.number_input("Sleep Hours Per Night", min_value=0.0, max_value=12.0, value=7.0, step=0.5, key="sleep", label_visibility="collapsed")
    
    st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem; margin-top: 1rem;">🧠 MENTAL HEALTH SCORE</span>', unsafe_allow_html=True)
    mental = st.slider(
        "Mental Health Score",
        min_value=1,
        max_value=10,
        value=5,
        help="Rate your overall mental health from 1 (Poor) to 10 (Excellent)",
        label_visibility="collapsed"
    )
    
    # Academic & Platform Section
    st.markdown("""
    <div style="margin-top: 2rem;"></div>
    <div class="input-container">
        <div style="font-size: 1.4rem; font-weight: 800; color: #e2e8f0; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 2px solid #764ba2;">
            🎓 Academic & Platform Info
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_3a, col_3b = st.columns(2)
    with col_3a:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">📚 EDUCATION LEVEL</span>', unsafe_allow_html=True)
        academic_level = st.selectbox(
            "Academic Level",
            ["High School", "Undergraduate", "Graduate"],
            key="academic_level",
            label_visibility="collapsed"
        )
    with col_3b:
        st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem;">📊 ACADEMICS AFFECTED</span>', unsafe_allow_html=True)
        academic_effect = st.selectbox(
            "Affects Academic Performance?",
            ["Yes", "No"],
            key="academic_effect",
            label_visibility="collapsed"
        )
    
    st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem; margin-top: 1rem;">📲 PRIMARY SOCIAL PLATFORM</span>', unsafe_allow_html=True)
    platform = st.selectbox(
        "Most Used Platform",
        [
            "Facebook", "LinkedIn", "Instagram", "Snapchat",
            "Twitter", "YouTube", "TikTok", "LINE",
            "KakaoTalk", "VKontakte", "WhatsApp", "WeChat"
        ],
        key="platform",
        label_visibility="collapsed"
    )
    
    st.markdown('<span style="font-size: 1.05rem; font-weight: 700; color: #cbd5e1; display: block; margin-bottom: 0.5rem; margin-top: 1rem;">🌍 COUNTRY / REGION</span>', unsafe_allow_html=True)
    country_list = [
        'India','USA','UK','Canada','Australia','Germany','France','Spain','Italy','China',
        'Japan','Brazil','Russia','South Korea','Mexico','Netherlands','Sweden','Norway',
        'Denmark','Finland','Singapore','Malaysia','Thailand','Indonesia','Philippines',
        'Pakistan','Bangladesh','Sri Lanka','Nepal','UAE','Saudi Arabia','South Africa','Other'
    ]
    country = st.selectbox("Country", country_list, key="country", label_visibility="collapsed")

with col2:
    st.markdown('<div class="section-header">📊 Quick Stats</div>', unsafe_allow_html=True)
    
    # Display metric cards
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{age}</div>
        <div class="metric-label">Years Old</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{usage:.1f}</div>
        <div class="metric-label">Daily Hours</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{sleep:.1f}</div>
        <div class="metric-label">Sleep Hours</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{mental}/10</div>
        <div class="metric-label">Mental Health</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Prediction Button
# ----------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 1, 1])
with predict_col2:
    predict_button = st.button("🔮 PREDICT IMPACT", use_container_width=True)

# ----------------------------
# Prediction Logic
# ----------------------------
if predict_button:
    input_dict = {
        "Age": age,
        "Avg_Daily_Usage_Hours": usage,
        "Sleep_Hours_Per_Night": sleep,
        "Mental_Health_Score": mental,
        "Gender": gender,
        "Academic_Level": academic_level,
        "Country": country,
        "Most_Used_Platform": platform,
        "Affects_Academic_Performance": academic_effect
    }
    input_df = pd.DataFrame([input_dict])
    
    try:
        processed_input = preprocessor.transform(input_df)
        prediction = model.predict(processed_input)
        result = prediction[0]
        
        # Display result with styling
        if result == "Positive":
            st.markdown(f"""
            <div class="result-container result-positive">
                <span class="result-emoji">😊</span>
                <div class="result-title">Positive Impact</div>
                <div class="result-message">
                    ✨ Social media is benefiting this student's life. The usage patterns suggest positive 
                    engagement with online communities, maintaining healthy sleep habits, and good mental wellness.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        elif result == "Negative":
            st.markdown(f"""
            <div class="result-container result-negative">
                <span class="result-emoji">⚠️</span>
                <div class="result-title">Negative Impact</div>
                <div class="result-message">
                    🚨 Social media may be negatively affecting this student. Consider reviewing daily usage patterns, 
                    sleep schedules, and mental health support. Balance is key to digital wellness.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        else:  # Neutral
            st.markdown(f"""
            <div class="result-container result-neutral">
                <span class="result-emoji">😐</span>
                <div class="result-title">Neutral Impact</div>
                <div class="result-message">
                    ⚖️ Social media has a balanced effect on this student. The current usage patterns 
                    indicate moderate influence on daily life with both benefits and challenges.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Additional insights
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">💡 Recommendations</div>', unsafe_allow_html=True)
        
        col_rec1, col_rec2, col_rec3 = st.columns(3)
        
        with col_rec1:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📱</div>
                <div class="metric-label">Screen Time</div>
                <div style="color: #e2e8f0; margin-top: 0.5rem; font-size: 0.9rem;">
                    Keep daily usage under 4 hours
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_rec2:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">😴</div>
                <div class="metric-label">Sleep Quality</div>
                <div style="color: #e2e8f0; margin-top: 0.5rem; font-size: 0.9rem;">
                    Maintain 7-9 hours daily
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_rec3:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🧠</div>
                <div class="metric-label">Mental Health</div>
                <div style="color: #e2e8f0; margin-top: 0.5rem; font-size: 0.9rem;">
                    Regular check-ins & balance
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.markdown(f"""
        <div class="result-container result-negative">
            <span class="result-emoji">❌</span>
            <div class="result-title">Error</div>
            <div class="result-message">
                {str(e)}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.markdown("""
<div class="sidebar-content">
    <div class="sidebar-title">ℹ️ About This App</div>
    <div class="sidebar-text">
        This advanced analytics tool predicts whether social media has a Positive, Negative, or Neutral 
        impact on students' lives based on their digital habits and wellness metrics.
        <br><br>
        <strong>Key Factors Analyzed:</strong>
        <ul style="margin: 1rem 0;">
            <li>Daily usage patterns</li>
            <li>Sleep quality</li>
            <li>Mental health indicators</li>
            <li>Academic performance</li>
            <li>Platform preferences</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-content" style="margin-top: 1.5rem;">
    <div class="sidebar-title">🎯 Tips for Digital Wellness</div>
    <div class="sidebar-text">
        <strong>✓ Do:</strong>
        <ul style="margin: 0.5rem 0;">
            <li>Take regular breaks</li>
            <li>Maintain healthy sleep</li>
            <li>Track screen time</li>
        </ul>
        <strong>✗ Avoid:</strong>
        <ul style="margin: 0.5rem 0;">
            <li>Late-night scrolling</li>
            <li>Excessive multitasking</li>
            <li>Social comparison</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("""
<div style="
    text-align: center;
    color: #64748b;
    font-size: 0.85rem;
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid #334155;
">
    <p>💻 Social Media Impact Predictor </p>
    
</div>
""", unsafe_allow_html=True)