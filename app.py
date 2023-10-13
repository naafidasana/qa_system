from transformers import AutoTokenizer, pipeline
import torch

from flask import Flask, request, jsonify


# Load pre-trained BERT model and tokenizer
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False, skip_special_tokens=False)
qa_pipeline = pipeline('question-answering', model=model_name, tokenizer=tokenizer)


# Create app.
app = Flask(__name__)

@app.route("/test", methods=["POST"])
def test():
    question = request.json.get('question')
    # Placeholder for question answering pipeline
    answer = "This is a placeholder answer."
    return jsonify ({
        'answer':answer
    })


@app.route("/question-answering", methods=["POST"])
def question_answering():
    question = request.json.get('question')
    context = request.json.get('context')

    #Default answer
    answer = "No answer found."
    with torch.no_grad():
        result = qa_pipeline(question=question, context=context)
        answer = result['answer']
        return jsonify({
            'answer':answer
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)