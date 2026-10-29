import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 명화 데이터베이스 정의
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="디지털 미술관 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 자체 명화 데이터베이스 (외부 DB 연결 없음)
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "별이 빛나는 밤",
        "artist": "빈센트 반 고흐",
        "style": "후기 인상주의",
        "mood": "몽환적인",
        "duration": 20,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        "description": "밤하늘의 요동치는 소용돌이와 소나무의 강렬한 생명력을 표현한 작품입니다.",
        "point": "강렬한 붓터치와 밤하늘의 색채 대비를 중심으로 감상해 보세요."
    },
    {
        "id": 2,
        "title": "인상, 일출",
        "artist": "클로드 모네",
        "style": "인상주의",
        "mood": "평화로운",
        "duration": 15,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg/1280px-Claude_Monet%2C_Impression%2C_soleil_levant.jpg",
        "description": "인상파라는 이름을 만들어낸 역사적인 작품으로, 붉은 태양과 항구의 안개를 담았습니다.",
        "point": "빛의 변화에 따라 시시각각 달라지는 순찰의 순간을 느껴보세요."
    },
    {
        "id": 3,
        "title": "기억의 지속",
        "artist": "살바도르 달리",
        "style": "초현실주의",
        "mood": "몽환적인",
        "duration": 25,
        "image_url": "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg",
        "description": "흘러내리는 시계를 통해 시간의 상대성과 무의식의 세계를 그린 작품입니다.",
        "point": "현실에서는 불가능한 사물들의 배치와 기이한 분위기에 집중해 보세요."
    },
    {
        "id": 4,
        "title": "절규",
        "artist": "에드바르 문크",
        "style": "표현주의",
        "mood": "웅장한/어두운",
        "duration": 15,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73.5_cm%2C_National_Museum_of_Art%2C_Architecture_and_Design.jpg/1280px-Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73.5_cm%2C_National_Museum_of_Art%2C_Architecture_and_Design.jpg",
        "description": "현대인의 불안과 고독을 핏빛 하늘과 곡선의 구도로 극대화하여 표현했습니다.",
        "point": "인물의 기괴한 표정과 소용돌이치는 배경 선의 불안감을 감상 포인트로 삼아보세요."
    },
    {
        "id": 5,
        "title": "비너스의 탄생",
        "artist": "산드로 보티첼리",
        "style": "르네상스",
        "mood": "화려한",
        "duration": 30,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/1280px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg",
        "description": "바다 조개껍데기 위에서 탄생한 비너스의 신화적 순간을 우아한 선으로 그린 명화입니다.",
        "point": "비너스의 우아한 포즈와 화면 전반에 흐르는 신화적 아우라를 관찰해 보세요."
    },
    {
        "id": 6,
        "title": "수련 연못",
        "artist": "클로드 모네",
        "style": "인상주의",
        "mood": "평화로운",
        "duration": 20,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Claude_Monet_-_Water_Lilies_-_1919.jpg/1280px-Claude_Monet_-_Water_Lilies_-_1919.jpg",
        "description": "지베르니 정원의 일본식 다리와 수련 연못의 반사된 빛을 감성적으로 그린 작품입니다.",
        "point": "물에 비친 하늘과 연못 표면 수련의 지평선 없는 배치를 감상해 보세요."
    },
    {
        "id": 7,
        "title": "아테네 학당",
        "artist": "라파엘로 산치오",
        "style": "르네상스",
        "mood": "웅장한/어두운",
        "duration": 35,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg/1280px-%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg",
        "description": "고대 철학자들과 학자들이 한자리에 모여 논쟁하는 이상적인 아카데미를 구현했습니다.",
        "point": "중앙의 플라톤과 아리스토텔레스의 손짓과 완벽한 투시도법 구도를 확인해 보세요."
    },
    {
        "id": 8,
        "title": "키스",
        "artist": "구스타프 클림트",
        "style": "상징주의",
        "mood": "화려한",
        "duration": 25,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg/1280px-The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg",
        "description": "금박을 가득 사용하여 연인 간의 황홀하고 영원한 사랑을 표현한 명작입니다.",
        "point": "화려한 기하학적 문양과 기묘하면서도 매혹적인 분위기에 매료되어 보세요."
    }
]

# 대표 명화 (필터링 결과가 없을 때 예외 처리용)
DEFAULT_ARTWORK = {
    "title": "모나리자",
    "artist": "레오나르도 다 빈치",
    "style": "르네상스",
    "mood": "신비로운",
    "duration": 20,
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/1280px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
    "description": "세계에서 가장 유명한 초상화로, 알 수 없는 신비로운 미소로 대중을 매료시키는 명작입니다.",
    "point": "스푸마토 기법을 사용한 부드러운 윤곽선과 시선에 따라 달라지는 미소를 감상하세요."
}

# -----------------------------------------------------------------------------
# 2. 사이드바 - 사용자 취향 및 관람 환경 입력
# -----------------------------------------------------------------------------
st.sidebar.title("🎨 도슨트 설정")
st.sidebar.write("맞춤형 전시 동선을 위해 취향을 알려주세요.")

# 필터 옵션 추출 (전체 선택 옵션 포함)
styles = ["전체"] + sorted(list(set(art["style"] for art in ARTWORKS_DB)))
moods = ["전체"] + sorted(list(set(art["mood"] for art in ARTWORKS_DB)))

# 입력 컴포넌트
selected_style = st.sidebar.selectbox("선호 미술 사조", styles)
selected_mood = st.sidebar.radio("원하는 분위기", moods)
max_time = st.sidebar.slider("총 관람 가능 시간 (분)", min_value=15, max_value=120, value=60, step=5)

# -----------------------------------------------------------------------------
# 3. 큐레이팅 추천 알고리즘 (필터링 & 시간 배분)
# -----------------------------------------------------------------------------
filtered_artworks = []
accumulated_time = 0

for art in ARTWORKS_DB:
    # 1) 사조 및 분위기 조건 체크
    style_match = (selected_style == "전체") or (art["style"] == selected_style)
    mood_match = (selected_mood == "전체") or (art["mood"] == selected_mood)
    
    if style_match and mood_match:
        # 2) 누적 시간이 관람 가능 시간을 초과하지 않도록 선별
        if accumulated_time + art["duration"] <= max_time:
            filtered_artworks.append(art)
            accumulated_time += art["duration"]

# -----------------------------------------------------------------------------
# 4. 결과 출력 및 예외 처리
# -----------------------------------------------------------------------------
st.title("🏛️ 맞춤형 전시회 큐레이팅 도슨트")
st.markdown("---")

# 예외 처리: 조건에 만족하는 작품이 전혀 없을 경우
if not filtered_artworks:
    st.warning("⚠️ 입력하신 조건에 들어맞는 작품 조합을 찾지 못했습니다. 대신 루브르 박물관의 대표 명화를 안내해 드립니다.")
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        st.image(DEFAULT_ARTWORK["image_url"], caption=DEFAULT_ARTWORK["title"], use_container_width=True)
    with col_info:
        st.subheader(f"{DEFAULT_ARTWORK['title']} ({DEFAULT_ARTWORK['artist']})")
        st.write(f"**사조:** {DEFAULT_ARTWORK['style']} | **소요 시간:** {DEFAULT_ARTWORK['duration']}분")
        st.info(f"**해설:** {DEFAULT_ARTWORK['description']}")
        st.success(f"**감상 포인트:** {DEFAULT_ARTWORK['point']}")

else:
    st.subheader(f"✨ 추천 동선 (총 {len(filtered_artworks)}개 작품 / 소요 시간: 약 {accumulated_time}분)")
    st.caption("선택하신 취향 및 가능 시간에 맞춰 도슨트 코스를 구성했습니다.")
    st.write("")

    # 작품 카드 출력 (2개 컬럼씩 그리드 형태 배치)
    for i in range(0, len(filtered_artworks), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(filtered_artworks):
                art = filtered_artworks[i + j]
                with cols[j]:
                    with st.container(border=True):
                        try:
                            st.image(art["image_url"], use_container_width=True)
                        except Exception:
                            st.caption("🖼️ 이미지 불러오기 오류")
                        
                        st.subheader(art["title"])
                        st.write(f"**작가:** {art['artist']} | **사조:** {art['style']}")
                        st.write(f"**분위기:** {art['mood']} | **관람 시간:** {art['duration']}분")
                        st.divider()
                        st.write(f"📖 **작품 해설**\n{art['description']}")
                        st.info(f"💡 **감상 포인트**\n{art['point']}")

    # -----------------------------------------------------------------------------
    # 5. 갤러리 도록 요약 및 CSV 저장
    # -----------------------------------------------------------------------------
    st.markdown("---")
    st.subheader("📋 관람 도록 요약본")

    # DataFrame 생성
    df_catalog = pd.DataFrame(filtered_artworks)[["title", "artist", "style", "mood", "duration", "description"]]
    df_catalog.columns = ["작품명", "작가", "미술 사조", "분위기", "관람 시간(분)", "해설"]
    
    st.dataframe(df_catalog, use_container_width=True)

    # 한글 깨짐 방지를 위한 utf-8-sig 인코딩 CSV 변환
    csv_data = df_catalog.to_csv(index=False).encode('utf-8-sig')

    st.download_button(
        label="📥 도록 다운로드 (CSV)",
        data=csv_data,
        file_name="my_art_exhibition_catalog.csv",
        mime="text/csv"
    )
