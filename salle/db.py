
from datetime import datetime
import json
from photo.db import PhotoDb
from .models import Salle
class SalleDb :
    def create_salle(equipment):
        equipment = Salle.objects.create(name =equipment["name"], description = equipment["description"], categorie = equipment["categorie"], prix = equipment["prix"] , photo = equipment["photo"]  , equipments =equipment["equipments"]   , status =equipment["status"]  ) 
        return equipment
    def get_salle(equipment_id):
        equipment = Salle.objects.get(id = equipment_id)
        equipment.equipments = json.loads( equipment.equipments)
        print(f'ffffffffffffffffffffffff {equipment.equipments}')
        return equipment
    def get_salle_by_name(equipment_name):
        equipment = Salle.objects.get(name = equipment_name)
        return equipment
    def update_salle(equipment_id, equipment):
        equipment1 = Salle.objects.get(id = equipment_id)
        print(equipment)
        equipment1.name = equipment["name"]
        equipment1.description = equipment["description"]
        equipment1.categorie = equipment["categorie"]
        equipment1.prix = equipment["prix"]
        equipment1.photo = equipment["photo"]
        equipment1.equipments =equipment["equipments"] 
        equipment1.save()
        return equipment1
    def delete_salle(equipment_id):
        equipment = Salle.objects.get(id = equipment_id)
        equipment.delete()
        return "equipment deleted"
    def get_all_salle():
        equipment = Salle.objects.all()
        for user in equipment:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        for i in equipment:
            i.equipments = json.loads(  i.equipments)
        
        return equipment
    def valisation_time(intervale , id):
        equipment = Salle.objects.get(id = id)
        python_data = json.loads(equipment.reservation_date)
        var_end  = datetime.strptime(intervale["form"] , "%Y-%m-%dT%H:%M")
        var_start  = datetime.strptime(intervale["to"] , "%Y-%m-%dT%H:%M")
        print(f'time :  {var_end.day}')
        for i in python_data:
                original_start = datetime.strptime(i["to"], "%Y-%m-%dT%H:%M")
                original_end = datetime.strptime(i["form"], "%Y-%m-%dT%H:%M")
                if  ( var_start <= original_start) and  ( var_end >= original_end):
                    return  False
        return True
        
    
    

    def time_includ(time , id):
        is_corect=  SalleDb.valisation_time({"to": time["to"] ,"form":time["form"] },id)
        if is_corect:
            equipment = Salle.objects.get(id = id)
            python = json.loads( str(equipment.reservation_date))
            python.append(time)
            equipment.reservation_date = json.dumps(python)
            equipment.save()
            print("time is  available") 
        else :
            print("time is not available") 
    def filter(data):
        salles = Salle.objects.all()
        if data.get("name"):
            salles = salles.filter(name__icontains=data["name"].strip())
        if data.get("categorie"):
            salles = salles.filter(categorie=data["categorie"].strip())
        for user in salles:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        for i in salles:
            i.equipments = json.loads(  i.equipments)
        return salles
    def change_status(id , status):
        equipment = Salle.objects.get(name=id)
        equipment.status = status
        equipment.save()
        return equipment
    def count_all_salle():
        return Salle.objects.all().count()
    def count_salle_by_status(status):
        return Salle.objects.filter(status=status).count()
 
    
       
        
        

    
