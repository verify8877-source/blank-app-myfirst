import streamlit as st

st.set_page_config(page_title="Streamlit 요소 예시", page_icon="✨", layout="wide")

st.title("🌟 Streamlit 요소 예시")
st.markdown("Streamlit 앱에서 자주 쓰는 요소들을 한 화면에서 확인해 보세요.")

with st.sidebar:
    st.header("사이드바")
    st.checkbox("사이드바 체크박스", value=True)
    st.slider("사이드바 슬라이더", 0, 100, 50)

st.subheader("1. 기본 입력 요소")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("이름", placeholder="홍길동")
    bio = st.text_area("한 줄 소개", "Streamlit으로 멋진 앱을 만들고 있어요.")
    age = st.number_input("나이", min_value=0, max_value=120, value=25)

with col2:
    mood = st.radio("오늘 기분", ["좋음", "보통", "나쁨"], horizontal=True)
    favorite = st.selectbox("좋아하는 언어", ["Python", "JavaScript", "Go", "Rust"])
    tags = st.multiselect("관심 기술", ["Streamlit", "FastAPI", "Docker", "PyTorch"])

st.button("환영 메시지 보기", type="primary")
if st.button("환영 메시지 보기"):
    st.success(f"{name or '방문자'}님, {favorite}를 좋아하시네요!")

st.divider()
st.subheader("2. 상태 표시와 메시지")
col3, col4, col5 = st.columns(3)
with col3:
    st.info("정보 메시지입니다.")
with col4:
    st.warning("주의 메시지입니다.")
with col5:
    st.error("에러 메시지입니다.")

st.divider()
st.subheader("3. 데이터와 차트")
chart_data = [3, 2, 4, 3, 5, 4]
st.line_chart(chart_data)

st.dataframe(
    {
        "이름": [name or "익명", "민수", "지연"],
        "나이": [age, 30, 28],
        "기분": [mood, "좋음", "보통"],
    }
)

st.metric("현재 선택한 항목", favorite, delta="좋아요")

st.divider()
st.subheader("4. 레이아웃과 확장")
with st.expander("추가 정보 보기"):
    st.write("이 영역은 접었다가 펼쳐서 볼 수 있는 공간입니다.")
    st.code("st.button('클릭')")

with st.container():
    st.caption("아래는 탭으로 구분한 예시입니다.")
    tab1, tab2 = st.tabs(["텍스트", "JSON"])
    with tab1:
        st.write("텍스트 요소를 보여주는 탭입니다.")
    with tab2:
        st.json({"name": name or "익명", "favorite": favorite, "tags": tags})
