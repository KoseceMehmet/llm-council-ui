import streamlit as st

def apply_dorkforge_theme():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'JetBrains Mono', monospace, sans-serif;
        }

        .stApp {
            background-color: #0b0e14;
            color: #d1d5db;
        }

        .stSidebar {
            background-color: #111622;
            border-right: 1px solid #1f293d;
        }

        h1, h2, h3, .accent-text {
            color: #00e5ff !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        div[data-testid="stColumn"] {
            background-color: #151c28;
            border: 1px solid #222f43;
            border-radius: 4px;
            padding: 16px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }

        .stButton>button {
            background-color: #151c28;
            color: #00e5ff;
            border: 1px solid #00e5ff;
            border-radius: 2px;
            font-weight: 600;
            text-transform: uppercase;
            transition: all 0.2s ease;
        }

        .stButton>button:hover {
            background-color: #00e5ff;
            color: #0b0e14;
            box-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
        }

        .status-badge-success {
            color: #10b981;
            border: 1px solid #10b981;
            padding: 2px 8px;
            font-size: 0.75rem;
            border-radius: 2px;
        }

        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div {
            background-color: #0f141c;
            color: #e5e7eb;
            border: 1px solid #222f43;
            border-radius: 2px;
        }
    </style>
    """, unsafe_allow_html=True)
