from flask import Flask, request, jsonify
import json


# Create app
app = Flask(__name__)

feedback_data = []

@app.route('/feedback', methods=["POST"])
def collect_feedback():
    feedback = request.json()
    feedback_data.append(feedback)
    with open('feedback.json', 'w') as f:
        json.dump(feedback_data, f)
    return jsonify({
        'message': 'Feedback Received.'
    })

@app.route('/feedback', methods=["GET"])
def get_feedback():
    return jsonify(feedback_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)