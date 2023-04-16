from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/protected', methods=['GET'])
def protected():
    # This is the protected endpoint that requires authentication
    token = request.headers.get('Authorization')
    if token != 'my_secret_token':
        return jsonify({'message': 'Invalid token'}), 401
    else:
        return jsonify({'message': 'Welcome to the protected endpoint!'})
