from django.contrib.auth import authenticate, login , logout as auth_login
from django.contrib.auth import logout
from user.models import User
class __Auth__:
    def login(request):
        user= authenticate(request , username = request.POST['username'] , password = request.POST['password'])
        if user is not None:
            login(request, user)  
        return user
    def register(request):
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'] , is_staff = True , phone=request.POST['phone'])
        return user
    def logout(request):
        logout(request)
        

