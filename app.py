from flask import Flask, render_template, request, jsonify
from google import genai

# ============================================================
# GEMINI API KEY
# ============================================================

API_KEY = "AQ.Ab8RN6IaBrVfJsQJ-YRmbCpKShPUYFhaOFdfcXbpj_UcXNz95w"

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

# ============================================================
# TOOL 1 — ADD NUMBERS
# ============================================================

def add_numbers(a: float, b: float) -> dict:

    print("\n🔧 TOOL CALLED: add_numbers")

    result = a + b

    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }


# ============================================================
# TOOL 2 — PRODUCT INFO
# ============================================================

def product_info(product_name: str) -> dict:

    print(f"\n🔧 TOOL CALLED: product_info ({product_name})")

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


# ============================================================
# REGISTER TOOLS
# ============================================================

tools = [
    add_numbers,
    product_info
]

# ============================================================
# CHAT SESSION
# ============================================================

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

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_api():

    user_message = request.json.get("message")

    try:

        response = chat.send_message(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        })


# ============================================================
# START APP
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)