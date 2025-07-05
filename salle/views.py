import json
from django.shortcuts import render , redirect
from equipment.db import EquipmentDb
from photo.db import PhotoDb
from . import dto
from .db import SalleDb
from django.contrib.auth.decorators import login_required

# Create your views here.
class SalleView :
    salle = {
        "name" :  '',
        "description"  : "",
        "prix" : "",
        "photo" : "",
        "categorie": "",
        "equipments":[],
        "status" :""
    }
    errors= {}
    is_update = False
    id_update =  None
    imge = None
    equipments = []
    equipments_selected = []
    def setValues ( request):
        SalleView.salle["name"] = request.POST.get("name")
        SalleView.salle["description"] = request.POST.get("description")
        SalleView.salle["prix"] = request.POST.get("prix")
        SalleView.salle["categorie"] = request.POST.get("categorie")
        SalleView.salle['photo'] = request.FILES.get('photo')
        SalleView.salle['equipments'] = json.dumps(SalleView.equipments_selected )



    @staticmethod
    @login_required

    def create_page ( request):
        SalleView.equipments = EquipmentDb.get_all_equipment()
        return render(
            request, 'add_salle.html',
              {"salle": SalleView.salle , 
               "errors":SalleView.errors , 
               "is_up" :SalleView.is_update ,  
               "equipments":SalleView.equipments ,
               "equipments_selected":SalleView.equipments_selected ,
               "title" : "Salles"
                 }) 
    

    @staticmethod
    @login_required
 
    def save(request):
        SalleView.setValues(request)
        SalleView.errors = dto.validator(request ,SalleView.is_update )
        if len(SalleView.errors) == 0:
            if not SalleView.is_update:
                SalleView.salle['photo'] = PhotoDb.create_photo( SalleView.salle['photo']).id
                SalleView.salle["status"] = "libre"
                SalleDb.create_salle(SalleView.salle)
            else:
                if  SalleView.salle['photo'] == None:
                    SalleView.salle['photo'] =  SalleView.imge
                else:
                    SalleView.salle['photo'] = PhotoDb.create_photo( SalleView.salle['photo']).id
                SalleDb.update_salle(SalleView.id_update,SalleView.salle)
                SalleView.inisalisation()
            return redirect('salle_list')
        else:
            return redirect ("salle_create_page")
    @staticmethod
    @login_required

    def list_salle(request):
        data =  {
             "name" : request.POST.get('name' , ''),
             "categorie" : request.POST.get('categorie' , ''),
        }
        SalleView.inisalisation()
        SalleView.cancel(request)
        print(data)
        return render(request, 'list_salle.html', {"salle": SalleDb.filter(data) , "title" : "Salles"})
    
    @staticmethod
    @login_required

    def delete_salle(request , id):
        SalleDb.delete_salle(id)
        return redirect("salle_list")
    
    @staticmethod
    @login_required
 
    def edit_page(request , id):
        SalleView.equipments = EquipmentDb.get_all_equipment()
        SalleView.id_update = id
        SalleView.is_update = True
        salle = SalleDb.get_salle(id)
        print(salle)
        SalleView.salle["name"] = salle.name
        SalleView.salle["description"] = salle.description
        SalleView.salle["categorie"] = salle.categorie
        SalleView.salle["prix"] = salle.prix
        SalleView.salle["status"] = salle.status
        SalleView.salle["photo"] = None
        SalleView.equipments_selected = salle.equipments

        SalleView.imge =  salle.photo

        print(SalleView.salle)

        return render(request, 'add_salle.html', {"salle": SalleView.salle ,  "errors":SalleView.errors ,"is_up" :SalleView.is_update  ,     "equipments":SalleView.equipments ,
               "equipments_selected":SalleView.equipments_selected , 
               "title" : "Salles"}) 
    def inisalisation():
        SalleView.salle = {
        "name" :  '',
        "description"  : "",
        "prix" : "",
        "photo" : "",
        "categorie": ""
    }
        SalleView.errors= {}
        # SalleView.equipments_selected =[]
        SalleView.is_update = False
        SalleView.id_update =  None
        SalleView.imge = None
        SalleView.equipments_selected = []
    @staticmethod
    @login_required

    def cancel(request):
        SalleView.inisalisation()
        return redirect("salle_list")
    
    #----------------- equipment----------------------#
    @staticmethod
    @login_required

    def add_equi(request , equi):
        SalleView.equipments_selected.append(equi)
        return redirect ("salle_create_page")
    @staticmethod
    @login_required

    def delete_equi(request , equi):
        SalleView.equipments_selected.remove(equi)
        return redirect ("salle_create_page")



    
