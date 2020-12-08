m.request({
    method: 'GET',
    url: '/' + id + '/read',
    withCredentials: true,
}).then(data => {
    document.getElementById('message_content').innerText = data['content']
}).catch(e => {
    if (e.code == 404 || e.code == 403) {
        window.location.replace('/gui/' + id + '/read')
    }
})


function edit_message() {
    content = document.getElementById('message_content').value
    if (content.length > 160) {
        document.getElementById('flash').innerText = 'Wiadomość jest za długa!'
        return;
    }
    m.request({
        method: 'POST',
        url: '/' + id + '/edit',
        body: {
            token: token,
            content: content,
        },
        withCredentials: true,
    }).then(data => {
        window.location.href = '/gui/' + id + '/read'
    })
}
