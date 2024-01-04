from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"data": "You're welcome to my server, you are on Home route of hello Service"})

@app.route("/hello", methods=["GET"])
def hello():
    msg = {"message": "Salam From Microservice Hello Service"}
    
    return jsonify(msg)

if __name__ == "__main__":
   app.run(port=8080)
