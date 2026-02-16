import streamlit as st
import requests
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="실시간 경제 대시보드", layout="wide")

st.title("💰 실시간 환율 & 코인 대시보드")
st.markdown("2026년 실시간 데이터를 시각화합니다.")

# 데이터 가져오는 함수
def get_data():
    # 환율 데이터 (USD to KRW)
    ex_url = "https://api.exchangerate-api.com/v4/latest/USD"
    ex_rate = requests.get(ex_url).json()['rates']['KRW']
    
    # 비트코인 데이터 (Upbit)
    btc_url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    btc_price = requests.get(btc_url).json()[0]['trade_price']
    
    return ex_rate, btc_price

ex_rate, btc_price = get_data()

# 화면 레이아웃 나누기
col1, col2 = st.columns(2)

with col1:
    st.metric(label="현재 환율 (USD/KRW)", value=f"{ex_rate:,.2f} 원")
    st.info("달러 대비 원화 환율입니다.")

with col2:
    st.metric(label="비트코인 (BTC/KRW)", value=f"{btc_price:,.0f} 원")
    st.warning("국내 거래소 실시간 가격입니다.")

# 간단한 입력 계산기 기능
st.divider()
st.subheader("🧮 간편 계산기")
usd_input = st.number_input("계산할 달러($)를 입력하세요", min_value=0.0)
if usd_input > 0:
    st.success(f"{usd_input:,.2f} 달러는 현재 {usd_input * ex_rate:,.0f} 원입니다.")

# 새로고침 버튼
if st.button('데이터 새로고침'):
    st.rerun()

    #터미널에 python -m streamlit run app.py 입력하기
    ##터미널에 입력하는 이유