from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=70)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profiles/images/%Y/%m/%d", blank=True, null=True)
    
    def __str__(self):
        return self.user.username