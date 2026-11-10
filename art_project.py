import streamlit as st
import pandas as pd
from PIL import Image
import urllib.request
import io

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 명화 데이터베이스
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="국내 미술관 맞춤 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 외부 차단 방지를 위한 이미지 로더 함수 (URL ➔ PIL Image)
@st.cache_data
def load_image_from_url(url):
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
        return Image.open(io.BytesIO(image_data))
    except Exception:
        return None

# 실제 명화 데이터베이스
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "황소",
        "artist": "이중섭",
        "style": "근대 서양화",
        "mood": "웅장한/어두운",
        "time_normal": 20,
        "time_fast": 10,
        "museum": "국립현대미술관 (서울관)",
        "location": "1층 한국근현대미술 특별전시실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Lee_Jung-seob_Bull.jpg/800px-Lee_Jung-seob_Bull.jpg",
        "description": "한국인의 민족적 강인함과 역동적인 생명력을 강렬한 붓터치로 표현한 근대 회화의 거작입니다.",
        "point_normal": "소의 눈망울과 붉은 배경 속 힘찬 선의 여운, 질감의 농담을 천천히 감상해 보세요.",
        "point_fast": "소의 강렬한 눈망울과 힘찬 붓터치 선에 집중하세요."
    },
    {
        "id": 2,
        "title": "씨름",
        "artist": "김홍도",
        "style": "조선 수묵풍속화",
        "mood": "평화로운",
        "time_normal": 15,
        "time_fast": 8,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 풍속화실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Gim_Hong-do-Ssireum.jpg/800px-Gim_Hong-do-Ssireum.jpg",
        "description": "씨름판을 둘러싼 관객들의 다양한 표정과 생동감 넘치는 원형 구도의 대표 풍속화입니다.",
        "point_normal": "화면 구석 엿장수부터 각양각색 관객들의 생생한 손짓과 표정을 하나씩 살펴보세요.",
        "point_fast": "씨름하는 두 인물의 긴장감과 화면 우측 하단 엿장수의 표정을 체크하세요."
    },
    {
        "id": 3,
        "title": "미인도",
        "artist": "신윤복",
        "style": "조선 수묵풍속화",
        "mood": "화려한",
        "time_normal": 20,
        "time_fast": 10,
        "museum": "간송미술관 (서울)",
        "location": "보화각 2층 한국화 전실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Shin_Yun-bok_-_Portrait_of_a_Beauty.jpg/800px-Shin_Yun-bok_-_Portrait_of_a_Beauty.jpg",
        "description": "조선 후기 여인의 미의식과 우아한 자태를 묘사한 대표적인 한국 고미술 작품입니다.",
        "point_normal": "섬세하게 묘사된 옷름과 붉은 삼회장저고리의 고운 선, 얹은머리의 디테일을 들여다보세요.",
        "point_fast": "여인의 섬세한 인상과 저고리 선의 고운 흐름을 빠르게 관찰하세요."
    },
    {
        "id": 4,
        "title": "인왕제색도",
        "artist": "정선",
        "style": "조선 진경산수화",
        "mood": "웅장한/어두운",
        "time_normal": 20,
        "time_fast": 9,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 실경산수화실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Inwang_jesaekdo.jpg/800px-Inwang_jesaekdo.jpg",
        "description": "비가 그친 뒤 인왕산의 안개 낀 암벽을 묵직한 수묵 농담으로 그려낸 국보입니다.",
        "point_normal": "물기에 젖은 검은 바위의 적묵법과 하얗게 피어오르는 계곡 안개의 대비를 관찰하세요.",
        "point_fast": "검은 암벽의 웅장함과 하얀 안개의 수묵 대비를 포커스로 보세요."
    },
    {
        "id": 5,
        "title": "묘작도 (猫雀圖)",
        "artist": "변상벽",
        "style": "조선 영모화",
        "mood": "평화로운",
        "time_normal": 15,
        "time_fast": 7,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 회화실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Byeon_Sang-byeok_-_Myojakdo.jpg/800px-Byeon_Sang-byeok_-_Myojakdo.jpg",
        "description": "조선 후기 화재 변상벽이 나무 위 참새를 바라보는 고양이의 순간을 섬세하게 담아낸 국보급 영모화입니다.",
        "point_normal": "고양이 털의 한 가닥까지 세밀하게 묘사한 정교한 필치와 고목나무 위 참새들의 생동감을 살펴보세요.",
        "point_fast": "고양이의 사실적인 털 묘사와 나무 위 참새의 구도에 주목하세요."
    },
    {
        "id": 6,
        "title": "세한도",
        "artist": "김정희",
        "style": "조선 문인화",
        "mood": "웅장한/어두운",
        "time_normal": 15,
        "time_fast": 8,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 기증관",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Sehando_by_Kim_Jeong-hui.jpg/800px-Sehando_by_Kim_Jeong-hui.jpg",
        "description": "추운 겨울에도 시들지 않는 소나무와 잣나무를 통해 변치 않는 지조를 담은 한국 대표 문인화입니다.",
        "point_normal": "거칠고 메마른 갈필 붓질 속에서 전해지는 절제된 선비 정신을 천천히 감상해 보세요.",
        "point_fast": "메마른 붓으로 표현된 소나무와 집의 절제된 구도를 관찰하세요."
    }
]

# 대표 명화 (예외 처리용)
DEFAULT_ARTWORK = {
    "title": "세한도",
    "artist": "김정희",
    "style": "조선 문인화",
    "mood": "웅장한/어두운",
    "duration": 15,
    "museum": "국립중앙박물관 (서울)",
    "location": "서화관 2층 기증관",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Sehando_by_Kim_Jeong-hui.jpg/800px-Sehando_by_Kim_Jeong-hui.jpg",
    "description": "추운 겨울에도 시들지 않는 소나무와 잣나무를 통해 변치 않는 지조를 담은 한국 대표 문인화입니다.",
    "point": "거칠고 메마른 붓질 속에서 전해지는 선비의 고결한 지조를 감상하세요."
}

# -----------------------------------------------------------------------------
# 2. 사이드바 - 관람 옵션 설정
# -----------------------------------------------------------------------------
st.sidebar.title("🎨 미술관 도슨트 설정")

view_mode = st.sidebar.radio(
    "🏃‍♂️ 관람 스타일에 맞춰 모드를 선택하세요",
    ["🍃 여유 감상 모드 (작품당 15~25분)", "⚡ 쾌속 감상 모드 (작품당 7~10분)"]
)

is_fast_mode = "쾌속" in view_mode

st.sidebar.markdown("---")

search_query = st.sidebar.text_input("🔍 미술관 직접 검색 (예: 국립현대, 국립중앙)", "")

museum_list = ["전체"] + sorted(list(set(art["museum"] for art in ARTWORKS_DB)))
selected_museum = st.sidebar.selectbox("🏛️ 목록에서 미술관 선택", museum_list)

styles = ["전체"] + sorted(list(set(art["style"] for art in ARTWORKS_DB)))
moods = ["전체"] + sorted(list(set(art["mood"] for art in ARTWORKS_DB)))

selected_style = st.sidebar.selectbox("🖌️ 선호 미술 사조", styles)
selected_mood = st.sidebar.radio("✨ 원하는 분위기", moods)
max_time = st.sidebar.slider("⏱️ 총 관람 가능 시간 (분)", min_value=15, max_value=120, value=60, step=5)

# -----------------------------------------------------------------------------
# 3. 추천 동선 알고리즘
# -----------------------------------------------------------------------------
filtered_artworks = []
accumulated_time = 0

for art in ARTWORKS_DB:
    duration = art["time_fast"] if is_fast_mode else art["time_normal"]
    point = art["point_fast"] if is_fast_mode else art["point_normal"]
    
    if search_query.strip():
        museum_match = search_query.strip().lower() in art["museum"].lower()
    else:
        museum_match = (selected_museum == "전체") or (art["museum"] == selected_museum)
    
    style_match = (selected_style == "전체") or (art["style"] == selected_style)
    mood_match = (selected_mood == "전체") or (art["mood"] == selected_mood)
    
    if museum_match and style_match and mood_match:
        if accumulated_time + duration <= max_time:
            art_copy = art.copy()
            art_copy["current_duration"] = duration
            art_copy["current_point"] = point
            filtered_artworks.append(art_copy)
            accumulated_time += duration

# -----------------------------------------------------------------------------
# 4. 결과 출력
# -----------------------------------------------------------------------------
st.title("🏛️ 맞춤형 미술관 큐레이팅 도슨트")

if is_fast_mode:
    st.success("⚡ **쾌속 감상 모드 활성화:** 작품당 7~10분 내외의 핵심 가이드로 제한된 시간 내 **더 많은 다작(多作)**을 추천합니다.")
else:
    st.info("🍃 **여유 감상 모드 활성화:** 작품당 15~25분의 소요 시간으로 작품의 깊이 있는 해설과 디테일을 느긋하게 감상합니다.")

st.markdown("---")

if not filtered_artworks:
    st.warning("⚠️ 선택하신 조건에 맞는 작품 조합이 없습니다. 대표 명화를 안내합니다.")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        img = load_image_from_url(DEFAULT_ARTWORK["image_url"])
        if img:
            st.image(img, caption=DEFAULT_ARTWORK["title"], use_container_width=True)
        else:
            st.caption("🖼️ [이미지 로딩 불가] 외부 네트워크 보안으로 이미지를 볼 수 없습니다.")
            
    with col_info:
        st.subheader(f"{DEFAULT_ARTWORK['title']} ({DEFAULT_ARTWORK['artist']})")
        st.markdown(f"📍 **소장 미술관:** `{DEFAULT_ARTWORK['museum']}` — *{DEFAULT_ARTWORK['location']}*")
        st.write(f"**사조:** {DEFAULT_ARTWORK['style']} | **소요 시간:** 약 {DEFAULT_ARTWORK['duration']}분")
        st.info(f"**해설:** {DEFAULT_ARTWORK['description']}")
        st.success(f"**감상 포인트:** {DEFAULT_ARTWORK['point']}")

else:
    target_museum = search_query if search_query else (selected_museum if selected_museum != "전체" else "전체 미술관")
    st.subheader(f"📍 [{target_museum}] 맞춤 관람 코스")
    st.markdown(f"⏱️ **추천 결과:** 총 **{len(filtered_artworks)}개** 작품 감상 예정 | **소요 시간:** 약 **{accumulated_time}분** (설정 시간: {max_time}분)")
    st.write("")

    for i in range(0, len(filtered_artworks), 2):
        cols = st.columns(2)
        for j in range(2):
            idx = i + j
            if idx < len(filtered_artworks):
                art = filtered_artworks[idx]
                with cols[j]:
                    with st.container(border=True):
                        st.markdown(f"### 🚩 **STEP {idx + 1}. {art['title']}** (`{art['current_duration']}분 코스`)")
                        
                        # 우회 함수를 사용해 안전하게 이미지 로딩
                        img = load_image_from_url(art["image_url"])
                        if img:
                            st.image(img, use_container_width=True)
                        else:
                            st.info(f"🖼️ **[작품 원화 전경: {art['title']}]**\n\n*(네트워크 차단으로 이미지를 열 수 없는 경우 로컬 이미지 파일 경로를 사용하세요)*")
                        
                        st.markdown(f"📍 **소장:** {art['museum']}")
                        st.caption(f"🏛️ **전시실 위치:** {art['location']}")
                        st.write(f"**작가:** {art['artist']} | **사조:** {art['style']} | **분위기:** {art['mood']}")
                        st.divider()
                        st.write(f"📖 **작품 해설**\n{art['description']}")
                        st.info(f"💡 **감상 포인트**\n{art['current_point']}")

    # -----------------------------------------------------------------------------
    # 5. 도록 요약본 및 CSV 저장
    # -----------------------------------------------------------------------------
    st.markdown("---")
    st.subheader("📋 동선순 관람 도록 요약본")

    df_raw = pd.DataFrame(filtered_artworks)
    df_raw["step"] = [f"STEP {k+1}" for k in range(len(filtered_artworks))]
    df_raw["duration_str"] = df_raw["current_duration"].astype(str) + "분"
    
    columns_map = {
        "step": "관람 순서",
        "title": "작품명",
        "artist": "작가",
        "museum": "소장 미술관",
        "location": "전시실 위치",
        "duration_str": "소요 시간",
        "description": "해설"
    }
    
    df_catalog = df_raw[list(columns_map.keys())].rename(columns=columns_map)
    st.dataframe(df_catalog, use_container_width=True)

    csv_data = df_catalog.to_csv(index=False).encode('utf-8-sig')

    st.download_button(
        label="📥 관람 도록 다운로드 (CSV)",
        data=csv_data,
        file_name="museum_route_catalog.csv",
        mime="text/csv"
    )
