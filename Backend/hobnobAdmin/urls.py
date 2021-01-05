from django.conf.urls import url
from . import views

app_name = 'hobnobAdmin'

urlpatterns = [
    url(r'^$', views.hobnobAdminLogin, name='hobnob_admin_login'),
    url(r'^logout/$', views.logout_func, name='logout'),
    url(r'^hobnob_admin/index/$', views.hobnobAdminIndex, name='hobnob_admin_index'),

    url(r'^hobnob_admin/users/$', views.AdminUsers.as_view(), name='users'),
    url(r'^hobnob_admin/users/add_new/$', views.AddNewUser.as_view(), name='add_new_user'),
    url(r'^hobnob_admin/users/manage/$', views.ManageUser.as_view(), name='manage_user'),

    url(r'^hobnob_admin/campaigns/$', views.Campaigns.as_view(), name='campaigns'),

    url(r'^hobnob_admin/profile/$', views.ProfileListView.as_view(), name='profile_list'),
    url(r'^hobnob_admin/profile/details/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile_detail'),

    url(r'^hobnob_admin/branding/$', views.Branding.as_view(), name='branding'),

    url(r'^hobnob_admin/deliverable/$', views.Deliverable.as_view(), name='deliverable'),

    url(r'^hobnob_admin/hashtags/$', views.Hashtags.as_view(), name='hashtags'),

    url(r'^hobnob_admin/calender/$', views.Calender.as_view(), name='calender'),

    url(r'^hobnob_admin/journey/$', views.Journey.as_view(), name='journey'),

    url(r'^hobnob_admin/finance/$', views.Finance.as_view(), name='finance'),

    url(r'^hobnob_admin/service/$', views.Service.as_view(), name='service'),

    url(r'^hobnob_admin/marketing/$', views.Marketing.as_view(), name='marketing'),

    url(r'^hobnob_admin/upload/$', views.Upload.as_view(), name='upload'),


]