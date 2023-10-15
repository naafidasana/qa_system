document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('feedback-form');
    const submitButton = document.getElementById('submit-feedback');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const question = document.getElementById('question').value;
        const context = document.getElementById('context').value;
        const feedbackText = document.getElementById('feedback_text').value;

        // Create a JSON object with the form data
        const data = {
            question: question,
            context: context,
            feedback_text: feedbackText
        };

        fetch('/feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
            })
            .catch(error => {
                console.error('Error', error);
            });
    });
});