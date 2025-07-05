def validator_login(request):
    msg_error = {}
    # Check if the request is a POST request
    if request.POST["username"] == '':
        msg_error['username'] = 'Username cannot be empty'
    if request.POST["password"] == '':
        msg_error['password'] = 'Password cannot be empty'
    return msg_error

def validator_register(request):
    msg_error = {}
    # Check if the request is a POST request
    if request.POST["username"] == '':
        msg_error['username'] = 'Username cannot be empty'
    if request.POST["password"] == '':
            msg_error['password'] = 'Password cannot be empty'
    elif request.POST["password"] != request.POST["password1"]:
         msg_error['confirm_password'] = 'Passwords do not match'
    if request.POST["phone"] == '':
            msg_error['phone'] = 'phone cannot be empty'
    return msg_error