state = false

function showpass() {
    const passInput = document.getElementById('pass')
    const eye = document.getElementById('eye')
    if (state) {
        passInput.setAttribute('type', 'password')
        state = false
        eye.classList.add('bx-show')
        eye.classList.remove('bx-hide')
    } else {
        eye.classList.add('bx-hide')
        eye.classList.remove('bx-show')
        passInput.setAttribute('type', 'text')
        state = true
    }

}


function checkName(user) {
    const lenghtError = document.getElementById('lenght-error')
    const nameError = document.getElementById('name-error')
    const btn = document.getElementById('r-btn')
    if (user.length >= 4) {
        lenghtError.innerHTML = ''
        var req = new XMLHttpRequest()
        req.onload = function() {
            if (this.responseText == 'true') {
                nameError.innerHTML = 'Username Available';
                nameError.classList.add('alert-success')
                nameError.classList.remove('alert-danger')
                nameError.style.display = 'block'
                btn.disabled = false;
            } else {
                nameError.innerHTML = "Username Already Exists"
                nameError.classList.add('alert-danger')
                nameError.classList.remove('alert-success')
                btn.disabled = true;
            }

        }
        req.open("GET", "/check-name?username=" + user, true)
        req.send();
    } else {
        lenghtError.innerHTML = "*Minimum Length 4 Character"
        nameError.style.display = 'none'
        btn.disabled = true
    }
    if (user.length == '') {
        nameError.innerHTML = ''
        nameError.classList.remove('alert-danger')
        nameError.classList.remove('alert-success')
        nameError.style.display = 'none'
        btn.disabled = true;
    }
}