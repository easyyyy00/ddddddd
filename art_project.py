import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 명화 데이터베이스 (미술관/전시실 위치 데이터 추가)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="디지털 미술관 도슨트",
    page_icon="🎨",
    layout="wide"
)

# 소장 미술관 및 위치 정보가 포함된 명화 DB
ARTWORKS_DB = [
    {
        "id": 1,
        "title": "별이 빛나는 밤",
        "artist": "빈센트 반 고흐",
        "style": "후기 인상주의",
        "mood": "몽환적인",
        "duration": 20,
        "museum": "뉴욕 현대미술관 (MoMA)",
        "location": "5층 502호 전시실",
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
        "museum": "마르모탕 모네 미술관 (파리)",
        "location": "지하 1층 인상파 전용관",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg/1280px-Claude_Monet%2C_Impression%2C_soleil_levant.jpg",
        "description": "인상파라는 이름을 만들어낸 역사적인 작품으로, 붉은 태양과 항구의 안개를 담았습니다.",
        "point": "빛의 변화에 따라 시시각각 달라지는 찰나의 순간을 느껴보세요."
    },
    {
        "id": 3,
        "title": "기억의 지속",
        "artist": "살바도르 달리",
        "style": "초현실주의",
        "mood": "몽환적인",
        "duration": 25,
        "museum": "뉴욕 현대미술관 (MoMA)",
        "location": "5층 517호 전시실",
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
        "museum": "노르웨이 국립미술관 (오슬로)",
        "location": "2층 문크 전용관",
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
        "museum": "우피치 미술관 (피렌체)",
        "location": "2층 10-14번 보티첼리 관",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/1280px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg",
        "description": "바다 조개껍데기 위에서 탄생한 비너스의 신화적 순간을 우아한 선으로 그린 명화입니다.",
        "point": "비너스의 우아한 포즈와 화면 전반에 흐르는 신화적 아우라를 관찰해 보세요."
    },
    {
        "id": 6,
        "title": "수련 연못",
        "artist": "클로드 모네",
        "style": "인
