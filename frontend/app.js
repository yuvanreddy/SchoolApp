fetch('/api/dashboard')
    .then(res => res.json())
    .then(data => console.log(data));