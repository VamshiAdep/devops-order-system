from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

def call_payment(order_id):
    for attempt in range(5):
        try:
            response = requests.post(
                "http://payment:5001/process-payment",
                json={"order_id": order_id},
                timeout=5
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2)

    return {"message": "Payment service unavailable"}


@app.route("/create-order", methods=["POST"])
def create_order():
    data = request.json
    order_id = data.get("order_id")

    payment_status = call_payment(order_id)

    return jsonify({
        "order_id": order_id,
        "payment_status": payment_status
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)