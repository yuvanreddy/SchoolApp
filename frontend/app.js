document.addEventListener('DOMContentLoaded', () => {
    loadStudents();
    
    document.getElementById('add-student').addEventListener('submit', addStudent);
});

async function loadStudents() {
    const response = await fetch('/students');
    const students = await response.json();
    const studentsDiv = document.getElementById('students');
    studentsDiv.innerHTML = students.map(s => `<div class="student">${s.name} - ${s.grade}</div>`).join('');
}

async function addStudent(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const grade = document.getElementById('grade').value;
    
    await fetch('/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, grade })
    });
    
    document.getElementById('name').value = '';
    document.getElementById('grade').value = '';
    loadStudents();
}
