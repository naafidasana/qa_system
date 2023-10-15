from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json


# Create app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://naafi:admin1234@db/qa_db"
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    context = db.Column(db.String(255), nullable=False)
    feedback_text = db.Column(db.String(255), nullable=False)

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
    app.run(host='0.0.0.0', port=8080)