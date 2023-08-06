from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)
messages = []
users = []


def store_message(user, message):
    messages.append({
        "user": user,
        "message": message,
        "time": datetime.now().strftime("%X")
    })


def format_messages():
    def format_message(message: dict):
        user, message, time = message.values()
        return f"{time} {user}: {message}"
    return "\n".join(map(format_message, messages))


def format_users():
    return "\n".join(users)


def valid_user(user):
    return user in users


def clear_messages():
    with open("messages.dat", mode="a+", encoding="utf-8") as file:
        file.write(format_messages() + "\n")
    messages.clear()


@app.route("/")
def index():
    return "Hi."


@app.route("/messages")
def get_messages():
    if "json" in request.args:
        return Response(json.dumps(messages), mimetype="application/json")
    else:
        return Response(format_messages(), mimetype="text/plain")


@app.route("/users")
def get_users():
    if "json" in request.args:
        return json.dumps(users)
    else:
        return format_users()


@app.route("/register", methods=["POST"])
def post_register():
    if "user" not in request.form:
        return Response("Missing data: 'user'", 400)
    user = request.form["user"]
    if valid_user(user):
        return Response(f"User: {repr(user)} is already registered.", 400)
    users.append(user)
    return "Registered succesfully."


@app.route("/send", methods=["POST"])
def post_send():
    if "user" not in request.form:
        return Response("Missing data: 'user'", 400)
    if "message" not in request.form:
        return Response("Missing data: 'message'", 400)
    user = request.form["user"]
    if not valid_user(user):
        return Response(f"User: {repr(user)} is not registered.")

    store_message(request.form["user"], request.form["message"])
    return "Message sent successfully"


@app.route("/clear")
def get_clear():
    password = request.args.get("p")
    correct_password = "t"
    if password is None or password != correct_password:
        return Response("Invalid password", 400)
    clear_messages()
    return "Cleared messages"


if __name__ == "__main__":
    app.run(debug=True)
