function get_token() {
    login = document.getElementById('login').value
    password = document.getElementById('password').value
    if (!login || !password) {
        document.getElementById('flash').innerText = 'Puste pola!'
        return false
    }
    m.request({
        method: 'POST',
        url: '/auth/token',
        body: {
            login: login,
            password: password,
        },
        withCredentials: true,
    }).then(data => {
        m.request({
            method: 'POST',
            url: '/gui/set_token',
            body: {
                'token': data['token'],
            },
            withCredentials: true,
        }).then(data => {
            window.location.href = '/gui/login'
        })
    }).catch(e => {
        if (e.code == 403) {
            document.getElementById('flash').innerText = 'Niepoprawne dane logowania'
        }
    })
    return false
}
