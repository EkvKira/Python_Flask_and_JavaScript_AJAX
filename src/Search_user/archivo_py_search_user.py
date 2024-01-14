from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    {"name": "Ramon", "age": 45, "city": "Alicante"},
    {"name": "Maria", "age": 20, "city": "Rojales"},
    {"name": "Lola", "age": 30, "city": "Valencia"}
]

@app.route('/search_user', methods=['POST'])
def search_user():
    data = request.get_json()
    user_name = data.get('name', '')

    found_user = next((user for user in users if user['name'] == user_name), None)

    if found_user:
        return jsonify(found_user)
    else:
        return jsonify({"name": "Not found", "age": 0, "city": "Unknown"})

if __name__ == '__main__':
    app.run(port=5000)
