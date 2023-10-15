from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://naafi:admin1234@db/qa_db"
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    context = db.Column(db.String(255), nullable=False)
    feedback_text = db.Column(db.String(255), nullable=False)

@app.route('/feedback', methods=["GET"])
def load_feedback_form():
    return render_template('feedback_page.html')

@app.route('/feedback', methods=["POST"])
def collect_feedback():
    if request.is_json:
        data = request.get_json()
        feedback = Feedback(
            question=data.get('question'),
            context=data.get('context'),
            feedback_text=data.get('feedback_text')
        )
        with app.app_context():
            db.session.add(feedback)
            db.session.commit()
        return jsonify({'message': 'Feedback Received and Saved to Database'}), 201
    else:
        return jsonify({'error': 'Invalid JSON data format'}), 400

@app.route('/fetch_feedbacks', methods=["GET"])
def get_feedback():
    feedback_entries = Feedback.query.all()
    feedback_data = [
        {
            'id': entry.id,
            'question': entry.question,
            'context': entry.context,
            'feedback_text': entry.feedback_text
        }
        for entry in feedback_entries
    ]
    return jsonify(feedback_data), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080)
