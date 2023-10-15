document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('form');
    const answerDisplay = document.querySelector('#answer');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const question = document.querySelector('#question').value;
        const context = document.querySelector('#context').value;

        fetch('/question-answering', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({question, context}),
        })
        .then(response => response.json())
        .then(data => {
            answerDisplay.textContent = data.answer;
        })
        .catch(error => {
            console.error('Error', error);
        });
    });
});