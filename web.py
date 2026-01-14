import streamlit as st

# ==========================================
# 모바일용 대출 계산기
# ==========================================

# 1. 제목과 설명
st.title("💰 대출 이자 계산기")
st.write("대출금과 금리를 입력하면 월 상환액을 계산해드립니다.")
st.write("Created by 감희주") # 여기에 이름을 넣으세요

# 2. 입력 받기 (숫자만 입력받도록 설정)
principal = st.number_input("대출금액 (원)", min_value=0, step=1000000, format="%d")
rate_annual = st.number_input("연 금리 (%)", min_value=0.0, step=0.1, format="%.2f")

# 3. 계산 버튼
if st.button("계산하기"):
    if principal > 0:
        rate_monthly = rate_annual / 12 / 100
        
        # 결과 보여주기
        st.success(f"대출금: {principal:,.0f}원 / 연이율: {rate_annual}%")
        st.markdown("---") # 구분선
        
        months_list = [12, 24, 36, 48, 60, 72]
        
        for months in months_list:
            if rate_monthly == 0:
                payment = principal / months
            else:
                numerator = principal * rate_monthly * ((1 + rate_monthly) ** months)
                denominator = ((1 + rate_monthly) ** months) - 1
                payment = numerator / denominator
            
            # 모바일에서 보기 좋게 큰 글씨로 출력
            st.subheader(f"{months}개월 상환 시")
            st.write(f"월 납입금: **{int(payment):,}원**")
            st.markdown("---") 
    else:
        st.error("대출금액을 입력해주세요!")