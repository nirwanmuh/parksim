import streamlit as st

st.set_page_config(page_title="Nirwandha | Links", page_icon="🌿", layout="centered")

# === CSS FIXED DARK/LIGHT MODE ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
    }

    /* === MODE TERANG === */
    @media (prefers-color-scheme: light) {
        body {
            background-color: #fafafa;
            color: #1a1a1a;
        }
        .link-card {
            background: #ffffff;
            color: #1a1a1a;
            border: 1px solid #e5e5e5;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .link-card:hover {
            background: #f7f7f7;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
        }
        .bio { color: #555; }
        footer { color: #888; }
    }

    /* === MODE GELAP === */
    @media (prefers-color-scheme: dark) {
        body {
            background-color: #0d0d0d;
            color: #f5f5f5;
        }
        .link-card {
            background: #1a1a1a;
            color: #f5f5f5;
            border: 1px solid #2a2a2a;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        .link-card:hover {
            background: #222;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        .bio { color: #aaa; }
        footer { color: #777; }
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
        border: 1px solid rgba(255,255,255,0.1);
        opacity: 0;
        animation: fadeIn 1s forwards;
    }
    h1 {
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 5px;
        opacity: 0;
        animation: fadeUp 1s forwards;
    }
    .bio {
        font-size: 15px;
        margin-bottom: 25px;
        opacity: 0;
        animation: fadeUp 1.4s forwards;
    }
    .link-card {
        border-radius: 12px;
        padding: 14px;
        margin: 10px auto;
        width: 85%;
        max-width: 420px;
        text-align: center;
        transition: all 0.25s ease;
        opacity: 0;
        animation: fadeUp 1.6s forwards;
    }
    a {
        text-decoration: none;
        color: inherit;
        font-weight: 500;
        font-size: 16px;
        letter-spacing: 0.2px;
    }
    footer {
        margin-top: 60px;
        font-size: 13px;
        padding-bottom: 3rem;
        opacity: 0;
        animation: fadeIn 2s forwards;
    }

    /* === Animasi === */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# === Konten utama ===
st.markdown("""
    <div class="main">
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic" alt="Profile Picture">
        <h1>Muhammad Nirwandha</h1>
        <p class="bio">Data & AI Enthusiast · Smart Port Innovator · Automation Visionary</p>
    </div>
""", unsafe_allow_html=True)

# === Daftar tautan ===
links = [
    ("💼 LinkedIn", "https://linkedin.com/in/username"),
    ("🐙 GitHub", "https://github.com/username"),
    ("🌐 Portfolio", "https://your-portfolio.com"),
    ("📸 Instagram", "https://instagram.com/username"),
    ("✉️ Email", "mailto:youremail@example.com"),
]

for text, url in links:
    st.markdown(f"""
        <div class="link-card">
            <a href="{url}" target="_blank">{text}</a>
        </div>
    """, unsafe_allow_html=True)

# === Footer ===
st.markdown("""
    <footer style="text-align:center;">
        © 2025 — Designed with simplicity<br>
        Built with ❤️ using <b>Streamlit</b>
    </footer>
""", unsafe_allow_html=True)
