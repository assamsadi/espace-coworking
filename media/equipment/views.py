from django.shortcuts import render , redirect

from photo.db import PhotoDb
from . import dto
from .db import EquipmentDb
from django.contrib.auth.decorators import login_required

# Create your views here.
class EquipmentView :
    equipment = {
        "nom" :  '',
        "description"  : "",
        "prix" : "",
        "photo" : "",
        "categorie": ""
    }
    errors= {}
    is_update = False
    id_update =  None
    imge = None
    def setValues ( request):
        EquipmentView.equipment["nom"] = request.POST.get("nom")
        EquipmentView.equipment["description"] = request.POST.get("description")
        EquipmentView.equipment["prix"] = request.POST.get("prix")
        EquipmentView.equipment["categorie"] = request.POST.get("categorie")
        EquipmentView.equipment['photo'] = request.FILES.get('photo')



    @staticmethod
    @login_required

    def create_page ( request):
        return render(request, 'add_equipment.html', {"equipment": EquipmentView.equipment , "errors":EquipmentView.errors , "is_up" :EquipmentView.is_update ,"title" : "Equipments"  }) 
    

    @staticmethod
    @login_required
 
    def save(request):
        EquipmentView.setValues(request)
        EquipmentView.errors = dto.validator(request ,EquipmentView.is_update )
        if len(EquipmentView.errors) == 0:
            if not EquipmentView.is_update:
                EquipmentView.equipment['photo'] = PhotoDb.create_photo( EquipmentView.equipment['photo']).id
                EquipmentDb.create_equipment(EquipmentView.equipment)
            else:
                if  EquipmentView.equipment['photo'] == None:
                    EquipmentView.equipment['photo'] =  EquipmentView.imge
                else:
                    EquipmentView.equipment['photo'] = PhotoDb.create_photo( EquipmentView.equipment['photo']).id
                EquipmentDb.update_equipment(EquipmentView.id_update,EquipmentView.equipment)
                EquipmentView.inisalisation()
            return redirect('equipment_list')
        else:
            return redirect ("equipment_create_page")
    @staticmethod
    @login_required

    def list_equipment(request):
     
        data =  {
             "nom" : request.POST.get('nom' , ''),
             "categorie" : request.POST.get('categorie' , ''),
        }
        print(data)
        EquipmentView.inisalisation()
        return render(request, 'list_equipment.html', {"equipment": EquipmentDb.filter(data) ,"title" : "Equipments"})
    
    @staticmethod
    @login_required

    def delete_equipment(request , id):
        EquipmentDb.delete_equipment(id)
        return redirect("equipment_list")
    
    @staticmethod
    @login_required
 
    def edit_page(request , id):
        EquipmentView.id_update = id
        EquipmentView.is_update = True

        equipment = EquipmentDb.get_equipment(id)
        EquipmentView.equipment["nom"] = equipment.nom
        EquipmentView.equipment["description"] = equipment.description
        EquipmentView.equipment["categorie"] = equipment.categorie
        EquipmentView.equipment["prix"] = equipment.prix
        EquipmentView.equipment["photo"] = None

        EquipmentView.imge =  equipment.photo

        print(EquipmentView.equipment)
        return render(request, 'add_equipment.html', {"equipment": EquipmentView.equipment ,  "errors":EquipmentView.errors , "title" : "Equipments" }) 
    def inisalisation():
        EquipmentView.equipment = {
        "nom" :  '',
        "description"  : "",
        "prix" : "",
        "photo" : "",
        "categorie": ""
    }
        EquipmentView.errors= {}
        EquipmentView.is_update = False
        EquipmentView.id_update =  None
        EquipmentView.imge = None
    @staticmethod
    @login_required

    def cancel(request):
        EquipmentView.inisalisation()
        return redirect("equipment_list")



    
