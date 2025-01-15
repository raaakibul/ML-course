from flask import Flask, render_template, request
from model import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat_response():
    user_message = request.form["message"]
    response = get_response(user_message)
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)
