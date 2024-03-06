// Function to send a POST request to Flask backend
function generatePassword() {
  const application = document.getElementById('application-input').value;
  const username = document.getElementById('username-input').value;

  const url = 'http://localhost:5000/suggestor'; // Update URL as needed
  
  fetch(url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          application: application,
          username: username
      })
  })
  .then(response => response.json())
  .then(data => {
      // Display generated password to the user
      const generatedPassword = data.password;
      // Update the UI with the generated password
      document.getElementById('password-display').innerText = generatedPassword;
  })
  .catch(error => console.error('Error:', error));
}

// Add event listener to trigger password generation
document.getElementById('generate-password-button').addEventListener('click', generatePassword);
