import streamlit as st

# 웹 페이지 제목 설정
st.title("💰 결제 및 시간 계산기 앱")
st.markdown("가격/비용 비교와 거리/속력에 따른 시간 계산을 제공합니다.")

# 시각적인 구분선
st.divider()

# --- 1. 결제 시스템 섹션 ---
st.header("1. 결제 시스템")

# 숫자 입력을 위한 number_input 위젯 사용 (기본값 0)
price = st.number_input("가격을 입력해주세요 (원)", min_value=0, value=0, step=1000)
total_cost = st.number_input("총 보유 비용(잔액)을 입력해주세요 (원)", min_value=0, value=0, step=1000)

# 결제 로직 실행 버튼
if st.button("결제하기"):
    if price <= total_cost:
        st.success("🎉 결제가 완료되었습니다!")
    else:
        st.error("❌ 잔액이 부족합니다.")

st.divider()

# --- 2. 이동 시간 계산기 섹션 ---
st.header("2. 이동 시간 계산기")

# 거리와 속력 입력 (정수형 변환을 위해 step=1 설정)
distance_km = st.number_input("거리(km)를 입력해주세요", min_value=0, value=0, step=1)
speed_ms = st.number_input("속력(m/s)을 입력해주세요", min_value=0, value=0, step=1)

if st.button("시간 계산하기"):
    if speed_ms == 0:
        st.warning("⚠️ 속력은 0이 될 수 없습니다. 올바른 속력을 입력해주세요.")
    else:
        # 단위를 맞추기 위한 계산 (km를 m로 변환: 거리 * 1000)
        distance_m = distance_km * 1000
        time_seconds = distance_m / speed_ms
        
        # 보기 좋게 분/초 등으로 환산 처리 (선택 사항)
        time_minutes = time_seconds / 60
        
        st.subheader("⏱️ 걸리는 시간 결과")
        st.metric(label="소요 시간 (초)", value=f"{time_seconds:,.2f} 초")
        st.info(f"💡 대략 **{time_minutes:.1f}분**이 소요됩니다. (단위: $m/s$ 기준 계산 완료)")
