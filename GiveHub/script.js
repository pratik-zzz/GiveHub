function handleDonateButtonClick() {
    window.location.href = 'donation.html'; 
}
function handleRequestButtonClick() {
    window.location.href = 'request.html'; 
}
document.getElementById('donateButton').addEventListener('click', handleDonateButtonClick);
document.getElementById('requestButton').addEventListener('click', handleRequestButtonClick);

// Get a reference to the share button
const shareButton = document.getElementById('shareButton');

// Get a reference to the share content
const shareContent = document.getElementById('shareContent');

// Add a click event listener to the share button
shareButton.addEventListener('click', async () => {
  try {
    // Check if the navigator.share method is available
    if (navigator.share) {
      // Use navigator.share to trigger the native share dialog
      await navigator.share({
        title: shareContent.querySelector('h2').innerText, // Title of the shared content
        text: shareContent.querySelector('p').innerText,   // Text content to share
        url: window.location.href                           // URL of the shared content
      });
      console.log('Shared successfully!');
    } else {
      // Fallback for browsers that do not support navigator.share
      alert('Sharing is not supported in your browser.');
    }
  } catch (error) {
    console.error('Error sharing:', error);
    // Handle errors while sharing
  }
  
});
