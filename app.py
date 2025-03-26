from flask import Flask, jsonify, request
import requests

# Services
from services import app_services

app = Flask(__name__)

def get_data():
    response = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow", timeout=4000)

    if (response.status_code == 200):
        return response.json()

    return "Unable to retrieve data!"

# http://127.0.0.1:3000/
@app.route("/")
def home():
    return jsonify({
        "msn": "It Works"
    })

# Task 1) http://127.0.0.1:3000/get-answered-responses
@app.route("/get-answered-responses")
def get_answered_responses():
    try:
        data = get_data()
        answered_responses, no_answered_responses = app_services.get_answered_responses(data)

        return jsonify({
            "msn": "Ok",
            "answered_responses": answered_responses,
            "no_answered_responses": no_answered_responses
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 2) http://127.0.0.1:3000/get-answer-highest-reputation
@app.route("/get-answer-highest-reputation")
def get_answer_highest_reputation():
    try:
        data = get_data()
        res = app_services.get_answer_highest_reputation(data)

        return jsonify({
            "msn": "Ok",
            "reputation": res["reputation"],
            "title": res["title"],
            "display_name": res["display_name"],
            "link": res["link"]
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 3) http://127.0.0.1:3000/get-answer-fewest-views
@app.route("/get-answer-fewest-views")
def get_answer_fewest_views():
    try:
        data = get_data()
        res = app_services.get_answer_fewest_views(data)

        return jsonify({
            "msn": "Ok",
            "question_id": res["question_id"],
            "title": res["title"],
            "viewCount": res["view_count"],
            "displayName": res["display_name"],
            "isAnswered": res["is_answered"],
            "link": res["link"]
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 4) http://127.0.0.1:3000/get-oldest-and-newest-answer
@app.route("/get-oldest-and-newest-answer")
def get_oldest_and_newest_answer():
    try:
        data = get_data()
        oldest_answer, newest_answer = app_services.get_oldest_and_newest_answer(data)

        return jsonify({
            "msn": "Ok",
            "oldestAnswer": {
                "title": oldest_answer["title"],
                "creationDate": oldest_answer["creation_date"],
                "displayName": oldest_answer["display_name"],
                "link": oldest_answer["link"],
            },
            "newestAnswer": {
                "title": newest_answer["title"],
                "creationDate": newest_answer["creation_date"],
                "displayName": newest_answer["display_name"],
                "link": newest_answer["link"],
            },
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

if __name__ == "__main__":
    app.run(debug=True, port=3000)
