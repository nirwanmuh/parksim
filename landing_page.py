import streamlit as st

# === KONFIGURASI DASAR HALAMAN ===
st.set_page_config(page_title="Nirwandha | Links", page_icon="🌿", layout="centered")

# === CSS MODERN MINIMALIST ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        scroll-behavior: smooth;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* === MODE TERANG === */
    body[data-theme="light"], .main.light {
        background-color: #f9f9f9;
        color: #1a1a1a;
    }

    /* === MODE GELAP === */
    body[data-theme="dark"], .main.dark {
        background-color: #111;
        color: #f5f5f5;
    }

    .profile-pic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 1px solid rgba(0,0,0,0.05);
        box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        margin-top: 2rem;
        opacity: 0;
        animation: fadeIn 1s forwards;
    }

    h1 {
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 5px;
        opacity: 0;
        animation: fadeUp 1.2s forwards;
    }

    .bio {
        font-size: 15px;
        color: #666;
        margin-bottom: 25px;
        opacity: 0;
        animation: fadeUp 1.5s forwards;
    }

    .link-card {
        background: var(--card-bg, rgba(255,255,255,0.9));
        border-radius: 12px;
        padding: 14px;
        margin: 10px auto;
        width: 85%;
        max-width: 420px;
        border: 1px solid rgba(0,0,0,0.05);
        transition: all 0.25s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
        opacity: 0;
        animation: fadeUp 1.8s forwards;
    }

    .link-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }

    a {
        text-decoration: none;
        color: inherit;
        font-weight: 500;
        font-size: 16px;
        letter-spacing: 0.3px;
    }

    footer {
        margin-top: 50px;
        color: #999;
        font-size: 13px;
        padding-bottom: 3rem;
        opacity: 0;
        animation: fadeIn 2.2s forwards;
    }

    /* === ANIMASI HALUS === */
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

# === TAMPILAN UTAMA ===
st.markdown("""
    <div style="text-align:center;">
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic" alt="Profile Picture">
        <h1>Muhammad Nirwandha</h1>
        <p class="bio">Data & AI Enthusiast · Smart Port Innovator · Automation Visionary</p>
    </div>
""", unsafe_allow_html=True)

# === DAFTAR TAUTAN ===
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

# === FOOTER ===
st.markdown("""
    <footer style="text-align:center;">
        © 2025 — Designed with simplicity<br>
        Built with ❤️ using <b>Streamlit</b>
    </footer>
""", unsafe_allow_html=True)
