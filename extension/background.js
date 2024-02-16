chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: readDataFromPage
    });
  });
  
  function readDataFromPage() {
    // Example: Read the title of the current page
    const pageTitle = document.title;
  
    // Example: Read the URL of the current page
    const pageUrl = window.location.href;
  
    // Create JSON object with page data
    const pageData = {
      title: pageTitle,
      url: pageUrl
    };
  
    // Save page data to storage
    chrome.storage.local.get('pages', function(data) {
      const pages = data.pages || [];
      pages.push(pageData);
      chrome.storage.local.set({ pages: pages }, function() {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError.message);
        } else {
          console.log('Page data saved:', pageData);
        }
      });
    });
  }
  
  