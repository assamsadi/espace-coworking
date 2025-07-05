from .db import UserDb
def validator(request , update):
    msg_error = {}
    if request.POST['username'] == '':
        msg_error['username'] = 'Username is required'
    else :
        if UserDb.get_user_by_username(request.POST['username']) is  None:
            msg_error['username'] = 'Username already exists'

        
    if request.POST['password'] == '' and not update:
        msg_error['password'] = 'Password is required'
    elif len(request.POST['password']) <8 and not update:
         msg_error['password'] = 'Password must be at least 8 characters'


    if request.POST['role'] == '':
        msg_error['role'] = 'Role is required'
    if request.FILES.get('photo') == None and not update:
        msg_error['photo'] = 'Photo is required'
    if request.POST['phone'] == '':
        msg_error['phone'] = 'Phone is required'
    return msg_error