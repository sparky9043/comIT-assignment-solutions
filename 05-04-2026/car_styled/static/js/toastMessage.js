document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const toastContainer = document.querySelector('#toast-container');
    
    while (toastContainer.firstChild) {
      toastContainer.removeChild(toastContainer.firstChild);
    }
  }, 3000);
});