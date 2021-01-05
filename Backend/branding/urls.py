from django.conf.urls import url
from . import views

app_name = 'branding'

urlpatterns = [
    url(r'^branding', views.branding, name='branding'),
    url(r'^brandAdd', views.brandAdd, name='brandAdd'),
]