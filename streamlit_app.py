import streamlit as st
import pandas as pd
from datetime import date

# ====== CSS LATAR HIJAU TUA ======
st.markdown(
    """
    <style>
    /* Warna latar utama */
    .stApp {
        background-color: #1b5e20;   /* hijau tua */
        color: white;                /* teks jadi putih */
    }

    /* Pastikan semua teks default ikut putih */
    h1,h2,h3,h4,h5,h6, p, label, span, div {
        color: white !important;
    }

    /* Kotak input & widget agar tidak silau */
    .css-1cpxqw2, .css-1d391kg, .css-1n76uvr, .stTextInput>div>div>input {
        background-color: #2e7d32 !important;  /* hijau sedikit lebih terang */
        color: white !important;
    }

    /* Sidebar dengan hijau lebih gelap agar kontras */
    section[data-testid="stSidebar"] {
        background-color: #145a17 !important;
    }
    </style>
    """,
    unsafe_allow_html=True

# ---------- Inisialisasi ----------
if "records" not in st.session_state:
    st.session_state.records = []          # list of dicts
if "page" not in st.session_state:
    st.session_state.page = "Menu"

# ---------- Sidebar Navigasi ----------
menu_items = ["Menu", "Cair", "Padat", "Gas",
              "Kebisingan", "B3", "Organik", "Non-Organik",
              "Data Keseluruhan"]

st.sidebar.title("Navigasi")
st.session_state.page = st.sidebar.radio("Pilih Halaman:", menu_items)

# ---------- Fungsi Simpan ----------
def simpan(data_dict):
    st.session_state.records.append(data_dict)
    st.success("✅ Data tersimpan!")

# ---------- Halaman: Menu Utama ----------
if st.session_state.page == "Menu":
    st.title("Sistem Pelaporan & Pengawasan Limbah Industri")
    st.write(
        """
        Pilih menu di sidebar untuk mulai mengisi pelaporan tiap jenis limbah.  
        Setelah mengisi, data akan muncul di **Data Keseluruhan**.
        """
    )

# ---------- Halaman: Cair ----------
elif st.session_state.page == "Cair":
    st.header("Pelaporan Limbah Cair")
    with st.form("form_cair"):
        tanggal = st.date_input("Tanggal", value=date.today())
        teknologi = st.text_input("Teknologi Pengolahan")
        proses = st.selectbox("Proses", ["Primer", "Sekunder", "Tersier"])
        kapasitas_ipal = st.number_input("Kapasitas IPAL (m³/hari)", min_value=0.0)
        debit = st.number_input("Debit Limbah Diolah", min_value=0.0)
        reagen = st.text_input("Reagen/Bahan Kimia")
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Cair", "Tanggal": tanggal, "Teknologi": teknologi,
            "Proses": proses, "Kapasitas": kapasitas_ipal,
            "Debit": debit, "Reagen": reagen
        })

# ---------- Halaman: Padat ----------
elif st.session_state.page == "Padat":
    st.header("Pelaporan Limbah Padat")
    with st.form("form_padat"):
        tanggal = st.date_input("Tanggal", value=date.today())
        jenis_padat = st.selectbox("Jenis Limbah Padat", ["B3", "Non B3"])
        cara = st.text_input("Cara Pengolahan")
        volume = st.number_input("Volume (kg/minggu)", min_value=0.0)
        lokasi = st.text_input("Lokasi Penyimpanan")
        metode = st.text_input("Metode Penyimpanan")
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Padat", "Tanggal": tanggal, "Jenis Padat": jenis_padat,
            "Cara": cara, "Volume": volume,
            "Lokasi": lokasi, "Metode": metode
        })

# ---------- Halaman: Gas ----------
elif st.session_state.page == "Gas":
    st.header("Pelaporan Limbah Gas")
    with st.form("form_gas"):
        tanggal = st.date_input("Tanggal", value=date.today())
        teknologi = st.text_input("Teknologi Pengendalian Emisi")
        jenis_gas = st.text_input("Jenis Gas")
        konsentrasi = st.number_input("Konsentrasi (mg/Nm³)", min_value=0.0)
        opasitas = st.number_input("Opasitas (%)", min_value=0.0, max_value=100.0)
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Gas", "Tanggal": tanggal, "Teknologi": teknologi,
            "Jenis Gas": jenis_gas, "Konsentrasi": konsentrasi, "Opasitas": opasitas
        })

# ---------- Halaman: Kebisingan ----------
elif st.session_state.page == "Kebisingan":
    st.header("Pelaporan Kebisingan")
    with st.form("form_noise"):
        tanggal = st.date_input("Tanggal", value=date.today())
        lokasi = st.text_input("Lokasi Pengukuran")
        tingkat_db = st.number_input("Tingkat Kebisingan (dB)", min_value=0.0)
        durasi = st.number_input("Durasi Pengukuran (menit)", min_value=0.0)
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Kebisingan", "Tanggal": tanggal,
            "Lokasi": lokasi, "dB": tingkat_db, "Durasi": durasi
        })

# ---------- Halaman: B3 ----------
elif st.session_state.page == "B3":
    st.header("Pelaporan Limbah B3")
    with st.form("form_b3"):
        tanggal = st.date_input("Tanggal", value=date.today())
        kode_b3 = st.text_input("Kode B3")
        volume = st.number_input("Volume (kg)", min_value=0.0)
        penyimpanan = st.text_input("Metode Penyimpanan")
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "B3", "Tanggal": tanggal,
            "Kode B3": kode_b3, "Volume": volume,
            "Penyimpanan": penyimpanan
        })

# ---------- Halaman: Organik ----------
elif st.session_state.page == "Organik":
    st.header("Pelaporan Limbah Organik")
    with st.form("form_org"):
        tanggal = st.date_input("Tanggal", value=date.today())
        sumber = st.text_input("Sumber Limbah")
        berat = st.number_input("Berat (kg)", min_value=0.0)
        metode = st.text_input("Metode Pengolahan")
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Organik", "Tanggal": tanggal,
            "Sumber": sumber, "Berat": berat, "Metode": metode
        })

# ---------- Halaman: Non-Organik ----------
elif st.session_state.page == "Non-Organik":
    st.header("Pelaporan Limbah Non-Organik")
    with st.form("form_nonorg"):
        tanggal = st.date_input("Tanggal", value=date.today())
        kategori = st.text_input("Kategori Limbah")
        berat = st.number_input("Berat (kg)", min_value=0.0)
        metode = st.text_input("Metode Pengolahan")
        submitted = st.form_submit_button("Simpan")
    if submitted:
        simpan({
            "Jenis": "Non-Organik", "Tanggal": tanggal,
            "Kategori": kategori, "Berat": berat, "Metode": metode
        })

# ---------- Halaman: Data Keseluruhan ----------
elif st.session_state.page == "Data Keseluruhan":
    st.header("Tabel Keseluruhan Data Pelaporan")
    if st.session_state.records:
        df = pd.DataFrame(st.session_state.records)
        st.dataframe(df, use_container_width=True)
        st.download_button(
            label="⬇️ Unduh CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="pelaporan_limbah.csv",
            mime="text/csv"
        )
    else:
        st.info("Belum ada data tersimpan.")
