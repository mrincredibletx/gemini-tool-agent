import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)


def add_numbers(a: float, b: float) -> dict:
    result = a + b
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }


def product_info(product_name: str) -> dict:
    products = {
        "iphone 15": {
            "name": "iPhone 15",
            "category": "Smartphone",
            "price": 69999,
            "currency": "INR"
        },
        "samsung s24": {
            "name": "Samsung Galaxy S24",
            "category": "Smartphone",
            "price": 74999,
            "currency": "INR"
        },
        "macbook air": {
            "name": "MacBook Air",
            "category": "Laptop",
            "price": 99999,
            "currency": "INR"
        }
    }

    product = products.get(product_name.lower())

    if product:
        return product

    return {
        "error": f"Product '{product_name}' not found."
    }


tools = [add_numbers, product_info]

chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "tools": tools,
        "system_instruction": """
        You are a helpful AI assistant.

        Rules:
        1. Use add_numbers tool when user wants calculations.
        2. Use product_info tool when user asks product details.
        3. For everything else answer normally.
        4. Be concise and friendly.
        """
    }
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."}), 400

    try:
        response = chat.send_message(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "reply": "Something went wrong while processing your request."
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
