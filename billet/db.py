
import json
from billet.models import Billet

class BilletDb :
    def createBillet(billet):
        billet_new = Billet.objects.create(
            user= billet['user'],
            from_reserve=billet['from_reserve'],
            to_reserve=billet['to_reserve'],
            duree=billet['duree'],
            num_salle=billet['num_salle'],
            qr_code=billet['qr_code'],
            equipements=billet['equipements'],
            servises=billet['servises'],
            status=billet['status'],
            type=billet['type'],
            prix=billet['prix'],
        )
        return billet_new
    def listBillet(user):
        date =  Billet.objects.filter(user = user)
        for i in date:
            i.equipements = json.loads(i.equipements)
            i.servises = json.loads(i.servises)
        return date
    def getBillet(id):
        billet = Billet.objects.get(id=id)
        billet.equipements = json.loads(billet.equipements)
        billet.servises = json.loads(billet.servises)
        return billet
       