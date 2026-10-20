from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")

def unsafe_calculator(expression):
    return eval(expression)
