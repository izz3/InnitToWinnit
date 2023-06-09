const goodButton = document.querySelector('#good-button');
console.log("good button: ", goodButton);
goodButton.addEventListener('click', () => {
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify({ user_input: 'Good' }),
        headers: {
          'Content-Type': 'application/json'
        }
    })
});

const badButton = document.querySelector('#bad-button');
badButton.addEventListener('click', () => {
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify({ user_input: 'Bad' }),
        headers: {
          'Content-Type': 'application/json'
        }
    })
});

const neutralButton = document.querySelector('#neutral-button');
neutralButton.addEventListener('click', () => {
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify({ user_input: 'Neutral' }),
        headers: {
          'Content-Type': 'application/json'
        }
    })
});