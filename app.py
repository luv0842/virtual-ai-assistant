from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
import requests

# ---------------- MongoDB ----------------
mongo_client = MongoClient("mongodb://localhost:27017/")

db = mongo_client["ai_assistant"]
collection = db["chat_history"]

print("MongoDB Connected Successfully!")

# ---------------- Flask ----------------
app = Flask(__name__)


def get_response(user_input):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": user_input,
                "stream": False
            },
            timeout=60
        )

        # Raise exception for bad HTTP status
        response.raise_for_status()

        data = response.json()

        # Get response safely
        bot_reply = data.get("response", "No response received from model.")

        # Save chat in MongoDB
        collection.insert_one({
            "user_message": user_input,
            "bot_reply": bot_reply,
            "time": datetime.utcnow()
        })

        return bot_reply

    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "Error: Request timed out."

    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"

    except Exception as e:
        return f"Unexpected Error: {e}"


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        if user_input:
            response = get_response(user_input)
        else:
            response = "Please enter a message."

    return render_template(
        "index.html",
        response=response,
        user_input=user_input
    )


if __name__ == "__main__":
    app.run(debug=True)