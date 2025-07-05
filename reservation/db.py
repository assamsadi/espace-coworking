from django.utils import timezone
import json
from .models import Reservation
class  ReservationDb : 
    def createRsevation(reservation):
        reservation = Reservation.objects.create(
            user= reservation['user'],
            from_reserve=reservation['from_reserve'],
            to_reserve=reservation['to_reserve'],
            duree=reservation['duree'],
            num_salle=reservation['num_salle'],
            num_ticket=reservation['num_ticket'],
            equipements=reservation['equipements'],
            servises=reservation['servises'],
            status=reservation['status'],
            type=reservation['type'],
            prix=reservation['prix'],
            date=reservation['date'],
        )
        return reservation
    def getReservation(id):
        data = Reservation.objects.get(id=id)
        data.equipements = json.loads(data.equipements)
        data.servises = json.loads(data.servises)
        return data
    def getAllReservation():
        date =  Reservation.objects.all()
        for i in date:
            i.equipements = json.loads(i.equipements)
            i.servises = json.loads(i.servises)
        return date
    def updateReservation(id, reservation):
        reservation = Reservation.objects.get(id=id)
        reservation.__dict__.update(reservation)
        reservation.save()
        return reservation
    def deleteReservation(id):
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
    def updateStatus(id , status):
        reservation = Reservation.objects.get(id=id)
        reservation.status = status
        reservation.save()
        return reservation
    def changeNum_ticket( id , num_ticket):
        reservation = Reservation.objects.get(id=id)
        reservation.num_ticket = num_ticket
        reservation.save()
        return reservation
    def filter(data , role):
        if role == 'admin':
            reservation  = Reservation.objects.all()
        else :
             reservation= Reservation.objects.filter(from_reserve =  str (timezone.now().date().strftime("%Y-%m-%d"))  )
             print (timezone.now().date().strftime("%Y-%m-%d"))

        if data.get("num_salle"):
            reservation = reservation.filter(num_salle__icontains=data["num_salle"].strip())
        if data.get("status"):
            reservation = reservation.filter(status=data["status"].strip())
        for i in reservation:
            i.equipements = json.loads(i.equipements)
            i.servises = json.loads(i.servises)
        return reservation
    def filterByUser(data , user):
        
        reservation  = Reservation.objects.filter(user=user)
        if data.get("num_salle"):
            reservation = reservation.filter(num_salle__icontains=data["num_salle"].strip())
        if data.get("status"):
            reservation = reservation.filter(status=data["status"].strip())
        for i in reservation:
            i.equipements = json.loads(i.equipements)
            i.servises = json.loads(i.servises)
        return reservation
    def updatePiament(id , status):
        reservation = Reservation.objects.get(id=id)
        reservation.piament = status
        reservation.save()
    def count_all_resevation():
        return Reservation.objects.all().count()
    def count_resevation_by_status(status):
        return Reservation.objects.filter(status=status).count()
    def count_resevation_by_piament(status):
        return Reservation.objects.filter(piament=status).count()
    