import pandas as pd
import streamlit as st

# 1. 앱 제목 설정
st.title("📚 공부 습관 대시보드")

# 2. 데이터 불러오기 및 열 이름 공백 정리
df = pd.read_csv("study.csv")
df.columns = df.columns.str.strip()  # 열 이름에 포함된 공백 제거

# 3. 상단에 학생 수, 평균 점수, 평균 공부시간을 한 줄(3개 열)로 표시
col1, col2, col3 = st.columns(3)
col1.metric("총 학생 수", f"{len(df)}명")
col2.metric("평균 점수", f"{df['점수'].mean():.1f}점")
col3.metric("평균 공부시간", f"{df['공부시간'].mean():.1f}시간")

st.divider()

# 4. 최소 공부시간 슬라이더 필터 생성
min_study = st.slider(
    "최소 공부시간을 선택하세요",
    float(df["공부시간"].min()),
    float(df["공부시간"].max()),
    0.0,
)

# 선택한 최소 공부시간 이상인 학생들만 필터링
filtered_df = df[df["공부시간"] >= min_study]
st.write(f"조건에 맞는 학생 수: **{len(filtered_df)}명**")

# 5. 시각화 (기본 차트 함수 활용)
st.subheader("📊 공부시간 vs 점수 산점도")
st.scatter_chart(filtered_df, x="공부시간", y="점수")

st.subheader("📈 학생별 점수 막대 그래프")
st.bar_chart(filtered_df.set_index("학생ID")["점수"])