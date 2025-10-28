import streamlit as st

# === KONFIGURASI HALAMAN ===
st.set_page_config(page_title="Nirwandha Links", page_icon="⚡", layout="centered")

# === CSS FUTURISTIK ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Rajdhani:wght@400;600&display=swap');

    body {
        background: radial-gradient(circle at 10% 20%, #0f0f1b 0%, #080810 100%);
        color: #e0e0e0;
        font-family: 'Rajdhani', sans-serif;
    }
    .main {
        text-align: center;
        margin-top: 2rem;
    }
    .profile-pic {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 3px solid #00ffe0;
        box-shadow: 0 0 25px #00ffe0;
        margin-bottom: 15px;
        transition: transform 0.4s ease;
    }
    .profile-pic:hover {
        transform: scale(1.05);
    }
    h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: #00ffe0;
        text-shadow: 0 0 10px #00ffe0;
    }
    .bio {
        color: #a0a0a0;
        font-size: 15px;
        margin-bottom: 30px;
    }
    .link-card {
        backdrop-filter: blur(12px);
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 255, 224, 0.4);
        border-radius: 14px;
        padding: 14px;
        margin: 10px auto;
        width: 85%;
        max-width: 420px;
        transition: all 0.35s ease-in-out;
        box-shadow: 0 0 10px rgba(0, 255, 224, 0.15);
    }
    .link-card:hover {
        background: rgba(0, 255, 224, 0.15);
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 0 25px rgba(0, 255, 224, 0.4);
    }
    a {
        text-decoration: none;
        color: #00ffe0;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        font-size: 16px;
    }
    footer {
        margin-top: 50px;
        font-size: 12px;
        color: #888;
    }
    .glow {
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse {
        from { text-shadow: 0 0 5px #00ffe0; }
        to { text-shadow: 0 0 20px #00ffe0, 0 0 40px #00ffe0; }
    }
    </style>
""", unsafe_allow_html=True)

# === KONTEN HALAMAN ===
st.markdown("""
    <div class="main">
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic" alt="Profile Picture">
        <h1 class="glow">MUHAMMAD NIRWANDHA</h1>
        <p class="bio">🚀 AI Engineer | Smart Port Innovator | Automation Visionary</p>
    </div>
""", unsafe_allow_html=True)

# === TAUTAN ===
links = [
    ("💼 LinkedIn", "https://linkedin.com/in/username"),
    ("🐙 GitHub", "https://github.com/username"),
    ("📸 Instagram", "https://instagram.com/username"),
    ("🌐 Portfolio", "https://your-portfolio.com"),
    ("📫 Email", "mailto:youremail@example.com"),
]

for text, url in links:
    st.markdown(f"""
        <div class="link-card">
            <a href="{url}" target="_blank">{text}</a>
        </div>
    """, unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""
    <footer>
        ⚡ Designed in 2025 — <span style="color:#00ffe0;">Futuristic Linktree</span><br>
        Built with ❤️ using Streamlit
    </footer>
""", unsafe_allow_html=True)
