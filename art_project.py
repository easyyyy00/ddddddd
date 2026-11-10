import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 국내 명화 데이터베이스
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="국내 미술관 검색 & 동선 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 국내 미술관 소장 작품 데이터베이스
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "황소",
        "artist": "이중섭",
        "style": "근대 서양화",
        "mood": "웅장한/어두운",
        "duration": 20,
        "museum": "국립현대미술관 (서울관)",
        "location": "1층 한국근현대미술 특별전시실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Lee_Jung-seob_Bull.jpg/1280px-Lee_Jung-seob_Bull.jpg",
        "description": "한국인의 민족적 강인함과 역동적인 생명력을 강렬한 붓터치로 표현한 근대 회화의 거작입니다.",
        "point": "소의 눈망울과 붉은 배경 속 힘찬 선의 여운을 감상해 보세요."
    },
    {
        "id": 2,
        "title": "미인도",
        "artist": "신윤복",
        "style": "조선 수묵풍속화",
        "mood": "화려한",
        "duration": 25,
        "museum": "간송미술관 (서울)",
        "location": "보화각 2층 한국화 전실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Shin_Yun-bok_-_Portrait_of_a_Beauty.jpg/1280px-Shin_Yun-bok_-_Portrait_of_a_Beauty.jpg",
        "description": "조선 후기 여인의 미의식과 우아한 자태를 묘사한 대표적인 한국 고미술 작품입니다.",
        "point": "섬세하게 묘사된 옷름과 붉은 삼회장저고리의 고운 선을 관찰해 보세요."
    },
    {
        "id": 3,
        "title": "우주 (05-IV-71 #200)",
        "artist": "김환기",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "duration": 30,
        "museum": "환기미술관 (서울)",
        "location": "본관 2층 점화 전용관",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Kim_Whanki_Universe.jpg/1280px-Kim_Whanki_Universe.jpg",
        "description": "푸른색 전면 점화로 우주의 아득함과 끝없는 깊이감을 은은한 울림으로 담아낸 추상화입니다.",
        "point": "수만 개의 무수한 푸른 점들이 이루어내는 은하수의 소용돌이를 느껴보세요."
    },
    {
        "id": 4,
        "title": "인왕제색도",
        "artist": "정선",
        "style": "조선 진경산수화",
        "mood": "웅장한/어두운",
        "duration": 20,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 실경산수화실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Inwang_jesaekdo.jpg/1280px-Inwang_jesaekdo.jpg",
        "description": "비가 그친 뒤 인왕산의 안개 낀 암벽을 묵직한 수묵 농담으로 그려낸 국보입니다.",
        "point": "물기에 젖은 검은 바위와 안개에 싸인 계곡의 대비를 감상 포인트로 삼아보세요."
    },
    {
        "id": 5,
        "title": "다다익선",
        "artist": "백남준",
        "style": "미디어 아트",
        "mood": "화려한",
        "duration": 25,
        "museum": "국립현대미술관 (과천관)",
        "location": "중앙홀 1-3층 연결 램프코어",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Nam_June_Paik_The_More_The_Better.jpg/1280px-Nam_June_Paik_The_More_The_Better.jpg",
        "description": "1,003대의 모니터를 탑 쌓기 형태로 설치한 세계 최대 규모의 비디오 아트 작품입니다.",
        "point": "화면들 속 다양한 영상과 탑 전체가 뿜어내는 현란한 리듬감을 확인해 보세요."
    },
    {
        "id": 6,
        "title": "묘작도",
        "artist": "변상벽",
        "style": "조선 영모화",
        "mood": "평화로운",
        "duration": 15,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 회화실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Byeon_Sang-byeok_-_Myojakdo.jpg/1280px-Byeon_Sang-byeok_-_Myojakdo.jpg",
        "description": "고양이와 참새의 한때를 정교한 필치로 세밀하게 그려낸 조선 후기 동물화 명작입니다.",
        "point": "고양이의 털 하나하나까지 사실적으로 묘사된 정밀한 표현력을 관찰해 보세요."
    },
    {
        "id": 7,
        "title": "작업 (Work)",
        "artist": "박수근",
        "style": "근대 서양화",
        "mood": "평화로운",
        "duration": 15,
        "museum": "리움미술관 (서울)",
        "location": "M1 3층 한국근대미술 전시장",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Park_Soo-keun_Work.jpg/1280px-Park_Soo-keun_Work.jpg",
        "description": "화강암을 연상시키는 특유의 거친 질감 위에 한국 서민들의 소박한 일상을 그려냈습니다.",
        "point": "마치 돌 위에 새겨진 듯한 한국적인 독특한 질감 표현을 느껴보세요."
    },
    {
        "id": 8,
        "title": "산월",
        "artist": "유영국",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "duration": 20,
        "museum": "국립현대미술관 (덕수궁관)",
        "location": "2층 한국 근대 추상전시실",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Yoo_Youngkuk_Mountain.jpg/1280px-Yoo_Youngkuk_Mountain.jpg",
        "description": "산과 달이라는 자연 요소를 강렬한 기하학적 색채와 조형적 선으로 재해석한 추상화입니다.",
        "point": "원색이 주는 따뜻한 에너지와 절제된 화면 구성을 감상해 보세요."
    }
]

# 예외 처리용 대표 명화
DEFAULT_ARTWORK = {
    "title": "세한도",
    "artist": "김정희",
    "style": "조선 문인화",
    "mood": "웅장한/어두운",
    "duration": 20,
    "museum": "국립중앙박물관 (서울)",
    "location": "서화관 2층 기증관",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Sehando_by_Kim_Jeong-hui.jpg/1280px-Sehando_by_Kim_Jeong-hui.jpg",
    "description": "추운 겨울에도 시들지 않는 소나무와 잣나무를 통해 변치 않는 지조를 담은 한국 대표 문인화입니다.",
    "point": "거칠고 메마른 붓질 속에서 전해지는 선비의 고결한 지조를 감상하세요."
}

# -----------------------------------------------------------------------------
# 2. 사이드바 - 미술관 검색 및 관람 옵션 설정
# -----------------------------------------------------------------------------
st.sidebar.title("🎨 미술관 동선 도슨트")
st.sidebar.write("미술관을 검색하거나 선택하면 소장 작품 중심 동선을 계산해 드립니다.")

# 1) 미술관 검색 및 드롭다운
search_query = st.sidebar.text_input("🔍 미술관 직접 검색 (예: 국립현대, 리움)", "")

museum_list = ["전체"] + sorted(list(set(art["museum"] for art in ARTWORKS_DB)))
selected_museum = st.sidebar.selectbox("🏛️ 목록에서 미술관 선택", museum_list)

# 2) 사조 / 분위기 / 시간 설정
styles = ["전체"] + sorted(list(set(art["style"] for art in ARTWORKS_DB)))
moods = ["전체"] + sorted(list(set(art["mood"] for art in ARTWORKS_DB)))

selected_style = st.sidebar.selectbox("🖌️ 선호 미술 사조", styles)
selected_mood = st.sidebar.radio("✨ 원하는 분위기", moods)
max_time = st.sidebar.slider("⏱️ 총 관람 가능 시간 (분)", min_value=15, max_value=120, value=60, step=5)

# -----------------------------------------------------------------------------
# 3. 검색어 및 시간 기반 동선 계산 알고리즘
# -----------------------------------------------------------------------------
filtered_artworks = []
accumulated_time = 0

for art in ARTWORKS_DB:
    # 1) 미술관 조건 (검색어가 입력되면 검색어 우선, 없으면 선택박스 기준)
    if search_query.strip():
        museum_match = search_query.strip().lower() in art["museum"].lower()
    else:
        museum_match = (selected_museum == "전체") or (art["museum"] == selected_museum)
    
    # 2) 사조 및 분위기 조건
    style_match = (selected_style == "전체") or (art["style"] == selected_style)
    mood_match = (selected_mood == "전체") or (art["mood"] == selected_mood)
    
    # 3) 조건에 충족하는 작품 중 관람 가능 시간 내 동선 추가 (누적 시간 계산)
    if museum_match and style_match and mood_match:
        if accumulated_time + art["duration"] <= max_time:
            filtered_artworks.append(art)
            accumulated_time += art["duration"]

# -----------------------------------------------------------------------------
# 4. 동선 추천 결과 및 카드 UI 출력
# -----------------------------------------------------------------------------
st.title("🏛️ 미술관별 맞춤 동선 계산 & 도슨트")
st.markdown("---")

# 검색 결과 예외 처리
if not filtered_artworks:
    st.warning("⚠️ 입력하신 미술관 검색어나 조건에 일치하는 작품 동선을 구성하지 못했습니다. 국보 대표 작품을 대체 안내합니다.")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        st.image(DEFAULT_ARTWORK["image_url"], caption=DEFAULT_ARTWORK["title"], use_container_width=True)
    with col_info:
        st.subheader(f"{DEFAULT_ARTWORK['title']} ({DEFAULT_ARTWORK['artist']})")
        st.markdown(f"📍 **소장 미술관:** `{DEFAULT_ARTWORK['museum']}` — *{DEFAULT_ARTWORK['location']}*")
        st.write(f"**사조:** {DEFAULT_ARTWORK['style']} | **소요 시간:** {DEFAULT_ARTWORK['duration']}분")
        st.info(f"**해설:** {DEFAULT_ARTWORK['description']}")
        st.success(f"**감상 포인트:** {DEFAULT_ARTWORK['point']}")

else:
    # 검색된 미술관명 표시 헤더
    target_museum = search_query if search_query else (selected_museum if selected_museum != "전체" else "전체 미술관")
    st.subheader(f"📍 [{target_museum}] 맞춤 관람 코스")
    st.info(f"⏱️ **추천 관람 동선:** 총 **{len(filtered_artworks)}개** 작품 관람 예정 | **소요 시간:** 약 **{accumulated_time}분** (설정 가능 시간: {max_time}분)")
    st.write("")

    # 작품 추천 동선 순서대로 2컬럼 레이아웃 배치
    for i in range(0, len(filtered_artworks), 2):
        cols = st.columns(2)
        for j in range(2):
            idx = i + j
            if idx < len(filtered_artworks):
                art = filtered_artworks[idx]
                with cols[j]:
                    with st.container(border=True):
                        # 관람 동선 순번 표시
                        st.markdown(f"### 🚩 **STEP {idx + 1}. {art['title']}**")
                        
                        try:
                            st.image(art["image_url"], use_container_width=True)
                        except Exception:
                            st.caption("🖼️ 이미지 불러오기 실패")
                        
                        st.markdown(f"📍 **소장:** {art['museum']}")
                        st.caption(f"🏛️ **전시실 위치:** {art['location']}")
                        st.write(f"**작가:** {art['artist']} | **사조:** {art['style']}")
                        st.write(f"**분위기:** {art['mood']} | **예상 관람 시간:** `{art['duration']}분`")
                        st.divider()
                        st.write(f"📖 **작품 해설**\n{art['description']}")
                        st.info(f"💡 **감상 포인트**\n{art['point']}")

    # -----------------------------------------------------------------------------
    # 5. 관람 순서 도록 표 및 CSV 다운로드
    # -----------------------------------------------------------------------------
    st.markdown("---")
    st.subheader("📋 동선순 관람 도록 요약본")

    df_raw = pd.DataFrame(filtered_artworks)
    # 관람 순번(STEP) 열 추가
    df_raw["step"] = [f"STEP {k+1}" for k in range(len(filtered_artworks))]
    
    columns_map = {
        "step": "관람 순서",
        "title": "작품명",
        "artist": "작가",
        "museum": "소장 미술관",
        "location": "전시실 위치",
        "duration": "소요 시간(분)",
        "description": "해설"
    }
    
    df_catalog = df_raw[list(columns_map.keys())].rename(columns=columns_map)
    st.dataframe(df_catalog, use_container_width=True)

    # 엑셀 깨짐 방지용 utf-8-sig 인코딩
    csv_data = df_catalog.to_csv(index=False).encode('utf-8-sig')

    st.download_button(
        label="📥 동선 도록 다운로드 (CSV)",
        data=csv_data,
        file_name="museum_route_catalog.csv",
        mime="text/csv"
    )
