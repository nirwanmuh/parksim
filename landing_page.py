import streamlit as st

# === Konfigurasi dasar halaman ===
st.set_page_config(page_title="Nirwandha | Links", page_icon="🌿", layout="centered")

# === CSS gaya minimalis modern ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    body {
        background-color: #fafafa;
        font-family: 'Inter', sans-serif;
        color: #222;
    }
    .main {
        text-align: center;
        padding-top: 3rem;
    }
    .profile-pic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
        border: 1px solid #ddd;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    h1 {
        font-weight: 600;
        margin-bottom: 5px;
    }
    .bio {
        color: #555;
        font-size: 15px;
        margin-bottom: 30px;
    }
    .link-card {
        background: white;
        border-radius: 10px;
        padding: 14px 0;
        margin: 10px auto;
        width: 85%;
        max-width: 420px;
        border: 1px solid #eee;
        transition: all 0.25s ease;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .link-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    a {
        text-decoration: none;
        color: #222;
        font-weight: 500;
        font-size: 16px;
        letter-spacing: 0.2px;
    }
    footer {
        margin-top: 60px;
        color: #888;
        font-size: 13px;
        padding-bottom: 2rem;
    }
    .social-icon {
        font-size: 20px;
        margin: 0 8px;
        color: #444;
        text-decoration: none;
    }
    .social-icon:hover {
        color: #111;
    }
    </style>
""", unsafe_allow_html=True)

# === Konten utama ===
st.markdown("""
    <div class="main">
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic" alt="Profile Picture">
        <h1>Muhammad Nirwandha</h1>
        <p class="bio">Data & AI Enthusiast | Smart Port Innovator | Problem Solver</p>
    </div>
""", unsafe_allow_html=True)

# === Daftar tautan ===
links = [
    ("LinkedIn →", "https://linkedin.com/in/username"),
    ("GitHub →", "https://github.com/username"),
    ("Portfolio →", "https://your-portfolio.com"),
    ("Instagram →", "https://instagram.com/username"),
    ("Email →", "mailto:youremail@example.com"),
]

for text, url in links:
    st.markdown(f"""
        <div class="link-card">
            <a href="{url}" target="_blank">{text}</a>
        </div>
    """, unsafe_allow_html=True)

# === Ikon sosial kecil ===
st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <a class="social-icon" href="https://linkedin.com/in/username">💼</a>
        <a class="social-icon" href="https://github.com/username">🐙</a>
        <a class="social-icon" href="https://instagram.com/username">📸</a>
    </div>
""", unsafe_allow_html=True)

# === Footer ===
st.markdown("""
    <footer>
        © 2025 — Designed with simplicity<br>
        Built using <b>Streamlit</b>
    </footer>
""", unsafe_allow_html=True)
