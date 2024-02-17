chromium.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url.includes('login')) {
    chromium.tabs.sendMessage(tabId, { action: 'showAlert' });
  }
});
