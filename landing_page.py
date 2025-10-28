import streamlit as st

# === Konfigurasi dasar halaman ===
st.set_page_config(page_title="Nirwandha Links", page_icon="✨", layout="centered")

# === CSS Kustom untuk tampilan modern ===
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .main {
        text-align: center;
    }
    .profile-pic {
        width: 130px;
        height: 130px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #00FFB3;
        margin-bottom: 10px;
        box-shadow: 0 0 15px rgba(0,255,179,0.4);
    }
    h1 {
        font-weight: 600;
        margin-bottom: 0;
    }
    .bio {
        font-size: 15px;
        color: #dcdcdc;
        margin-bottom: 30px;
    }
    .link-card {
        background-color: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 14px;
        margin: 10px auto;
        width: 80%;
        max-width: 400px;
        transition: all 0.3s ease-in-out;
        text-align: center;
    }
    .link-card:hover {
        transform: translateY(-3px);
        background-color: rgba(255,255,255,0.15);
        box-shadow: 0 0 15px rgba(0,255,179,0.3);
    }
    a {
        text-decoration: none;
        color: #00FFB3;
        font-weight: 500;
        font-size: 17px;
    }
    footer {
        margin-top: 40px;
        font-size: 13px;
        color: #bbb;
    }
    </style>
""", unsafe_allow_html=True)

# === Konten utama ===
st.markdown("""
    <div class="main">
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic" alt="Profile Picture">
        <h1>Muhammad Nirwandha</h1>
        <p class="bio">🚢 Smart Port & AI Developer | Data Storyteller | Automation Enthusiast</p>
    </div>
""", unsafe_allow_html=True)

# === Kartu Tautan ===
links = [
    ("💼 LinkedIn", "https://linkedin.com/in/username"),
    ("🐙 GitHub", "https://github.com/username"),
    ("📸 Instagram", "https://instagram.com/username"),
    ("📧 Email", "mailto:youremail@example.com"),
    ("🌐 Portfolio", "https://your-portfolio.com"),
]

for text, url in links:
    st.markdown(f"""
        <div class="link-card">
            <a href="{url}" target="_blank">{text}</a>
        </div>
    """, unsafe_allow_html=True)

# === Footer ===
st.markdown("""
    <footer>
        Made with ❤️ using <b>Streamlit</b><br>
        © 2025 Nirwandha
    </footer>
""", unsafe_allow_html=True)
