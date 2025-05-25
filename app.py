
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ SatoshiJet Backend is running!"

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    wallet = data.get("wallet")
    amount = data.get("amount")
    return jsonify({"message": f"Deposit request received from {wallet} for {amount} TRX"})

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    wallet = data.get("wallet")
    amount = data.get("amount")
    if wallet and amount:
        return jsonify({"message": f"Withdrawal request sent to admin for {amount} TRX from {wallet}"})
    return jsonify({"error": "Missing wallet or amount"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
