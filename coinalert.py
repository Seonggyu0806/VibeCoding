import streamlit as st
import requests
import pandas as pd
import time
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="비트코인 실시간 대시보드", layout="wide")

st.title("🚀 실시간 암호화폐 모니터링")
st.write("업비트(Upbit) API를 이용한 실시간 시세 정보입니다.")

# 데이터를 담을 빈 공간 생성
placeholder = st.empty()

# 가격 기록을 위한 리스트 (차트용)
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['time', 'BTC', 'ETH'])

def get_crypto_data():
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH"
    res = requests.get(url).json()
    return res

# 실시간 루프
while True:
    data = get_crypto_data()
    btc_price = data[0]['trade_price']
    eth_price = data[1]['trade_price']
    current_time = datetime.now().strftime('%H:%M:%S')

    # 데이터프레임 업데이트 (최근 20개 기록 유지)
    new_data = pd.DataFrame({'time': [current_time], 'BTC': [btc_price], 'ETH': [eth_price]})
    st.session_state.history = pd.concat([st.session_state.history, new_data]).tail(20)

    with placeholder.container():
        # 1. 상단 지표 (Metrics)
        col1, col2 = st.columns(2)
        col1.metric(label="Bitcoin (BTC)", value=f"{btc_price:,.0f} KRW", delta=f"{data[0]['signed_change_rate']*100:.2f}%")
        col2.metric(label="Ethereum (ETH)", value=f"{eth_price:,.0f} KRW", delta=f"{data[1]['signed_change_rate']*100:.2f}%")

        # 2. 실시간 차트
        st.subheader("실시간 가격 변동")
        chart_data = st.session_state.history.set_index('time')
        st.line_chart(chart_data)

        # 3. 상세 테이블
        st.subheader("최근 데이터 기록")
        st.table(st.session_state.history.iloc[::-1]) # 역순 표시

    time.sleep(2) # 2초마다 갱신