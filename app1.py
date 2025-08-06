import streamlit as st
import requests
import json
import os


# API 키와 요청 헤더 설정
# API 키를 변수에 직접 할당합니다.
upstage_api_key = "up_MrJrannMiFutFLHHuSgG8USjDwzUg"

url = "https://api.upstage.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {upstage_api_key}",
    "Content-Type": "application/json"
}



st.title("할 짓 추천하기!")

menu = st.sidebar.selectbox("메뉴", ["홈", "설정"])

user_setting = ""

if menu == "홈":
    st.header("홈 페이지")
    st.write("이곳은 앱의 홈 페이지입니다.")

    data = {
    "model": "solar-1-mini-chat",  # 사용할 모델명
    "messages": [
        {"role": "user", "content": "할 짓 추천에 대한 사실에 한마디만 해줘!"}
        ]
    }

    # API 호출
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 결과 출력
    if response.status_code == 200:
        result = response.json()
        st.text(result['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code}, {response.text}")




elif menu == "설정":
    st.header("설정:")
    where = st.selectbox("당신의 위치:",["야외","실내"])
    get = st.text_input("당신이 가지고있는 것:")
    etc = st.text_area("따로 구체적 정보가 있다면 입력!:")
    

    passs = st.button("완료!")

    if passs == True:
        if etc == "" and get == "":
            user_setting = f"사용자의 위치는 {where}"
        if get == "":
            user_setting = f"사용자의 위치는 {where},사용자는 {etc}"
        if etc == "":
            user_setting = f"사용자의 위치는 {where},사용자가 가지고 있는건 {get}"
        if get != "" and etc != "":
            user_setting = f"사용자의 위치는 {where},사용자가 가지고 있는건 {get},사용자는 {etc}"

        st.text("설정이 완료되었습니다!")
        st.text(user_setting)