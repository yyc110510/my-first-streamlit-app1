from flask import Flask, render_template, request
import random

app = Flask(__name__)

activities = {
    "실내": [
        "넷플릭스에서 다큐멘터리 한 편 보기",
        "냉장고 털어서 남은 재료로 요리하기",
        "유튜브에서 스트레칭 루틴 따라 하기",
        "방 청소하고 인테리어 소품 재배치하기",
        "30분 동안 집중해서 독서하기 (책 아무거나)",
        "그림 그리는 앱으로 일러스트 하나 그려보기"
    ],
    "야외": [
        "근처 공원까지 산책하고 하늘 사진 찍기",
        "편의점 가서 새로운 음료수 하나 사서 마시기",
        "동네 도서관이나 서점 구경하기",
        "근처 카페 가서 커피 한 잔 마시며 노트 쓰기",
        "자전거 타고 근처 강변이나 공원 돌기",
    ],
    "혼자": [
        "ChatGPT에게 하루 일기 써달라고 요청하기",
        "마음속 고민을 노트에 써내려가기",
        "내가 좋아하는 주제로 블로그 글 하나 써보기",
        "온라인 무료 강의 1개 수강해보기 (인프런, 유튜브 등)",
        "그림판이나 캔바로 오늘의 기분 그려보기"
    ],
    "친구랑": [
        "친구한테 아무 말 없이 '잘 지내?' 라고 톡 보내기",
        "같이 공포 영화 보자고 연락해보기",
        "온라인 게임 같이 하자고 제안하기 (롤, 발로란트 등)",
        "근처 버스 정류장에서 아무 버스 타보기 (함께 모험!)",
        "친구랑 AI 이미지로 서로 캐릭터 생성해보기",
        "무작정 만나서 즉흥 브런치 먹기"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_activity = None
    selected_category = None
    if request.method == "POST":
        selected_category = request.form.get("category")
        if selected_category in activities:
            selected_activity = random.choice(activities[selected_category])
        else:
            # 랜덤 선택
            category = random.choice(list(activities.keys()))
            selected_category = category
            selected_activity = random.choice(activities[category])
    return render_template("index.html", activity=selected_activity, category=selected_category)

if __name__ == "__main__":
    app.run(debug=True)















https://docs.google.com/presentation/d/1AcmMQC9XHOX6a_Aq1bzgDcUQrX21xkkAj5o2Ow6FdZw/edit?slide=id.g373310d9267_0_0#slide=id.g373310d9267_0_0
