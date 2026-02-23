import tkinter as tk
import requests
from tkinter import font as tkfont

# --- 디자인 설정 (색상 및 폰트) ---
BG_COLOR = "#F0F4F8"   # 앱 배경색 (밝은 하늘색 톤)
TEXT_COLOR = "#333333" # 기본 글자색 (진한 회색)
ACCENT_COLOR = "#4A90E2" # 강조색 (파란색, 버튼 등)

# 폰트 설정 (가독성 좋은 Arial/Helvetica 계열 사용)
FONT_CITY = ("Helvetica", 24, "bold")
FONT_TEMP = ("Helvetica", 48, "bold")
FONT_DESC = ("Helvetica", 16)
FONT_DETAIL = ("Helvetica", 12)
FONT_EMOJI = ("Apple Color Emoji", 80) # 윈도우는 "Segoe UI Emoji" 권장

def get_weather(event=None):
    city_name = city_entry.get().strip()
    
    if city_name.lower() == 'n':
        window.destroy()
        return

    # 초기화 및 유효성 검사
    reset_labels()
    if not city_name:
        city_label.config(text="도시 이름을 입력해주세요")
        return

    api_key = "725b65b4c73314d17ea6f1a03f422080"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric', 'lang': 'kr'}

    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 404:
            city_label.config(text=f"❌ 도시를 찾을 수 없습니다.")
            desc_label.config(text=f"'{city_name}' 스펠링을 확인해주세요.")
            return
            
        response.raise_for_status()
        weather_data = response.json()

        # 데이터 추출
        temp = round(weather_data['main']['temp']) # 온도는 반올림해서 깔끔하게
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        weather_main = weather_data['weather'][0]['main']
        city_display_name = weather_data['name'] # API에서 주는 공식 도시 이름

        # 이모지 매핑
        emoji_dict = {
            'Clear': '☀️', 'Clouds': '☁️', 'Rain': '🌧️', 'Drizzle': '🌦️',
            'Thunderstorm': '⛈️', 'Snow': '❄️', 'Mist': '🌫️', 'Fog': '🌫️', 'Haze': '🌫️'
        }
        weather_emoji = emoji_dict.get(weather_main, '🌡️')

        # --- 결과 화면 업데이트 (각 라벨별로 따로 설정) ---
        city_label.config(text=city_display_name)
        emoji_label.config(text=weather_emoji)
        temp_label.config(text=f"{temp}°")
        desc_label.config(text=description)
        detail_label.config(text=f"습도: {humidity}%")

    except requests.exceptions.RequestException:
         city_label.config(text="인터넷 연결 오류")
         desc_label.config(text="네트워크 상태를 확인해주세요.")

def reset_labels():
    """검색 시작 시 기존 결과 지우기"""
    city_label.config(text="")
    emoji_label.config(text="")
    temp_label.config(text="")
    desc_label.config(text="")
    detail_label.config(text="")

# --- GUI 구성 ---
window = tk.Tk()
window.title("My Weather App")
window.geometry("360x550") # 스마트폰 비율처럼 세로로 길게
window.configure(bg=BG_COLOR) # 전체 배경색 설정

# 1. 상단 검색 영역 (Frame으로 묶어서 관리)
search_frame = tk.Frame(window, bg=BG_COLOR, pady=20)
search_frame.pack(fill="x")

city_entry = tk.Entry(search_frame, width=20, font=("Helvetica", 14), bd=0, highlightthickness=1, highlightcolor=ACCENT_COLOR)
city_entry.pack(pady=5, ipady=5) # ipady로 입력창 내부 높이 키움
city_entry.bind('<Return>', get_weather)
# 시작 안내 문구 placeholder처럼 넣기
city_entry.insert(0, "도시 입력 (예: Seoul)") 
city_entry.bind("<FocusIn>", lambda args: city_entry.delete('0', 'end')) # 클릭하면 안내 문구 삭제

search_button = tk.Button(search_frame, text="검색", command=get_weather, bg="white", fg=ACCENT_COLOR, font=("Helvetica", 12, "bold"), relief="flat", padx=10)
search_button.pack(pady=5)

# 2. 메인 결과 영역
content_frame = tk.Frame(window, bg=BG_COLOR)
content_frame.pack(expand=True)

# 도시 이름 (크고 진하게)
city_label = tk.Label(content_frame, text="오늘의 날씨는?", font=FONT_CITY, bg=BG_COLOR, fg=TEXT_COLOR)
city_label.pack(pady=(20, 10))

# 이모지 (가장 크게)
emoji_label = tk.Label(content_frame, text="🌍", font=FONT_EMOJI, bg=BG_COLOR)
emoji_label.pack()

# 온도 (매우 크게 강조)import tkinter as tk
import requests
from tkinter import font as tkfont

# --- 디자인 설정 (색상 및 폰트) ---
BG_COLOR = "#F0F4F8"   # 앱 배경색 (밝은 하늘색 톤)
TEXT_COLOR = "#333333" # 기본 글자색 (진한 회색)
ACCENT_COLOR = "#4A90E2" # 강조색 (파란색, 버튼 등)

# 폰트 설정 (가독성 좋은 Arial/Helvetica 계열 사용)
FONT_CITY = ("Helvetica", 24, "bold")
FONT_TEMP = ("Helvetica", 48, "bold")
FONT_DESC = ("Helvetica", 16)
FONT_DETAIL = ("Helvetica", 12)
FONT_EMOJI = ("Apple Color Emoji", 80) # 윈도우는 "Segoe UI Emoji" 권장

def get_weather(event=None):
    city_name = city_entry.get().strip()
    
    if city_name.lower() == 'n':
        window.destroy()
        return

    # 초기화 및 유효성 검사
    reset_labels()
    if not city_name:
        city_label.config(text="도시 이름을 입력해주세요")
        return

    api_key = "여기에_발급받은_API_키를_입력하세요"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city_name, 'appid': api_key, 'units': 'metric', 'lang': 'kr'}

    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 404:
            city_label.config(text=f"❌ 도시를 찾을 수 없습니다.")
            desc_label.config(text=f"'{city_name}' 스펠링을 확인해주세요.")
            return
            
        response.raise_for_status()
        weather_data = response.json()

        # 데이터 추출
        temp = round(weather_data['main']['temp']) # 온도는 반올림해서 깔끔하게
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        weather_main = weather_data['weather'][0]['main']
        city_display_name = weather_data['name'] # API에서 주는 공식 도시 이름

        # 이모지 매핑
        emoji_dict = {
            'Clear': '☀️', 'Clouds': '☁️', 'Rain': '🌧️', 'Drizzle': '🌦️',
            'Thunderstorm': '⛈️', 'Snow': '❄️', 'Mist': '🌫️', 'Fog': '🌫️', 'Haze': '🌫️'
        }
        weather_emoji = emoji_dict.get(weather_main, '🌡️')

        # --- 결과 화면 업데이트 (각 라벨별로 따로 설정) ---
        city_label.config(text=city_display_name)
        emoji_label.config(text=weather_emoji)
        temp_label.config(text=f"{temp}°")
        desc_label.config(text=description)
        detail_label.config(text=f"습도: {humidity}%")

    except requests.exceptions.RequestException:
         city_label.config(text="인터넷 연결 오류")
         desc_label.config(text="네트워크 상태를 확인해주세요.")

def reset_labels():
    """검색 시작 시 기존 결과 지우기"""
    city_label.config(text="")
    emoji_label.config(text="")
    temp_label.config(text="")
    desc_label.config(text="")
    detail_label.config(text="")

# --- GUI 구성 ---
window = tk.Tk()
window.title("My Weather App")
window.geometry("360x550") # 스마트폰 비율처럼 세로로 길게
window.configure(bg=BG_COLOR) # 전체 배경색 설정

# 1. 상단 검색 영역 (Frame으로 묶어서 관리)
search_frame = tk.Frame(window, bg=BG_COLOR, pady=20)
search_frame.pack(fill="x")

city_entry = tk.Entry(search_frame, width=20, font=("Helvetica", 14), bd=0, highlightthickness=1, highlightcolor=ACCENT_COLOR)
city_entry.pack(pady=5, ipady=5) # ipady로 입력창 내부 높이 키움
city_entry.bind('<Return>', get_weather)
# 시작 안내 문구 placeholder처럼 넣기
city_entry.insert(0, "도시 입력 (예: Seoul)") 
city_entry.bind("<FocusIn>", lambda args: city_entry.delete('0', 'end')) # 클릭하면 안내 문구 삭제

search_button = tk.Button(search_frame, text="검색", command=get_weather, bg="white", fg=ACCENT_COLOR, font=("Helvetica", 12, "bold"), relief="flat", padx=10)
search_button.pack(pady=5)

# 2. 메인 결과 영역
content_frame = tk.Frame(window, bg=BG_COLOR)
content_frame.pack(expand=True)

# 도시 이름 (크고 진하게)
city_label = tk.Label(content_frame, text="오늘의 날씨는?", font=FONT_CITY, bg=BG_COLOR, fg=TEXT_COLOR)
city_label.pack(pady=(20, 10))

# 이모지 (가장 크게)
emoji_label = tk.Label(content_frame, text="🌍", font=FONT_EMOJI, bg=BG_COLOR)
emoji_label.pack()

# 온도 (매우 크게 강조)
temp_label = tk.Label(content_frame, text="", font=FONT_TEMP, bg=BG_COLOR, fg=TEXT_COLOR)
temp_label.pack()

# 날씨 설명 (중간 크기)
desc_label = tk.Label(content_frame, text="도시를 검색해보세요", font=FONT_DESC, bg=BG_COLOR, fg=TEXT_COLOR)
desc_label.pack(pady=10)

# 습도 등 세부 정보 (작게)
detail_label = tk.Label(content_frame, text="", font=FONT_DETAIL, bg=BG_COLOR, fg="gray")
detail_label.pack(side="bottom", pady=20)

window.mainloop()
temp_label = tk.Label(content_frame, text="", font=FONT_TEMP, bg=BG_COLOR, fg=TEXT_COLOR)
temp_label.pack()

# 날씨 설명 (중간 크기)
desc_label = tk.Label(content_frame, text="도시를 검색해보세요", font=FONT_DESC, bg=BG_COLOR, fg=TEXT_COLOR)
desc_label.pack(pady=10)

# 습도 등 세부 정보 (작게)
detail_label = tk.Label(content_frame, text="", font=FONT_DETAIL, bg=BG_COLOR, fg="gray")
detail_label.pack(side="bottom", pady=20)

window.mainloop()