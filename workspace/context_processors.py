# myapp/context_processors.py
from photo.db import PhotoDb
from abonnes.db import AbonneDb
def user_photo(request):
    if request.user.is_authenticated:
        return {
            'user_photo_url': PhotoDb.get_photo(request.user.photo)
        }
    return {}

def is_abonnee(request):
    ab = AbonneDb.getAbonneeByUser(request.user.username)
    if request.user.is_authenticated and ab:
        return {
            'is_abonnee': True,
            "type" : ab.type
        }
    return {'is_abonnee': False}