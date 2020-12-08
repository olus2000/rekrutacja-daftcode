function create_message() {
    content = document.getElementById('message_content').value
    if (content.length > 160) {
        document.getElementById('flash').innerText = 'Wiadomość jest za długa!'
        return;
    }
    m.request({
        method: 'POST',
        url: '/create',
        body: {
            token: token,
            content: content,
        },
        withCredentials: true,
    }).then(data => {
        window.location.href = '/gui/' + data['id'] + '/read'
    }).catch(e => {
        if (e.code == 403) {
            window.location.replace('/gui/login')
        }
    })
}
