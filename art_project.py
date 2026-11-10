import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 국내 명화 데이터베이스
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="국내 미술관 맞춤 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 기본 명화 데이터베이스 (기본값: 여유 감상 소요 시간 기준)
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "황소",
        "artist": "이중섭",
        "style": "근대 서양화",
        "mood": "웅장한/어두운",
        "time_normal": 20, # 여유 모드 (분)
        "time_fast": 10,   # 쾌속 모드 (분)
        "museum": "국립현대미술관 (서울관)",
        "location": "1층 한국근현대미술 특별전시실",
        "image_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=800",
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
        "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800",
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
        "image_url": "https://images.unsplash.com/photo-1579783901586-d8827248356f?w=800",
        "description": "조선 후기 여인의 미의식과 우아한 자태를 묘사한 대표적인 한국 고미술 작품입니다.",
        "point_normal": "섬세하게 묘사된 옷름과 붉은 삼회장저고리의 고운 선, 얹은머리의 디테일을 들여다보세요.",
        "point_fast": "여인의 섬세한 인상과 저고리 선의 고운 흐름을 빠르게 관찰하세요."
    },
    {
        "id": 4,
        "title": "우주 (05-IV-71 #200)",
        "artist": "김환기",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "time_normal": 25,
        "time_fast": 10,
        "museum": "환기미술관 (서울)",
        "location": "본관 2층 점화 전용관",
        "image_url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800",
        "description": "푸른색 전면 점화로 우주의 아득함과 깊이감을 은은한 울림으로 담아낸 추상화입니다.",
        "point_normal": "수만 개의 무수한 푸른 점들이 이루어내는 은하수의 소용돌이와 깊은 울림을 정적으로 감상해 보세요.",
        "point_fast": "전면 점화가 주는 동심원의 거대한 소용돌이 패턴을 감상하세요."
    },
    {
        "id": 5,
        "title": "인왕제색도",
        "artist": "정선",
        "style": "조선 진경산수화",
        "mood": "웅장한/어두운",
        "time_normal": 20,
        "time_fast": 9,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 실경산수화실",
        "image_url": "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=800",
        "description": "비가 그친 뒤 인왕산의 안개 낀 암벽을 묵직한 수묵 농담으로 그려낸 국보입니다.",
        "point_normal": "물기에 젖은 검은 바위의 적묵법과 하얗게 피어오르는 계곡 안개의 대비를 관찰하세요.",
        "point_fast": "검은 암벽의 웅장함과 하얀 안개의 수묵 대비를 포커스로 보세요."
    },
    {
        "id": 6,
        "title": "다다익선",
        "artist": "백남준",
        "style": "미디어 아트",
        "mood": "화려한",
        "time_normal": 20,
        "time_fast": 10,
        "museum": "국립현대미술관 (과천관)",
        "location": "중앙홀 1-3층 연결 램프코어",
        "image_url": "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800",
        "description": "1,003대의 모니터를 탑 쌓기 형태로 설치한 세계 최대 규모의 비디오 아트 작품입니다.",
        "point_normal": "1층부터 3층까지 램프코어를 따라 올라가며 다채롭게 바뀌는 모니터 전경을 감상해 보세요.",
        "point_fast": "모니터 탑 전체가 뿜어내는 비디오 아트의 화려한 리듬감을 확인하세요."
    },
    {
        "id": 7,
        "title": "묘작도",
        "artist": "변상벽",
        "style": "조선 영모화",
        "mood": "평화로운",
        "time_normal": 15,
        "time_fast": 7,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 회화실",
        "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800",
        "description": "고양이와 참새의 한때를 정교한 필치로 세밀하게 그려낸 조선 후기 동물화 명작입니다.",
        "point_normal": "고양이 털의 세밀한 결 표현과 나무 위 참새들의 생생한 위치 배치를 살펴보세요.",
        "point_fast": "고양이 털의 세밀한 묘사력과 참새들의 표정에 주목하세요."
    },
    {
        "id": 8,
        "title": "작업 (Work)",
        "artist": "박수근",
        "style": "근대 서양화",
        "mood": "평화로운",
        "time_normal": 15,
        "time_fast": 8,
        "museum": "리움미술관 (서울)",
        "location": "M1 3층 한국근대미술 전시장",
        "image_url": "https://images.unsplash.com/photo-1579783901586-d8827248356f?w=800",
        "description": "화강암을 연상시키는 특유의 거친 질감 위에 한국 서민들의 소박한 일상을 그려냈습니다.",
        "point_normal": "여러 번 겹쳐 칠해 만든 돌 벽면 같은 독특한 질감과 서민들의 차분한 포즈를 느껴보세요.",
        "point_fast": "화강암을 연상시키는 한국적인 독특한 마티에르(질감)를 확인하세요."
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
    "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800",
    "description": "추운 겨울에도 시들지 않는 소나무와 잣나무를 통해 변치 않는 지조를 담은 한국 대표 문인화입니다.",
    "point": "거칠고 메마른 붓질 속에서 전해지는 선비의 고결한 지조를 감상하세요."
}

# -----------------------------------------------------------------------------
# 2. 사이드바 - 감상 모드 분리 및 검색 옵션
# -----------------------------------------------------------------------------
st.sidebar.title("🎨 미술관 도슨트 설정")

# ⭐️ 핵심 변경: 관람 모드 분리 버튼 (라디오 옵션)
view_mode = st.sidebar.radio(
    "🏃‍♂️ 관람 스타일에 맞춰 모드를 선택하세요",
    ["🍃 여유 감상 모드 (작품당 15~25분)", "⚡ 쾌속 감상 모드 (작품당 7~10분)"]
)

# 모드 상태 체크
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
# 3. 관람 모드별 소요 시간 적용 및 동선 계산 알고리즘
# -----------------------------------------------------------------------------
filtered_artworks = []
accumulated_time = 0

for art in ARTWORKS_DB:
    # 모드에 따른 소요 시간 및 감상 포인트 선택
    duration = art["time_fast"] if is_fast_mode else art["time_normal"]
    point = art["point_fast"] if is_fast_mode else art["point_normal"]
    
    # 검색 조건
    if search_query.strip():
        museum_match = search_query.strip().lower() in art["museum"].lower()
    else:
        museum_match = (selected_museum == "전체") or (art["museum"] == selected_museum)
    
    style_match = (selected_style == "전체") or (art["style"] == selected_style)
    mood_match = (selected_mood == "전체") or (art["mood"] == selected_mood)
    
    # 조건 만족 시 동선에 추가 (누적 시간 제어)
    if museum_match and style_match and mood_match:
        if accumulated_time + duration <= max_time:
            # 렌더링용 임시 필드 설정
            art_copy = art.copy()
            art_copy["current_duration"] = duration
            art_copy["current_point"] = point
            filtered_artworks.append(art_copy)
            accumulated_time += duration

# -----------------------------------------------------------------------------
# 4. 결과 출력 및 카드 배치
# -----------------------------------------------------------------------------
st.title("🏛️ 맞춤형 미술관 큐레이팅 도슨트")

# 모드별 안내 배너
if is_fast_mode:
    st.success("⚡ **쾌속 감상 모드 활성화:** 작품당 7~10분 내외의 핵심 가이드로 제한된 시간 내 **더 많은 다작(多作)**을 추천합니다.")
else:
    st.info("🍃 **여유 감상 모드 활성화:** 작품당 15~25분의 소요 시간으로 작품의 깊이 있는 해설과 디테일을 느긋하게 감상합니다.")

st.markdown("---")

if not filtered_artworks:
    st.warning("⚠️ 선택하신 조건에 맞는 작품 조합이 없습니다. 대표 명화를 안내합니다.")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        st.image(DEFAULT_ARTWORK["image_url"], caption=DEFAULT_ARTWORK["title"], use_container_width=True)
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
                        
                        try:
                            st.image(art["image_url"], use_container_width=True)
                        except Exception:
                            st.caption("🖼️ 이미지 불러오기 실패")
                        
                        st.markdown(f"📍 **소장:** {art['museum']}")
                        st.caption(f"🏛️ **전시실 위치:** {art['location']}")
                        st.write(f"**작가:** {art['artist']} | **사조:** {art['style']} | **분위기:** {art['mood']}")
                        st.divider()
                        st.write(f"📖 **작품 해설**\n{art['description']}")
                        st.info(f"💡 **감상 포인트**\n{art['current_point']}")

    # -----------------------------------------------------------------------------
    # 5. 관람 도록 표 및 CSV 다운로드
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
