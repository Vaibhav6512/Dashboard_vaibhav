from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Accounts)
admin.site.register(models.InfluencerList)
admin.site.register(models.PhotographerList)
