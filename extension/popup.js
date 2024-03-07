document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('passwordForm');
  const passwordContainer = document.getElementById('passwordContainer');
  const passwordText = document.getElementById('passwordText');
  const copyButton = document.getElementById('copyButton');

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const application = document.getElementById('application').value;

    const data = {
      username: username,
      application: application
    };

    fetch('http://localhost:5000/suggestor', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      const password = data.password;
      passwordText.textContent = 'Generated Password: ' + password;
      passwordContainer.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error generating password. Please try again.');
    });
  });

  copyButton.addEventListener('click', function () {
    const password = passwordText.textContent.replace('Generated Password: ', '');
    navigator.clipboard.writeText(password)
    .then(() => {
      alert('Password copied to clipboard.');
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error copying password to clipboard.');
    });
  });
});
