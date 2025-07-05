from django.shortcuts import render , redirect

from . import dto
from .db import ServiceDb
from django.contrib.auth.decorators import login_required

# Create your views here.
class ServiceViews :
    equipment = {
        "nom" :  '',
        "description"  : "",
        "prix" : "",
        "categorie": ""
    }
    errors= {}
    is_update = False
    id_update =  None
    imge = None
    def setValues ( request):
        ServiceViews.equipment["nom"] = request.POST.get("nom")
        ServiceViews.equipment["description"] = request.POST.get("description")
        ServiceViews.equipment["prix"] = request.POST.get("prix")
        ServiceViews.equipment["categorie"] = request.POST.get("categorie")



    @staticmethod
    @login_required

    def create_page ( request):
        return render(request, 'add_service.html', {"equipment": ServiceViews.equipment , "errors":ServiceViews.errors , "is_up" :ServiceViews.is_update ,"title" : "Services"  }) 
    

    @staticmethod
    @login_required
 
    def save(request):
        ServiceViews.setValues(request)
        ServiceViews.errors = dto.validator(request ,ServiceViews.is_update )
        if len(ServiceViews.errors) == 0:
            if not ServiceViews.is_update:
                ServiceDb.create_equipment(ServiceViews.equipment)
            else:
                ServiceDb.update_equipment(ServiceViews.id_update,ServiceViews.equipment)
                ServiceViews.inisalisation()
            return redirect('service_list')
        else:
            return redirect ("service_create_page")
    @staticmethod
    @login_required

    def list_equipment(request):
        data =  {
             "nom" : request.POST.get('nom' , ''),
             "categorie" : request.POST.get('categorie' , ''),
        }
        
        ServiceViews.inisalisation()
        return render(request, 'list_service.html', {"equipment": ServiceDb.fitler(data) ,"title" : "Services"})
    
    @staticmethod
    @login_required

    def delete_equipment(request , id):
        ServiceDb.delete_equipment(id)
        return redirect("service_list")
    
    @staticmethod
    @login_required
 
    def edit_page(request , id):
        ServiceViews.id_update = id
        ServiceViews.is_update = True

        equipment = ServiceDb.get_equipment(id)
        ServiceViews.equipment["nom"] = equipment.nom
        ServiceViews.equipment["description"] = equipment.description
        ServiceViews.equipment["categorie"] = equipment.categorie
        ServiceViews.equipment["prix"] = equipment.prix


        print(ServiceViews.equipment)
        return render(request, 'add_service.html', {"equipment": ServiceViews.equipment ,  "errors":ServiceViews.errors ,"is_up" :ServiceViews.is_update ,"title" : "Services"  }) 
    def inisalisation():
        ServiceViews.equipment = {
        "nom" :  '',
        "description"  : "",
        "prix" : "",
        "categorie": ""
    }
        ServiceViews.errors= {}
        ServiceViews.is_update = False
        ServiceViews.id_update =  None
        ServiceViews.imge = None
    @staticmethod
    @login_required

    def cancel(request):
        ServiceViews.inisalisation()
        return redirect("service_list")



    
