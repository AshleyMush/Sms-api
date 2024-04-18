from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    # This is where you'll handle user creation logic.
    return jsonify({"status": "success", "message": "User created"}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # This is where you'll retrieve user data.
    return jsonify({"user_id": user_id, "user_name": "Example"})

if __name__ == '__main__':
    app.run(debug=True)
