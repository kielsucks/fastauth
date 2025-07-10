from flask import Flask, request

app = Flask(__name__)

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    print(f"Request: {request.method} {request.path}")
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data()}")
    print("Response: 200 OK")
    return "Auth endpoint reached", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
