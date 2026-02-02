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
    .subject-card {
        background-color: #ffffff;
        padding: 30px;
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

# 顯示 Q 版師生圖
try:
    img = Image.open("data/portal_bg.jpg")
    st.image(img, use_column_width=True)
except:
    st.error("📸 數據溢位：找不到 data/portal_bg.jpg，請檢查資料夾路徑。")

# --- 3. 指揮官寄語 ---
st.markdown(f"""
### 📣 首席工程師（老師）的戰前叮嚀：
各位同學，最後 30 天不是要你們去死背，是要你們學會掌控規則。
理化的莫耳數公式 $$n = \\frac{{m}}{{M}}$$ 就像手搖飲的珍珠，只要掌握質量與分子量的關係，
考卷上的難題就會像去冰微糖一樣好吞！
""")

st.divider()

# --- 4. 三大科入口選單 (時空門) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## ⚛️ 理化")
    st.markdown("#### 【珍珠莫耳實驗室】")
    st.write("精準掌控每一顆原子的質量。")
    st.link_button("🔥 啟動理化實驗室", "https://science-ai-lab-bbbvhmgpodx4qssgdhpxoi.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## 🧬 生物")
    st.markdown("#### 【生命真理研究室】")
    st.write("從顯微鏡解讀生存的禁忌。")
    st.link_button("🍀 啟動生命研究室", "https://aibiologylab-ws7gxsja64fym3fpvq5lpu.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    st.markdown("## 🪐 地科")
    st.markdown("#### 【星艦導航指揮室】")
    st.write("跟隨馬斯克衝向星辰大海。")
    st.link_button("🚀 啟動星艦導航室", "https://aiearthsciencelab-yvpfgocxyuwgqfowtcvfpi.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 科學真理補完計畫 | 指揮官：資深理化老師與 AI 助教團")