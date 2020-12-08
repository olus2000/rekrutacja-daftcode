function read_message() {
    message_id = document.getElementById('read_message_number').value
    window.location.href = '/gui/' + message_id + '/read'
    return false;
}
