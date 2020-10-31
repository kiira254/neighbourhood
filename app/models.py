from django.db import models

# Create your models here.
class Profile (models.Model):
    username = models.CharField(max_length = 50,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'Profile')
    bio = models.TextField(null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 60)

def __str__(self):
        return self.user.username