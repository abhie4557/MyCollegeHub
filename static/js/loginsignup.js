document.addEventListener('DOMContentLoaded', (event) => {
    // Get the modals
    const loginModal = document.getElementById('loginModal');
    const signupModal = document.getElementById('signupModal');

    // Get the buttons that open the modals
    const loginBtn = document.getElementById('loginBtn');
    const signupBtn = document.getElementById('signupBtn');

    // Get the <span> elements that close the modals
    const closeLogin = document.getElementById('closeLogin');
    const closeSignup = document.getElementById('closeSignup');

    // Function to open a modal and disable body scroll
    function openModal(modal) {
        modal.style.display = 'flex'; // Change to 'flex' to use flexbox centering
        document.body.classList.add('modal-open');
    }

    // Function to close a modal and enable body scroll
    function closeModal(modal) {
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
    }

    // When the user clicks the button, open the login modal
    loginBtn.onclick = function() {
        openModal(loginModal);
    }

    // When the user clicks the button, open the signup modal
    signupBtn.onclick = function() {
        openModal(signupModal);
    }

    // When the user clicks on <span> (x), close the login modal
    closeLogin.onclick = function() {
        closeModal(loginModal);
    }

    // When the user clicks on <span> (x), close the signup modal
    closeSignup.onclick = function() {
        closeModal(signupModal);
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == loginModal) {
            closeModal(loginModal);
        } else if (event.target == signupModal) {
            closeModal(signupModal);
        }
    }
});
