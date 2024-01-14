from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/random_num', methods=['GET'])
def random_num():
    random_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    return jsonify({'value': random_number})

if __name__ == '__main__':
    app.run(debug=True)
