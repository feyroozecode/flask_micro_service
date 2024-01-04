from flask import Flask, jsonify
import requests

app = Flask(__name__)

random_service_url = "http://127.0.0.1:8081/generate"

# calling the random nbr generator micro_service
def call_random_microservice():
    response = requests.get(random_service_url)

    return response.json().get("random_number")

@app.route("/check", methods=['GET'])
def check_even_odd():
    random_number = call_random_microservice()
    result = "even" if random_number % 2 == 0 else "odd"

    return jsonify({"random_number": random_number , "result": result })

if __name__ == "__main__":
   app.run(port=8082)
