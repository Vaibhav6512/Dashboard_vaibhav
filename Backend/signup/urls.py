from django.conf.urls import url
from . import views

app_name = 'signup'

urlpatterns = [
    url(r'^$', views.login_func, name='login'),
    url(r'^create/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_func, name='logout'),
    url(r'^influencer_regis/$', views.influencer_regis, name='influencer_regis'),
    url(r'^photographer_regis/$', views.photographer_regis, name='photographer_regis'),
]
