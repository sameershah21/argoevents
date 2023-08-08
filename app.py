from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/message')
def message():
    messages = ["hello", "bye", "morning"]
    return jsonify(message=random.choice(messages))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
