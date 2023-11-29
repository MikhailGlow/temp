function sendMessage() {
    var name = document.getElementById("name").value;
    var message = prompt("Введите ваше сообщение:");

    if (name.trim() === "") {
        name = "Гость";
    }

    if (message === null || message.trim() === "") {
        alert("Ошибка! Сообщение не может быть пустым.");
        return;
    }

    var chatBox = document.getElementById("chat-box");
    var newMessage = name + ": " + message;
    var div = document.createElement("div");
    div.appendChild(document.createTextNode(newMessage));
    chatBox.appendChild(div);

    // Очистка поля ввода после отправки сообщения
    document.getElementById("name").value = "";
}

// Вызов функции sendMessage при нажатии Enter
document.getElementById("name").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
