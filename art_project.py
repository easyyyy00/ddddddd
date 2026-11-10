import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 명화 데이터베이스
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
        "title": "
