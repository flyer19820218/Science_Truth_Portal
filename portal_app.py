import streamlit as st
from PIL import Image

# --- 1. 頁面配置 (全黑翩翩體、全黑文字、專業指揮艙風格) ---
st.set_page_config(page_title="考前 30 天：科學真理指揮中心", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, span, label, li {
        color: #000000 !important;
        font-family: 'HanziPen SC', '翩翩體', 'KaiTi', sans-serif !important;
    }
    .subject-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        border: 4px solid #000000;
        text-align: center;
        transition: 0.3s;
        height: 100%;
    }
    .subject-card:hover {
        transform: translateY(-10px);
        background-color: #fffde7;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .formula-box {
        background-color: #f1f8e9;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
        border: 1px dashed #2e7d32;
    }
    .main-title {
        font-size: 3.5rem !important;
        text-align: center;
        background: linear-gradient(45deg, #1A237E, #01579B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題與靈魂背景圖 ---
st.markdown('<h1 class="main-title">🚀 考前 30 天：科學真理指揮中心 🚀</h1>', unsafe_allow_html=True)

try:
    img = Image.open("data/portal_bg.jpg")
    st.image(img, use_column_width=True)
except:
    st.error("📸 數據溢位：找不到 data/portal_bg.jpg，請檢查 GitHub 檔案路徑。")

st.divider()

# --- 3. 三大科入口選單 (真理啟示卡 + 精確網址對位) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## ⚛️ 理化")
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"n = \frac{m}{M}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("**【珍珠莫耳定律】**")
    st.write("想知道這杯珍奶有多少珍珠？秤出總質量 $m$，除以單顆珍珠的分子量 $M$ 就對了！")
    # --- 填入您的理化網址 ---
    st.link_button("🔥 啟動理化實驗室", "https://science-ai-lab-bbbvhmgpodx4qssgdhpxoi.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## 🧬 生物")
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"6CO_2 + 6H_2O \xrightarrow{光} C_6H_{12}O_6 + 6O_2")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("**【光合作用能量工廠】**")
    st.write("吸入二氧化碳，配上陽光，植物就能為你調製出一杯熱騰騰的葡萄糖能量飲！")
    # --- 填入您的生物網址 ---
    st.link_button("🍀 啟動生命研究室", "https://aibiologylab-ws7gxsja64fym3fpvq5lpu.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## 🪐 地科")
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"E = 10^{4.8 + 1.5M}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("**【板塊震盪能量契約】**")
    st.write("當板塊大口喝下能量，地震規模 $M$ 增加 1，釋放能量 $E$ 可是會暴增 32 倍！")
    # --- 填入您的地科網址 ---
    st.link_button("🚀 啟動星艦導航室", "https://aiearthsciencelab-yvpfgocxyuwgqfowtcvfpi.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("💡 提醒：進站後請先備好 API 通行證，即可啟動 AI 助教進行圖文導讀。")