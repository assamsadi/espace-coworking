from .models import User
from photo.db import PhotoDb
class UserDb:
    def create(request):
        if  request['role'] == 'admin':
            user = User.objects.create_user(username=request['username'], password=request['password'] ,role=request['role'] , is_staff = True , phone=request['phone'] , photo = request['photo']) 
        else:
            user = User.objects.create_user(username=request['username'], password=request['password'] ,role=request['role'] , is_staff = False , phone=request['phone'] , photo = request['photo']) 

        return user
    def get_user_by_id(id):
        user = User.objects.get(id=id)
        return user
    def get_user_by_username(username):
        user = User.objects.filter(username=username)
        return user
    def delete_user(id):
        user = User.objects.get(id=id)
        user.delete()
        return user
    def update_user(id,request ):
        try:
            user = User.objects.get(id=id)  # Fetch the user first
        
        # Update fields (manually or dynamically)
            user.username = request.get('username', user.username)
        
            if request['password'] != "":  # Hash password if provided
                user.set_password(request['password'])  # Uses Django's hashing
        
            user.role = request.get('role', user.role)  # Custom field (if using CustomUser)
            user.is_staff = request.get('is_staff', user.is_staff)
            user.phone = request.get('phone', user.phone)  # Requires CustomUser
            user.photo = request.get('photo', user.photo)  # Requires CustomUser
        
            user.save()  # Triggers Django's save() and signals
            return True
        except User.DoesNotExist:
            return False        
    def get_all_users():
        users = User.objects.all()
        #find imge for eache user 
        for user in users:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        return users
    def filter_user(data):
        users = User.objects.all()

        if data.get("username"):
            users = users.filter(username__icontains=data["username"].strip())
    
        if data.get("role"):
            users = users.filter(role=data["role"].strip())

            
        # if data["status"]:
        #     users = user.filter(status=data["status"])
        
        for user in users:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        return users

    
