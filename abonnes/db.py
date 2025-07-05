from .models import Abonne
class AbonneDb :
    def createAbonnee(abonnee):
        Abonne.objects.create(**abonnee)
    def getAbonneeByUser (user) :
        return Abonne.objects.filter(user=user).first()
