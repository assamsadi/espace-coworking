from photo.models import Photo


class PhotoDb:
    def create_photo (photo):
        data = Photo.objects.create(file  = photo)
        return data
    def get_photo (id):
        data = Photo.objects.filter(id = id).first()
        return data
    def delete_photo (id):
        data = Photo.objects.get(id = id)
        data.delete()
        return data
    def update_photo (id, photo):
        data = Photo.objects.get(id = id)
        data.file = photo
        data.save()
        return data
    def all():
        return Photo.objects.all()