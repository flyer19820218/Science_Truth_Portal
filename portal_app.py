import streamlit as st
from PIL import Image

# --- 1. 頁面配置 (全能適配版) ---
st.set_page_config(page_title="考前 30 天：科學真理指揮中心", layout="wide")

st.markdown("""
    <style>
    /* 全黑翩翩體鎖定 */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, span, label, li {
        color: #000000 !important;
        font-family: 'HanziPen SC', '翩翩體', 'KaiTi', sans-serif !important;
    }
    
    /* 標題自適應 */
    .main-title {
        font-size: calc(1.5rem + 2vw) !important;
        text-align: center;
        background: linear-gradient(45deg, #1A237E, #01579B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }

    /* 針對所有裝置的大按鈕設計 */
    .stButton>button {
        width: 100% !important;
        height: 3.8rem !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border: 3px solid #000000 !important;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #fffde7 !important;
        transform: scale(1.02);
    }

    /* 容器邊框強化 */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 3px solid #000000 !important;
        border-radius: 20px !important;
        background-color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題與靈魂背景圖 ---
st.markdown('<h1 class="main-title">🚀 考前 30 天：科學真理指揮中心 🚀</h1>', unsafe_allow_html=True)

try:
    img = Image.open("data/portal_bg.jpg")
    st.image(img, use_column_width=True)
except:
    st.error("📸 數據溢位：找不到 data/portal_bg.jpg，請檢查 GitHub 檔案夾路徑。")

st.divider()

# --- 3. 三大科容器 (在 iPad 上會自動橫排，在手機上會自動垂直堆疊) ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    with st.container(border=True):
        st.markdown("### ⚛️ 理化")
        st.latex(r"n = \frac{m}{M}")
        st.write("**【珍珠莫耳定律】**")
        st.write("秤出質量 $m$，除以分子量 $M$，就是莫耳數 $n$！掌握每一顆珍珠的份量。")
        st.link_button("🔥 進入理化實驗室", "https://science-ai-lab-bbbvhmgpodx4qssgdhpxoi.streamlit.app/")

with col2:
    with st.container(border=True):
        st.markdown("### 🧬 生物")
        st.latex(r"6CO_2 + 6H_2O \rightarrow C_6H_{12}O_6 + 6O_2")
        st.write("**【能量工廠】**")
        st.write("陽光、水與二氧化碳，就是植物調製能量飲的秘密！解開生命的代碼。")
        st.link_button("🍀 進入生命研究室", "https://aibiologylab-ws7gxsja64fym3fpvq5lpu.streamlit.app/")

with col3:
    with st.container(border=True):
        st.markdown("### 🪐 地科")
        st.latex(r"E = 10^{4.8 + 1.5M}")
        st.write("**【板塊能量契約】**")
        st.write("地震規模 $M$ 增加 1，釋放能量 $E$ 可是暴增 32 倍！跟著馬斯克看透地底。")
        st.link_button("🚀 進入星艦導航室", "https://aiearthsciencelab-yvpfgocxyuwgqfowtcvfpi.streamlit.app/")

st.divider()
st.caption("© 2026 科學真理補完計畫 | 指揮官：理化老師 & AI 助教團")