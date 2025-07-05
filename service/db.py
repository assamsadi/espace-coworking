from .models import Service
class ServiceDb :
    def create_equipment(equipment):
        equipment = Service.objects.create(nom =equipment["nom"], description = equipment["description"], categorie = equipment["categorie"], prix = equipment["prix"] ) 
        return equipment
    def get_equipment(equipment_id):
        equipment = Service.objects.get(id = equipment_id)
        return equipment
    def update_equipment(equipment_id, equipment):
        equipment1 = Service.objects.get(id = equipment_id)
        print(equipment)
        equipment1.nom = equipment["nom"]
        equipment1.description = equipment["description"]
        equipment1.categorie = equipment["categorie"]
        equipment1.prix = equipment["prix"]
        equipment1.save()
        return equipment1
    def delete_equipment(equipment_id):
        equipment = Service.objects.get(id = equipment_id)
        equipment.delete()
        return "equipment deleted"
    def get_all_equipment():
        equipment = Service.objects.all()
        return equipment
    def fitler(data):
        service  = Service.objects.all()
        if data.get("nom"):
            service = service.filter(nom__icontains=data["nom"].strip())
        if data.get("categorie"):
            service = service.filter(categorie=data["categorie"].strip())
        return service
    def count_service():
        return Service.objects.all().count()
    
