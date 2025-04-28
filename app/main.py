from flask import Flask, jsonify
from app.utils import greet_user

app = Flask(__name__)

# 🚨 Insecure endpoint — no auth or checks
@app.route("/admin-data", methods=["GET"])
def get_admin_data():
    return jsonify({"secrets": "super-sensitive-admin-info"})

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet_user(user))

    # Start the Flask app
    app.run(debug=True)