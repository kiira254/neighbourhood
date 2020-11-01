from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile (models.Model):
    username = models.CharField(max_length = 50,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'Profile')
    bio = models.TextField(null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)

def __str__(self):
        return self.user.username

class Neighborhood (models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE)
    occupants = models.IntegerField(null=True)

    @classmethod
    def __str__(self):
        return self.name

    @classmethod
    def create_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    @classmethod
    def update_neighborhood(self):
        self.save()

    @classmethod
    def update_occupants(self):
        self.occupants += 1
        self.save()