from django.shortcuts import redirect, render
from .db import UserDb
from photo.db import PhotoDb 
from . import dto
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserView:
    user = {
    "username" : "",
    "role" : "",
    "phone": "",
    "password" : "",
    "photo": ""
    
}
    recherche= ''
    errors = {}
    is_update = False
    id_update = None
    @staticmethod
    @login_required
    def saveValues(request):
        UserView.user['username'] = request.POST['username']
        UserView.user['role'] = request.POST['role']
        UserView.user['phone'] = request.POST['phone']
        UserView.user['password'] = request.POST['password']
        UserView.user['photo'] = request.FILES.get('photo')

   
    @staticmethod
    @login_required
    def list_user(request):
        UserView.inisalisation()
        UserView.recherche = request.POST.get('username', '')

        data =  {
             "username" : request.POST.get('username' , ''),
             "role" : request.POST.get('role' , ''),
        }
        print(data)
        users = UserDb.filter_user(data)
        return render(request, 'list_user.html', {'users': users ,  "recherche": UserView.recherche  , "title" : "Users"})  
        
    
    @staticmethod
    @login_required
    def create_page(request):
        return render(request, 'add_user.html' ,{"user" :UserView.user  , "errors" :UserView.errors , "is_update" : UserView.is_update, "title" : "Users"} )    
    
    @staticmethod
    @login_required
    def save(request):
        # validation
        UserView.saveValues(request)
        UserView.errors =  dto.validator(request , UserView.is_update)
        print(f"aaaaaaaaaaaaaaaaaa {UserView.errors}")
        print(UserView.errors)
        if UserView.errors:
            if UserView.is_update:
                return redirect('edit_page',  id=UserView.id_update )
            else:
                return redirect('create_page')
        
        
        #save 
        if UserView.is_update:
            if UserView.user['photo'] == None :
                    UserView.user['photo'] = UserDb.get_user_by_id(UserView.id_update).photo
            print(UserView.user)
            UserDb.update_user(UserView.id_update, UserView.user)
        else:
            UserView.user['photo'] = PhotoDb.create_photo( UserView.user['photo']).id
            UserDb.create(UserView.user)
        return redirect('list_users')






        # if True:
        #     if UserView.is_update:
        #         # UserView.user['photo'] = PhotoDb.create_photo( UserView.user['photo']).id
        #         
        #         if  UserView.errors:
        #           return redirect('edit_page',  id=UserView.id_update )
        #         else:
        #           UserDb.update_user(UserView.id_update, UserView.user)
        #     else:
        #         UserDb.create(UserView.user)       
        #     return redirect('list_users'  )
        # else :
        #      return redirect('create_page')
        # pass 

    @staticmethod
    @login_required
    def delete_user(request, id) :
        UserDb.delete_user(id)
        return redirect('list_users')
    
    @staticmethod
    @login_required
    def edit_page(request, id) :
        UserView.inisalisation()
        user = UserDb.get_user_by_id(id)
        if not UserView.is_update :
            UserView.user["username"] = user.username
            UserView.user["role"] = user.role
            UserView.user["phone"] = user.phone
            UserView.user["photo"] = user.photo
            UserView.id_update = id
            UserView.is_update = True
        print(user)
        return render(request, 'add_user.html' ,{"user" :UserView.user  , "errors" :UserView.errors , "is_update" : UserView.is_update ,"title" : "Users"} )   

    def inisalisation():
            UserView.user = {
                  "username" : "",
                    "role" : "",
    "phone": "",
    "password" : "",
    "photo": ""
            }
            UserView.errors = {}
            UserView.is_update = False
            UserView.id_update = None
            print("qwertyuiopdiegf0g 08ueft8uefvtudgf0v8ud0fv8ud8edvft ")

    @staticmethod
    @login_required
    def cancel(request):
        UserView.inisalisation()
        return redirect('list_users')
    





