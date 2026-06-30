import streamlit as st
import pandas as pd
import pickle
import streamlit.components.v1 as components
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Smoking AI Command Center",
    page_icon="🚬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODEL
# =========================
model = pickle.load(
    open("random_forest_streamlit.pkl", "rb")
)

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# CSS
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Orbitron',sans-serif;
}

.stApp{
    background:
    linear-gradient(
    180deg,
    #08111f,
    #0b1629,
    #08111f
    );
    color:#e2e8f0;
}

/* HERO */
.hero{
    background:
    rgba(17,24,39,0.65);

    backdrop-filter:
    blur(20px);

    border:
    1px solid rgba(59,130,246,0.3);

    padding:40px;
    border-radius:30px;

    box-shadow:
    0 0 30px rgba(59,130,246,0.15);

    text-align:center;
}

.hero h1{
    color:#60a5fa;
}

/* CARD */
.card{
    background:
    rgba(17,24,39,0.65);

    backdrop-filter:
    blur(20px);

    border:
    1px solid rgba(59,130,246,0.2);

    padding:25px;
    border-radius:25px;

    box-shadow:
    0 0 20px rgba(59,130,246,0.12);

    transition:0.4s;
}

.card:hover{
    transform:
    translateY(-8px);
}

.metric{
    background:
    rgba(17,24,39,0.65);

    padding:25px;

    border-radius:25px;

    text-align:center;
}

.metric h1{
    color:#60a5fa;
}

/* RESULT */
.smoker{
    background:
    linear-gradient(
    180deg,
    #220909,
    #3b0d0d
    );

    border:
    1px solid rgba(239,68,68,0.4);

    box-shadow:
    0 0 25px rgba(239,68,68,0.25);

    padding:35px;
    border-radius:25px;
    text-align:center;
}

.nonsmoker{
    background:
    linear-gradient(
    180deg,
    #0c1d38,
    #102544
    );

    border:
    1px solid rgba(96,165,250,0.4);

    box-shadow:
    0 0 25px rgba(96,165,250,0.25);

    padding:35px;
    border-radius:25px;
    text-align:center;
}

.fire{
    font-size:50px;
    animation:
    fire 1s infinite alternate;
}

@keyframes fire{
    from{
        transform:translateY(0px);
    }
    to{
        transform:translateY(-10px);
    }
}

.smoke{
    font-size:60px;
    animation:
    smoke 3s infinite;
}

@keyframes smoke{
    0%{
        opacity:0;
        transform:translateY(20px);
    }

    100%{
        opacity:1;
        transform:translateY(-30px);
    }
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class='hero'>

<h1>
🚬 SMOKING AI COMMAND CENTER
</h1>

<p>
Prediksi Status Merokok Berdasarkan Data Kesehatan
Menggunakan Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🚬 Smoking AI")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "🤖 Prediksi",
        "📋 Riwayat",
        "ℹ️ Tentang"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("""
Model Terbaik

✅ Random Forest
Accuracy : 82.99%
""")

st.sidebar.write(
    f"🕒 {datetime.now().strftime('%d-%m-%Y %H:%M')}"
)

# =========================
# METRIC
# =========================
c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric'>
    <h1>82.99%</h1>
    Accuracy
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric'>
    <h1>77.27%</h1>
    F1 Score
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric'>
    <h1>91.54%</h1>
    ROC AUC
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================
# HOME
# =========================
if menu == "🏠 Home":

    st.markdown("""
    <div class='card'>

    <h2>Selamat Datang 👋</h2>

    Sistem ini digunakan untuk memprediksi
    status merokok berdasarkan data kesehatan.

    Silakan pilih menu Prediksi.

    </div>
    """, unsafe_allow_html=True)

# =========================
# PREDIKSI
# =========================
elif menu == "🤖 Prediksi":

    col1,col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Jenis Kelamin",
            ["Laki-laki","Perempuan"]
        )

        height = st.number_input(
            "Tinggi Badan (cm)",
            100,250,170
        )

        waist = st.number_input(
            "Lingkar Pinggang (cm)",
            40,200,80
        )

        hemoglobin = st.number_input(
            "Hemoglobin",
            0.0,30.0,14.0
        )

        triglyceride = st.number_input(
            "Triglyceride",
            0,1000,120
        )

    with col2:

        gtp = st.number_input(
            "GTP",
            0,1000,30
        )

        ldl = st.number_input(
            "LDL",
            0,500,100
        )

        cholesterol = st.number_input(
            "Cholesterol",
            0,500,180
        )

        alt = st.number_input(
            "ALT",
            0,1000,25
        )

        hdl = st.number_input(
            "HDL",
            0,500,50
        )

    if st.button("🚀 Prediksi"):

        gender_num = (
            1 if gender == "Laki-laki"
            else 0
        )

        input_data = pd.DataFrame({
            'gender':[gender_num],
            'Gtp':[gtp],
            'hemoglobin':[hemoglobin],
            'height(cm)':[height],
            'triglyceride':[triglyceride],
            'waist(cm)':[waist],
            'LDL':[ldl],
            'Cholesterol':[cholesterol],
            'ALT':[alt],
            'HDL':[hdl]
        })

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0]

        persen = int(
            probability[1]*100
        )

        status = (
            "PEROKOK"
            if prediction == 1
            else
            "TIDAK MEROKOK"
        )

        st.session_state.history.append({
            "Waktu":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            ),
            "Status":
            status,
            "Probabilitas":
            persen
        })

        if prediction == 1:

            st.markdown("""
            <div class='smoker'>

            <div class='smoke'>
            💨
            </div>

            <h1 style='color:#ef4444'>
            🚬 PEROKOK
            </h1>

            <div class='fire'>
            🔥🔥🔥
            </div>

            </div>
            """,
            unsafe_allow_html=True)

        else:

            st.snow()
            st.balloons()

            st.markdown("""
            <div class='nonsmoker'>

            <h1 style='color:#60a5fa'>
            ❄️ TIDAK MEROKOK ❄️
            </h1>

            <h2>
            ☃️ ❄️ ☃️
            </h2>

            </div>
            """,
            unsafe_allow_html=True)

        st.write("")

        components.html(
        f"""
        <div style="
        width:250px;
        height:250px;
        border-radius:50%;
        background:
        conic-gradient(
        #ef4444 {persen}%,
        #1e293b {persen}%);

        display:flex;
        justify-content:center;
        align-items:center;

        margin:auto;

        font-size:45px;
        font-weight:bold;

        color:white;

        box-shadow:
        0 0 30px rgba(59,130,246,0.4);
        ">

        {persen}%

        </div>
        """,
        height=300
        )

        st.progress(
            persen
        )

        if persen >= 70:
            st.error(
                "Risiko Tinggi"
            )
        elif persen >= 40:
            st.warning(
                "Risiko Sedang"
            )
        else:
            st.success(
                "Risiko Rendah"
            )

        st.subheader(
            "Data Input"
        )

        st.dataframe(
            input_data,
            use_container_width=True
        )

# =========================
# HISTORY
# =========================
elif menu == "📋 Riwayat":

    st.subheader(
        "Riwayat Prediksi"
    )

    if len(
        st.session_state.history
    ) == 0:

        st.info(
            "Belum ada prediksi."
        )

    else:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            history_df,
            use_container_width=True
        )

        csv = history_df.to_csv(
            index=False
        )

        st.download_button(
            "📥 Download CSV",
            csv,
            "history.csv",
            "text/csv"
        )

# =========================
# ABOUT
# =========================
else:

    st.markdown("""
    <div class='card'>

    <h2>Tentang Aplikasi</h2>

    Aplikasi ini dibangun menggunakan
    algoritma Random Forest untuk
    klasifikasi status merokok
    berdasarkan data kesehatan.

    <br><br>

    Developer :
    Nama Anda

    </div>
    """, unsafe_allow_html=True)