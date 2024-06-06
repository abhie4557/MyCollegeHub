document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.alert-dismissible .close').forEach(function(button) {
      button.addEventListener('click', function() {
        const alert = button.parentElement;
        alert.classList.remove('show');
        alert.classList.add('fade');
        setTimeout(() => alert.remove(), 150); // Remove the alert after fade-out transition
      });
    });
  });
  