import streamlit as st

# === Konfigurasi halaman ===
st.set_page_config(
    page_title="My Linktree",
    page_icon="🌐",
    layout="centered"
)

# === Styling CSS ===
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
        text-align: center;
    }
    .profile-pic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin-bottom: 10px;
        border: 3px solid #4CAF50;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        height: 50px;
        margin-top: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# === Konten utama ===
st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", use_column_width=False, width=120)
st.title("Muhammad Nirwandha")
st.write("🚀 Data & AI Enthusiast | Passionate about Smart Ports and Automation")

st.write("---")

# === Tombol tautan ===
if st.button("💼 LinkedIn"):
    st.markdown("[Klik di sini](https://linkedin.com/in/username)", unsafe_allow_html=True)

if st.button("📸 Instagram"):
    st.markdown("[Klik di sini](https://instagram.com/username)", unsafe_allow_html=True)

if st.button("🐙 GitHub"):
    st.markdown("[Klik di sini](https://github.com/username)", unsafe_allow_html=True)

if st.button("✉️ Email"):
    st.markdown("[Klik di sini](mailto:youremail@example.com)", unsafe_allow_html=True)

st.write("---")
st.caption("Made with ❤️ using Streamlit")

