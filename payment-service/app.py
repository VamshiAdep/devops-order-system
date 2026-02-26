from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Health Check Endpoint (Very Important)
@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


@app.route("/process-payment", methods=["POST"])
def process_payment():
    data = request.get_json()

    if not data or "order_id" not in data:
        return jsonify({"error": "order_id required"}), 400

    order_id = data["order_id"]

    return jsonify({
        "message": f"Payment processed for order {order_id}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)