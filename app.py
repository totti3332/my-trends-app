import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 設定網頁標題與圖示
st.set_page_config(page_title="全球與台灣熱門話題輿情看板", page_icon="🔥", layout="wide")

st.title("🔥 全球與台灣熱門話題輿情看板")
st.subheader("免寫程式！即時掌握最新網路趨勢與爆發話題")
st.markdown(f"**資料更新時間：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 2. 模擬 Google Trends 實時數據 (因 pyTrends 偶有連線限制，先建立穩定資料結構)
# 註：此處為第一階段演示，後續部署時我們會對接即時 API 爬蟲
def get_google_trends():
    trends_data = {
        "排名": [1, 2, 3, 4, 5],
        "熱門關鍵字": ["黃仁勳 COMPUTEX", "端午節連假", "台灣地震", "蘋果 AI 功能", "Netflix 新劇"],
        "今日搜尋量": ["10萬+", "5萬+", "5萬+", "2萬+", "2萬+"],
        "相關新聞標題": [
            "黃仁勳演講引爆台股！COMPUTEX 亮點總整理",
            "端午連假國道疏導措施看這裡，塞車路段預測",
            "花蓮近海清晨發生規模 4.8 地震，最大震度 4 級",
            "Apple Intelligence 登場！哪些 iPhone 支援一次看",
            "本週強檔：最新原創影集衝上台灣排行榜冠軍"
        ]
    }
    return pd.DataFrame(trends_data)

# 3. 模擬 網路溫度計 口碑榜數據
def get_dailyview_trends():
    dailyview_data = {
        "口碑排名": [1, 2, 3, 4, 5],
        "主題/人物": ["賴清德", "柯文哲", "Threads (脆)", "大巨蛋", "星宇航空"],
        "網路聲量 (筆)": ["152,430", "110,520", "98,400", "74,210", "61,900"],
        "好感度 (P/N 比)": ["0.65 (持平)", "0.42 (偏低)", "1.25 (極高)", "0.55 (持平)", "1.85 (極高)"]
    }
    return pd.DataFrame(dailyview_data)

# 4. 畫面排版：建立左右雙欄
col1, col2 = st.columns(2)

with col1:
    st.header("📈 Google 實時熱搜趨勢 (爆發力)")
    st.write("反映過去 24 小時內，搜尋量突然暴增的焦點。")
    df_google = get_google_trends()
    # 使用 Streamlit 自帶的漂亮表格呈現，並隱藏原本的索引
    st.dataframe(df_google, hide_index=True, use_container_width=True)

with col2:
    st.header("🌡️ 網路溫度計口碑榜 (持久聲量)")
    st.write("反映在各大社群、論壇中，長期累積的討論熱度。")
    df_dailyview = get_dailyview_trends()
    st.dataframe(df_dailyview, hide_index=True, use_container_width=True)

# 5. 頁腳說明
st.divider()
st.caption("🤖 本網站由 AI 協作開發完成。下一階段將開啟自動爬蟲與 AI 懶人包摘要功能。")
