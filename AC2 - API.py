from flask import Flask, jsonify

app = Flask(__name__)

DATA = {"Thing1": "One", "Thing2": "Two", "Thing3": "three"}

@app.route('/', methods=["GET"])
def listar_dados():
    return jsonify(DATA), 200

if __name__ == "__main__":
    app.run()