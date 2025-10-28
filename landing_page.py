import streamlit as st
import pandas as pd
import datetime
import uuid
import os

# === Konfigurasi dasar ===
st.set_page_config(page_title="Nirwandha Links", page_icon="✨", layout="centered")

# === Buat file log kalau belum ada ===
LOG_FILE = "access_log.csv"
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=["session_id", "timestamp", "event", "link", "ip_address", "user_agent"])
    df.to_csv(LOG_FILE, index=False)

# === Fungsi untuk mencatat log ===
def log_event(event, link=None):
    try:
        ip = st.session_state.get("ip_address", "unknown")
        ua = st.session_state.get("user_agent", "unknown")

        log_data = {
            "session_id": st.session_state.session_id,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event": event,
            "link": link or "",
            "ip_address": ip,
            "user_agent": ua,
        }

        df = pd.DataFrame([log_data])
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    except Exception as e:
        st.error(f"Gagal mencatat log: {e}")

# === Buat session unik untuk tiap pengunjung ===
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.ip_address = st.experimental_get_query_params().get("ip", ["unknown"])[0]
    st.session_state.user_agent = st.experimental_get_query_params().get("ua", ["unknown"])[0]
    log_event("page_visit")

# === CSS minimal modern ===
st.markdown("""
<style>
body {
    background-color: #0f1117;
    color: #e6e6e6;
    font-family: 'Poppins', sans-serif;
}
.main { text-align: center; }
.profile-pic {
    width: 120px; height: 120px;
    border-radius: 50%;
    border: 2px solid #444;
    margin-bottom: 10px;
}
h1 { font-weight: 600; }
.link-button {
    display: block;
    width: 80%;
    max-width: 380px;
    background: #1e1e1e;
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    padding: 12px;
    margin: 10px auto;
    color: #00e0a7;
    text-decoration: none;
    transition: all 0.2s ease;
}
.link-button:hover {
    background: #00e0a7;
    color: black;
}
footer {
    margin-top: 30px;
    font-size: 12px;
    color: #777;
}
</style>
""", unsafe_allow_html=True)

# === Konten utama ===
st.markdown("""
<div class="main">
    <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic">
    <h1>Muhammad Nirwandha</h1>
    <p>🚢 Smart Port & AI Developer | Data Storyteller | Automation Enthusiast</p>
</div>
""", unsafe_allow_html=True)

# === Link interaktif dengan logging ===
links = {
    "💼 LinkedIn": "https://linkedin.com/in/username",
    "🐙 GitHub": "https://github.com/username",
    "🌐 Portfolio": "https://your-portfolio.com",
    "📧 Email": "mailto:youremail@example.com",
}

for name, url in links.items():
    if st.button(name, key=url):
        log_event("link_click", link=name)
        st.markdown(f"<meta http-equiv='refresh' content='0; url={url}'>", unsafe_allow_html=True)

# === Footer ===
st.markdown("""
<footer>Made with ❤️ using Streamlit</footer>
""", unsafe_allow_html=True)
