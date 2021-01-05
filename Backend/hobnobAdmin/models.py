from django.db import models
from django.contrib.auth.models import User

class HobnobAdmin(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isHobnobAdmin = models.BooleanField(default=False)

    users = models.BooleanField(default=False)
    campaigns = models.BooleanField(default=False)
    profile = models.BooleanField(default=False)
    branding = models.BooleanField(default=False)
    deliverable = models.BooleanField(default=False)
    hashtags = models.BooleanField(default=False)
    calender = models.BooleanField(default=False)
    journey = models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    marketing = models.BooleanField(default=False)
    Upload = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username


