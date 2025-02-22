function toggleChat() {
    const chatWindow = document.getElementById('chatWindow');
    chatWindow.style.display = chatWindow.style.display === 'none' ? 'flex' : 'none';
    }

function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');

    if (chatInput.value.trim() !== '') {

        const message = document.createElement('div');
        message.className = 'message';
        message.textContent = chatInput.value;

        chatMessages.appendChild(message);

        chatInput.value = '';

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

    document.getElementById('chatInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

window.addEventListener('beforeunload', function (e) {
    // Evitar que el navegador cierre inmediatamente
    //e.preventDefault();
    alert("El navegador se va a cerrar.");
    // Mostrar un mensaje de confirmación (opcional)
    console.log("El navegador se va a cerrar.");
});