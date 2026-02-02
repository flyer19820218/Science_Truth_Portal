import streamlit as st
from PIL import Image

# --- 1. 頁面配置 (全黑翩翩體、專業指揮艙風格) ---
st.set_page_config(page_title="考前 30 天：科學真理指揮中心", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, span, label, li {
        color: #000000 !important;
        font-family: 'HanziPen SC', '翩翩體', 'KaiTi', sans-serif !important;
    }
    .main-title {
        font-size: 3.5rem !important;
        text-align: center;
        background: linear-gradient(45deg, #1A237E, #01579B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin-bottom: 20px;
    }
    /* 讓按鈕字體變大 */
    .stButton>button {
        font-size: 1.4rem !important;
        font-weight: bold !important;
        height: 3.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題與靈魂背景圖 ---
st.markdown('<h1 class="main-title">🚀 考前 30 天：科學真理指揮中心 🚀</h1>', unsafe_allow_html=True)

try:
    img = Image.open("data/portal_bg.jpg")
    st.image(img, use_column_width=True)
except:
    st.error("📸 數據溢位：找不到 data/portal_bg.jpg，請檢查 GitHub 檔案夾。")

st.divider()

# --- 3. 三大科真理容器 (使用 border=True 強制裝箱) ---
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### ⚛️ 理化")
        st.latex(r"n = \frac{m}{M}")
        st.write("**【珍珠莫耳定律】**")
        st.write("秤出總質量 $m$，除以單顆珍珠分子量 $M$，就是莫耳數 $n$！")
        st.link_button("🔥 進入理化實驗室", "https://science-ai-lab-bbbvhmgpodx4qssgdhpxoi.streamlit.app/")

with col2:
    with st.container(border=True):
        st.markdown("### 🧬 生物")
        st.latex(r"6CO_2 + 6H_2O \rightarrow C_6H_{12}O_6 + 6O_2")
        st.write("**【能量工廠】**")
        st.write("陽光、水與二氧化碳，就是植物調製能量飲的終極秘方！")
        st.link_button("🍀 進入生命研究室", "https://aibiologylab-ws7gxsja64fym3fpvq5lpu.streamlit.app/")

with col3:
    with st.container(border=True):
        st.markdown("### 🪐 地科")
        st.latex(r"E = 10^{4.8 + 1.5M}")
        st.write("**【板塊能量契約】**")
        st.write("地震規模 $M$ 增加 1，釋放能量 $E$ 可是暴增 32 倍的狂想！")
        st.link_button("🚀 進入星艦導航室", "https://aiearthsciencelab-yvpfgocxyuwgqfowtcvfpi.streamlit.app/")

st.divider()
st.info("💡 提醒：進站後請先備好 API 通行證，即可啟動 AI 助教進行圖文導讀。")