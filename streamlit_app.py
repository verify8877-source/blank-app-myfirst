import random

import streamlit as st

st.set_page_config(page_title="영어 단어 게임", page_icon="📚", layout="centered")

st.title("📚 영어 단어 뜻 맞추기")
st.markdown("영어 단어가 화면 상단에 나타나면, 한글 뜻을 입력해 보세요.")

WORDS = [
    ("apple", "사과"),
    ("book", "책"),
    ("river", "강"),
    ("sun", "태양"),
    ("computer", "컴퓨터"),
    ("friend", "친구"),
    ("teacher", "선생님"),
    ("house", "집"),
    ("music", "음악"),
    ("travel", "여행"),
]

if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(WORDS)
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "last_result" not in st.session_state:
    st.session_state.last_result = ""


def next_question():
    st.session_state.current_word = random.choice(WORDS)
    st.session_state.show_result = False
    st.session_state.last_result = ""
    st.session_state.user_answer = ""


def check_answer():
    st.session_state.total += 1
    user_answer = st.session_state.user_answer.strip()
    correct_answer = st.session_state.current_word[1]
    if user_answer == correct_answer:
        st.session_state.score += 1
        st.session_state.last_result = "정답입니다! 🎉"
        st.session_state.show_result = True
    else:
        st.session_state.last_result = f"아쉽습니다. 정답은 '{correct_answer}'입니다."
        st.session_state.show_result = True


col1, col2 = st.columns([2, 1])
with col1:
    st.metric("점수", f"{st.session_state.score}/{st.session_state.total}")
with col2:
    if st.button("새 게임", use_container_width=True):
        st.session_state.score = 0
        st.session_state.total = 0
        next_question()

word, meaning = st.session_state.current_word
st.markdown(
    f"<div style='text-align:center; font-size:48px; font-weight:bold; margin: 20px 0;'>{word}</div>",
    unsafe_allow_html=True,
)

st.text_input("한글 뜻을 입력하세요", key="user_answer", placeholder="예: 사과")

col3, col4 = st.columns(2)
with col3:
    st.button("정답 확인", on_click=check_answer, use_container_width=True)
with col4:
    st.button("다음 문제", on_click=next_question, use_container_width=True)

if st.session_state.show_result:
    if st.session_state.last_result.startswith("정답"):
        st.success(st.session_state.last_result)
    else:
        st.error(st.session_state.last_result)

st.caption("Tip: 뜻을 입력한 뒤 정답 확인을 누르면 결과가 나옵니다.")
