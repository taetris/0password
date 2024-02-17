chromium.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'showAlert') {
      alert('Login page detected!'); // Change this to your desired alert mechanism
    }
  });
  