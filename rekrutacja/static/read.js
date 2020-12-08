m.request({
    method: 'GET',
    url: '/' + id + '/read',
    withCredentials: true,
}).then(data => {
    document.getElementById('message_content').innerText = data['content']
}).catch(e => {
    if (e.code == 404) {
        document.getElementById('message_content').innerText = 'Wiadomość nie istnieje'
    }
})


function delete_message() {
    m.request({
        method: 'POST',
        url: '/' + id + '/delete',
        body: {
            token: token,
        },
        withCredentials: true,
    })
}
