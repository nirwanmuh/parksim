import streamlit as st
from PIL import Image

# === Konfigurasi Halaman ===
st.set_page_config(
    page_title="SmartPort - Intelligent Port Management",
    page_icon="🚢",
    layout="wide",
)

# === Styling CSS ===
st.markdown("""
    <style>
    body {
        background-color: #f9fafc;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-top: 1em;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #475569;
        margin-bottom: 2em;
    }
    .feature-card {
        padding: 2em;
        border-radius: 1rem;
        background: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 4em;
    }
    </style>
""", unsafe_allow_html=True)

# === Hero Section ===
col1, col2 = st.columns([1, 1.2])
with col1:
    st.markdown("<div class='main-title'>🚢 SmartPort</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Optimalkan manajemen pelabuhan dengan kecerdasan buatan</div>", unsafe_allow_html=True)
    st.markdown("""
    SmartPort membantu operator pelabuhan mengelola kendaraan, muatan, dan keseimbangan kapal secara otomatis 
    menggunakan teknologi **AI dan IoT**.
    """)
    st.markdown("✅ Optimasi muatan & keseimbangan kapal")
    st.markdown("✅ Analisis data pelabuhan real-time")
    st.markdown("✅ Integrasi dengan sensor IoT dan kamera AI")
    st.markdown("")

    if st.button("🚀 Coba Sekarang", use_container_width=True):
        st.switch_page("app.py")  # jika kamu punya halaman app terpisah
with col2:
    image = Image.open("pelabuhan.jpg") if "pelabuhan.jpg" else None
    st.image(image, caption="Sistem SmartPort", use_column_width=True)

st.markdown("---")

# === Features Section ===
st.subheader("✨ Fitur Utama")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='feature-card'>📊 <br><b>Dashboard Analitik</b><br><br> Pantau semua aktivitas kapal dan kendaraan secara real-time melalui dashboard interaktif.</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='feature-card'>⚙️ <br><b>AI Optimization</b><br><br> Sistem cerdas menghitung posisi muatan optimal untuk menjaga keseimbangan dan efisiensi.</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='feature-card'>🌐 <br><b>Integrasi IoT</b><br><br> Konektivitas dengan sensor, kamera, dan perangkat IoT untuk pemantauan otomatis.</div>", unsafe_allow_html=True)

st.markdown("---")

# === About Section ===
st.subheader("🧭 Tentang SmartPort")
st.markdown("""
SmartPort dikembangkan untuk mendukung digitalisasi pelabuhan dengan pendekatan **AI + IoT + Data Intelligence**.  
Dengan sistem ini, pengelola pelabuhan dapat:
- Mengoptimalkan penataan kendaraan dan muatan kapal.  
- Mengurangi waktu bongkar-muat.  
- Meningkatkan efisiensi operasional hingga 30%.  
- Mendapat insight berbasis data untuk pengambilan keputusan strategis.
""")

st.markdown("---")

# === Footer ===
st.markdown("<div class='footer'>© 2025 SmartPort AI — Dibangun dengan ❤️ dan Streamlit</div>", unsafe_allow_html=True)
