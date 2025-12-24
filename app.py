from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS # type: ignore

from ollama_brain import ask_ollama
from executor import execute_plan

app = Flask(__name__)
CORS(app)

print("🔥 Zen AutoGPT Agent starting...")

@app.route("/")
def home():
    return render_template("voice.html")
@app.route("/agent", methods=["POST"])
def agent():
    user_text = request.json.get("text", "")
    user_text_lower = user_text.lower()

    print(f"🧠 User said: {user_text}")

    plan = ask_ollama(user_text)
    print("📜 Raw Plan:", plan)

    # Simply pass through all actions
    # The executor will handle open_application with fallback to website
    # And handle open_website directly
    
    print("🧹 Final Plan:", plan)

    result = execute_plan(plan)

    return jsonify({
        "reply": result
    })

if __name__ == "__main__":
    app.run(debug=True)

