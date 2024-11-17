// script.js

// Variáveis para armazenar dados (neste exemplo simples, usamos localStorage para persistir os dados temporariamente)
let users = JSON.parse(localStorage.getItem('users')) || [];
let reminders = JSON.parse(localStorage.getItem('reminders')) || [];

// Função para registrar o usuário
function registerUser() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const email = document.getElementById('email').value;

    if (name && age && email) {
        const user = { name, age, email };
        users.push(user);
        localStorage.setItem('users', JSON.stringify(users));
        alert('Usuário cadastrado com sucesso!');
        document.getElementById('registrationForm').reset();
    } else {
        alert('Por favor, preencha todos os campos!');
    }
}

// Função para adicionar lembrete de medicação
function addReminder() {
    const medication = document.getElementById('medication').value;
    const time = document.getElementById('time').value;

    if (medication && time) {
        const reminder = { medication, time };
        reminders.push(reminder);
        localStorage.setItem('reminders', JSON.stringify(reminders));
        displayReminders();
        alert('Lembrete adicionado com sucesso!');
        document.getElementById('reminderForm').reset();
    } else {
        alert('Por favor, preencha todos os campos!');
    }
}

// Função para exibir os lembretes cadastrados
function displayReminders() {
    const remindersList = document.getElementById('remindersList');
    remindersList.innerHTML = ''; // Limpa a lista para re-renderizar

    reminders = JSON.parse(localStorage.getItem('reminders')) || [];

    reminders.forEach((reminder) => {
        const reminderItem = document.createElement('div');
        reminderItem.innerText = `${reminder.medication} - ${reminder.time}`;
        remindersList.appendChild(reminderItem);
    });
}

// Exibe lembretes salvos ao carregar a página
window.onload = displayReminders;