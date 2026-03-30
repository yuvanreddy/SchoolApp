const socket = io('http://localhost:5000');

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('connected', (data) => {
    console.log(data.data);
});

socket.on('new_notification', (notification) => {
    displayNotification(notification.message);
});

function displayNotification(message) {
    const notificationsDiv = document.getElementById('notifications');
    const notificationDiv = document.createElement('div');
    notificationDiv.className = 'notification';
    notificationDiv.textContent = message;
    notificationsDiv.appendChild(notificationDiv);

    // Remove notification after 5 seconds
    setTimeout(() => {
        notificationsDiv.removeChild(notificationDiv);
    }, 5000);
}

document.getElementById('send-notification').addEventListener('click', () => {
    fetch('/api/notifications', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: 'Test notification from frontend!' })
    });
});

// Fetch initial dashboard data (optional, can be removed if not needed)
fetch('/api/dashboard')
    .then(res => res.json())
    .then(data => console.log('Dashboard data:', data))
    .catch(err => console.error('Error fetching dashboard:', err));