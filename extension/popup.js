document.getElementById("passwordForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var application = document.getElementById("application").value;
    var masterPassword = document.getElementById("masterPassword").value;
    // Handle user input (e.g., store data, encrypt master password)
    console.log("Username:", username);
    console.log("Application:", application);
    console.log("Master Password:", masterPassword);
  });
  