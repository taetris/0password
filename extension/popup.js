document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('passwordForm');

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
          alert('Generated Password: ' + password);
      })
      .catch(error => {
          console.error('Error:', error);
          alert('Error generating password. Please try again.');
      });
  });
});
