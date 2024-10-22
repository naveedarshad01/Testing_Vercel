from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, ML Experts!"})

# Make sure the app runs in production
if __name__ == '__main__':
    app.run(debug=True)
