import streamlit as st

st.title("할 짓 추천하기!")

menu = st.sidebar.selectbox("메뉴", ["홈", "설정"])

user_setting = ""

if menu == "홈":
    st.header("홈 페이지")
    st.write("이곳은 앱의 홈 페이지입니다.")




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