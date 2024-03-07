document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('passwordForm');
  const passwordContainer = document.getElementById('passwordContainer');
  const passwordText = document.getElementById('passwordText');
  const copyButton = document.getElementById('copyButton');
  const togglePasswordVisibilityButton = document.getElementById('togglePasswordVisibility');

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
      passwordText.style.display = 'inline-block';
      passwordContainer.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error generating password. Please try again.');
    });
  });
  togglePasswordVisibilityButton.addEventListener('click', function () {
    const isPasswordVisible = passwordText.style.display !== 'none';
    passwordText.style.display = isPasswordVisible ? 'none' : 'inline-block';
    togglePasswordVisibilityButton.textContent = isPasswordVisible ? 'Show Password' : 'Hide Password';
  });
  
  copyButton.addEventListener('click', function () {
    const password = passwordText.textContent.replace('Generated Password: ', '');
    navigator.clipboard.writeText(password)
    .then(() => {
      copiedNote.textContent = 'Copied!';
      copiedNote.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error copying password to clipboard.');
    });
  });
});
