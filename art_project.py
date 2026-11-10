import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 국내 명화 데이터베이스 (작품당 7~10분 구성)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="국내 미술관 다작 관람 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 작품 수 대폭 확장 & 소요 시간 7~10분 적용 데이터베이스
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "황소",
        "artist": "이중섭",
        "style": "근대 서양화",
        "mood": "웅장한/어두운",
        "duration": 10,
        "museum": "국립현대미술관 (서울관)",
        "location": "1층 한국근현대미술 특별전시실",
        "image_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=800",
        "description": "한국인의 민족적 강인함과 역동적인 생명력을 강렬한 붓터치로 표현한 거작입니다.",
        "point": "소의 눈망울과 붉은 배경 속 힘찬 선의 여운을 집중적으로 감상하세요."
    },
    {
        "id": 2,
        "title": "씨름",
        "artist": "김홍도",
        "style": "조선 수묵풍속화",
        "mood": "평화로운",
        "duration": 8,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 풍속화실",
        "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800",
        "description": "씨름판을 둘러싼 관객들의 다양한 표정과 생동감 넘치는 원형 구도의 대표 풍속화입니다.",
        "point": "엿장수와 구경꾼들의 신나는 표정 변화를 포인터 삼아 감상해 보세요."
    },
    {
        "id": 3,
        "title": "미인도",
        "artist": "신윤복",
        "style": "조선 수묵풍속화",
        "mood": "화려한",
        "duration": 10,
        "museum": "간송미술관 (서울)",
        "location": "보화각 2층 한국화 전실",
        "image_url": "https://images.unsplash.com/photo-1579783901586-d8827248356f?w=800",
        "description": "조선 후기 여인의 미의식과 우아한 자태를 묘사한 대표적인 한국 고미술 작품입니다.",
        "point": "섬세하게 묘사된 옷름과 삼회장저고리의 고운 선을 관찰해 보세요."
    },
    {
        "id": 4,
        "title": "우주 (05-IV-71 #200)",
        "artist": "김환기",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "duration": 10,
        "museum": "환기미술관 (서울)",
        "location": "본관 2층 점화 전용관",
        "image_url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800",
        "description": "푸른색 전면 점화로 우주의 아득함과 깊이감을 은은한 울림으로 담아낸 추상화입니다.",
        "point": "무수한 푸른 점들이 이루어내는 은하수의 소용돌이를 느껴보세요."
    },
    {
        "id": 5,
        "title": "인왕제색도",
        "artist": "정선",
        "style": "조선 진경산수화",
        "mood": "웅장한/어두운",
        "duration": 9,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 실경산수화실",
        "image_url": "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=800",
        "description": "비가 그친 뒤 인왕산의 안개 낀 암벽을 묵직한 수묵 농담으로 그려낸 국보입니다.",
        "point": "물기에 젖은 검은 바위와 안개에 싸인 계곡의 대비에 주목해 보세요."
    },
    {
        "id": 6,
        "title": "다다익선",
        "artist": "백남준",
        "style": "미디어 아트",
        "mood": "화려한",
        "duration": 10,
        "museum": "국립현대미술관 (과천관)",
        "location": "중앙홀 1-3층 연결 램프코어",
        "image_url": "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800",
        "description": "1,003대의 모니터를 탑 쌓기 형태로 설치한 세계 최대 규모의 비디오 아트 작품입니다.",
        "point": "다양한 영상 모니터 탑 전체가 뿜어내는 현란한 리듬감을 확인해 보세요."
    },
    {
        "id": 7,
        "title": "묘작도",
        "artist": "변상벽",
        "style": "조선 영모화",
        "mood": "평화로운",
        "duration": 7,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 회화실",
        "image_url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800",
        "description": "고양이와 참새의 한때를 정교한 필치로 세밀하게 그려낸 조선 후기 동물화 명작입니다.",
        "point": "고양이의 털 하나하나 세밀하게 묘사된 정밀한 표현력을 관찰해 보세요."
    },
    {
        "id": 8,
        "title": "작업 (Work)",
        "artist": "박수근",
        "style": "근대 서양화",
        "mood": "평화로운",
        "duration": 8,
        "museum": "리움미술관 (서울)",
        "location": "M1 3층 한국근대미술 전시장",
        "image_url": "https://images.unsplash.com/photo-1579783901586-d8827248356f?w=800",
        "description": "화강암을 연상시키는 특유의 거친 질감 위에 한국 서민들의 소박한 일상을 그려냈습니다.",
        "point": "마치 돌 위에 새겨진 듯한 한국적인 독특한 질감을 느껴보세요."
    },
    {
        "id": 9,
        "title": "산월",
        "artist": "유영국",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "duration": 8,
        "museum": "국립현대미술관 (덕수궁관)",
        "location": "2층 한국 근대 추상전시실",
        "image_url": "https://images.unsplash.com/photo-1507646221600-a1913af8861a?w=800",
        "description": "산과 달이라는 자연 요소를 강렬한 기하학적 색채와 조형적 선으로 재해석한 작품입니다.",
        "point": "원색이 주는 강렬한 에너지와 절제된 화면 구성을 감상해 보세요."
    },
    {
        "id": 10,
        "title": "생태",
        "artist": "천경자",
        "style": "한국화/채색화",
        "mood": "화려한",
        "duration": 9,
        "museum": "서울시립미술관 (서소문본관)",
        "location": "2층 천경자 컬렉션 전용전시실",
        "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800",
        "description": "수십 마리의 뱀이 엉켜 있는 강렬한 구도를 통해 한과 생명력을 채색으로 표현한 대표작입니다.",
        "point": "화려하면서도 기묘한 채색의 농담과 인상적인 구도를 포인트로 삼으세요."
    },
    {
        "id": 11,
        "title": "어디서 무엇이 되어 다시 만나랴",
        "artist": "김환기",
        "style": "한국 추상미술",
        "mood": "몽환적인",
        "duration": 10,
        "museum": "환기미술관 (서울)",
        "location": "본관 1층 전시장",
        "image_url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800",
        "description": "이광섭의 시구에서 제목을 따와 그리운 이들을 생각하며 점을 찍어나간 서정적 추상화입니다.",
        "point": "점 하나하나에 담긴 작가의 고독과 그리움의 정서를 정적으로 감상해 보세요."
    },
    {
        "id": 12,
        "title": "강산무진도",
        "artist": "이인문",
        "style": "조선 산수화",
        "mood": "웅장한/어두운",
        "duration": 10,
        "museum": "국립중앙박물관 (서울)",
        "location": "서화관 2층 회화실",
        "image_url": "https://images.unsplash.com/photo-1578926375605-eaf7559b1458?w=800",
        "description": "대자연의 무궁무진한 산수 풍경을 대형 두루마리에 광활하고 웅장하게 파노라마로 펼친 작품입니다.",
        "point": "끊임없이 이어지는 산천과 사람들의 소소한 일상을 시선의 이동에 따라 파노라마로 보세요."
    }
]

# 대표 명화 (예외 처리용)
DEFAULT_ARTWORK = {
    "title": "세한도",
    "artist": "김정희",
    "style": "조선 문인화",
    "mood": "웅장한/어두운",
    "duration": 8,
    "museum": "국립중앙박물관 (서울)",
    "location": "서화관 2층 기증관",
    "image_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800",
    "description": "추운 겨울에도 시들지 않는 소나무와 잣나무를 통해 변치 않는 지조를 담은 한국 대표 문인화입니다.",
    "point": "거칠고 메마른 붓질 속에서 전해지는 선비의 고결한 지조를 감상하세요."
}

# -----------------------------------------------------------------------------
# 2. 사이드바 - 미술관 검색 및 필터 입력
# -----------------------------------------------------------------------------
st.sidebar.title("🎨 다작 코스 쾌속 도슨트")
st.sidebar.write("작품당 7~10분 내외로 핵심만 빠르게 감상할 수 있는 동선을 짜드립니다.")

search_query = st.sidebar.text_input("🔍 미술관 직접 검색 (예: 국립현대, 국립중앙)", "")

museum_list = ["전체"] + sorted(list(set(art["museum"] for art in ARTWORKS_DB)))
selected_museum = st.sidebar.selectbox("🏛️ 목록에서 미술관 선택", museum_list)

styles = ["전체"] + sorted(list(set(art["style"] for art in ARTWORKS_DB)))
moods = ["전체"] + sorted(list(set(art["mood"] for art in ARTWORKS_DB)))

selected_style = st.sidebar.selectbox("🖌️ 선호 미술 사조", styles)
selected_mood = st.sidebar.radio("✨ 원하는 분위기", moods)
max_time = st.sidebar.slider("⏱️ 총 관람 가능 시간 (분)", min_value=15, max_value=120, value=60, step=5)

# -----------------------------------------------------------------------------
# 3. 쾌속 관람 동선 계산 알고리즘 (누적 시간 제어)
# -----------------------------------------------------------------------------
filtered_artworks = []
accumulated_time = 0

for art in ARTWORKS_DB:
    if search_query.strip():
        museum_match = search_query.strip().lower() in art["museum"].lower()
    else:
        museum_match = (selected_museum == "전체") or (art["museum"] == selected_museum)
    
    style_match = (selected_style == "전체") or (art["style"] == selected_style)
    mood_match = (selected_mood == "전체") or (art["mood"] == selected_mood)
    
    if museum_match and style_match and mood_match:
        if accumulated_time + art["duration"] <= max_time:
            filtered_artworks.append(art)
            accumulated_time += art["duration"]

# -----------------------------------------------------------------------------
# 4. 결과 화면 및 쾌속 관람 카드 배치
# -----------------------------------------------------------------------------
st.title("🏛️ 맞춤형 다작(多作) 관람 큐레이팅 도슨트")
st.caption("⚡ 작품당 7~10분 핵심 감상 코스로 제한된 시간 내 가장 많은 작품을 관람하세요.")
st.markdown("---")

if not filtered_artworks:
    st.warning("⚠️ 입력하신 조건에 들어맞는 작품 조합을 찾지 못했습니다. 대표 국보 명화를 대체 안내합니다.")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        st.image(DEFAULT_ARTWORK["image_url"], caption=DEFAULT_ARTWORK["title"], use_container_width=True)
    with col_info:
        st.subheader(f"{DEFAULT_ARTWORK['title']} ({DEFAULT_ARTWORK['artist']})")
        st.markdown(f"📍 **소장 미술관:** `{DEFAULT_ARTWORK['museum']}` — *{DEFAULT_ARTWORK['location']}*")
        st.write(f"**사조:** {DEFAULT_ARTWORK['style']} | **핵심 소요 시간:** {DEFAULT_ARTWORK['duration']}분")
        st.info(f"**해설:** {DEFAULT_ARTWORK['description']}")
        st.success(f"**감상 포인트:** {DEFAULT_ARTWORK['point']}")

else:
    target_museum = search_query if search_query else (selected_museum if selected_museum != "전체" else "전체 미술관")
    st.subheader(f"📍 [{target_museum}] 쾌속 집중 관람 코스")
    st.success(f"⚡ **추천 코스 요약:** 총 **{len(filtered_artworks)}개**의 많은 작품 감상 예정 | **총 예상 시간:** 약 **{accumulated_time}분** (설정 시간: {max_time}분)")
    st.write("")

    for i in range(0, len(filtered_artworks), 2):
        cols = st.columns(2)
        for j in range(2):
            idx = i + j
            if idx < len(filtered_artworks):
                art = filtered_artworks[idx]
                with cols[j]:
                    with st.container(border=True):
                        st.markdown(f"### 🚩 **STEP {idx + 1}. {art['title']}** (⏱️ `{art['duration']}분 코스`)")
                        
                        try:
                            st.image(art["image_url"], use_container_width=True)
                        except Exception:
                            st.caption("🖼️ 이미지 불러오기 실패")
                        
                        st.markdown(f"📍 **소장:** {art['museum']}")
                        st.caption(f"🏛️ **전시실 위치:** {art['location']}")
                        st.write(f"**작가:** {art['artist']} | **사조:** {art['style']} | **분위기:** {art['mood']}")
                        st.divider()
                        st.write(f"📖 **핵심 요약 해설**\n{art['description']}")
                        st.info(f"💡 **10초 감상 포인트**\n{art['point']}")

    # -----------------------------------------------------------------------------
    # 5. 도록 요약본 및 CSV 다운로드
    # -----------------------------------------------------------------------------
    st.markdown("---")
    st.subheader("📋 쾌속 관람 동선 도록 요약본")

    df_raw = pd.DataFrame(filtered_artworks)
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

    csv_data = df_catalog.to_csv(index=False).encode('utf-8-sig')

    st.download_button(
        label="📥 쾌속 동선 도록 다운로드 (CSV)",
        data=csv_data,
        file_name="fast_track_museum_catalog.csv",
        mime="text/csv"
    )
