from flask import Flask, jsonify
from app.utils import greet_user

app = Flask(__name__)

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet_user(user))

