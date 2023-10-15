from transformers import AutoTokenizer, pipeline
import torch

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


# Load pre-trained BERT model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
#tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, skip_special_tokens=False)
#qa_pipeline = pipeline('question-answering', model=model_name, tokenizer=tokenizer)


# Create app.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://naafi:admin1234@db/qa_db"
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    context = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)

@app.route("/", methods=["POST"])
def test():
    question = request.json.get('question')
    # Placeholder for question answering pipeline
    answer = ""
    return render_template("qa_page.html", answer=answer)


@app.route("/question-answering", methods=["GET", "POST"])
def question_answering():
    answer = None
    if request.method == "POST":
        question = request.json.get('question')
        context = request.json.get('context')

        with torch.no_grad():
            
            result = {"answer": "this is a placeholder answer."}
            answer = result['answer']

    # Save question, context and answer in database
    with app.app_context():
        usr_query = Question(question=question, context=context, answer=answer)
        db.session.add(usr_query)
        db.session.commit()
    return render_template("qa_page.html", answer=answer)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
