function get_data() {
    let current_user = JSON.parse(localStorage.getItem('current'));
    let object_name = document.getElementById('user_name');
    object_name.innerHTML = current_user.name;
}

function logout() {
    localStorage.clear();
    window.location.href = "";
}