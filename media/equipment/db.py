from photo.db import PhotoDb
from .models import Equipement
class EquipmentDb :
    def create_equipment(equipment):
        equipment = Equipement.objects.create(nom =equipment["nom"], description = equipment["description"], categorie = equipment["categorie"], prix = equipment["prix"] , photo = equipment["photo"] ) 
        return equipment
    def get_equipment(equipment_id):
        equipment = Equipement.objects.get(id = equipment_id)
        return equipment
    def update_equipment(equipment_id, equipment):
        equipment1 = Equipement.objects.get(id = equipment_id)
        print(equipment)
        equipment1.nom = equipment["nom"]
        equipment1.description = equipment["description"]
        equipment1.categorie = equipment["categorie"]
        equipment1.prix = equipment["prix"]
        equipment1.photo = equipment["photo"]
        equipment1.save()
        return equipment1
    def delete_equipment(equipment_id):
        equipment = Equipement.objects.get(id = equipment_id)
        equipment.delete()
        return "equipment deleted"
    def get_all_equipment():
        equipment = Equipement.objects.all()
        for user in equipment:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        return equipment
    def filter(data):
        equipment  = Equipement.objects.all()
        if data.get("nom"):
            equipment = equipment.filter(nom__icontains=data["nom"].strip())
        if data.get("categorie"):
            equipment = equipment.filter(categorie=data["categorie"].strip())
        for user in equipment:
            user.photo = PhotoDb.get_photo(user.photo)
            user.photo = user.photo
        return equipment
    def count_equipmnet():
        return Equipement.objects.all().count()
    
