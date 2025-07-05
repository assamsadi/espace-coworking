from django.http import HttpResponse
from django.shortcuts import render , redirect
from .db import __Auth__
from photo.db import PhotoDb
from . import dto
# Create your views here.
class auth__views:
    user_login = {
        "username" : "",
        "password" : "",
    }
    user_register = {
        "username" : "",
        "password" : "",
        "password2" : "",
        "phone" : "",
    }
    errors = {}
    def set_value_login(request):
        auth__views.user_login["username"] = request.POST["username"]
        auth__views.user_login["password"] = request.POST["password"]


    def set_value_register(request):
        auth__views.user_register["username"] = request.POST["username"]
        auth__views.user_register["password"] = request.POST["password"]
        auth__views.user_register["password1"] = request.POST["password1"]
        auth__views.user_register["phone"] = request.POST["phone"]
       
            
    @staticmethod
    def loginPage(request):
        return render(request, 'login.html', {"errors": auth__views.errors , "user_login" : auth__views.user_login})


    @staticmethod
    def registerPage(request):
        return render (request , "register.html" ,  {"errors": auth__views.errors , "user_login" : auth__views.user_register})

    
    @staticmethod
    def login(request):
        auth__views.set_value_login(request)
        auth__views.errors = dto.validator_login(request)
        if auth__views.errors:
            return redirect('loginPage')
        user = __Auth__.login(request)
        if user != None :
            user.photo = PhotoDb.get_photo(user.photo)
            if user.role == 'admin':
                return redirect("dashboard_page")
            if user.role == 'staff':
                return redirect("list_page_staff")
            if user.role == 'client':
                return redirect("create_page")
        else :
            auth__views.errors["server"] = "username or password is incorrect"
            return redirect("loginPage")

    @staticmethod
    def register(request):
        auth__views.set_value_register(request)
        auth__views.errors = dto.validator_register(request)
        if auth__views.errors:
            return redirect('registerPage')
        else :
        
            user = __Auth__.register(request)
            return redirect("create_page")

    @staticmethod
    def  logout(request):
        __Auth__.logout(request)
        return redirect("loginPage")


