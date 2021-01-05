from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginFormAdmin
from django import forms
from django.views.generic import TemplateView, ListView, DetailView
from signup.models import InfluencerList, PhotographerList, Accounts
from django.contrib.auth.models import User


class AdminUsers(TemplateView):
    template_name = 'hobnobAdmin/user.html'

class AddNewUser(TemplateView):
    template_name = 'hobnobAdmin/addnewuser.html'

class ManageUser(TemplateView):
    template_name = 'hobnobAdmin/manageuser.html'

# class ManageUser(TemplateView):
#     template_name = 'hobnobAdmin/manageuser.html'

class ProfileListView(ListView):
    model = User
    template_name = 'hobnobAdmin/profile.html'

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['influencer_profile_list'] = InfluencerList.objects.all()
        context['photographer_profile_list'] = PhotographerList.objects.all()
        # context['influencer_profile_list'] = InfluencerList.objects.all()
        return context

class ProfileDetailView(DetailView):
    model = Accounts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['profile_list'] = Accounts.objects.all()
        return context

class Campaigns(TemplateView):
    template_name = 'hobnobAdmin/campaigns.html'

class Branding(TemplateView):
    template_name = 'hobnobAdmin/branding.html'

class Deliverable(TemplateView):
    template_name = 'hobnobAdmin/deliverable.html'

class Hashtags(TemplateView):
    template_name = 'hobnobAdmin/hashtags.html'

class Calender(TemplateView):
    template_name = 'hobnobAdmin/calender.html'

class Journey(TemplateView):
    template_name = 'hobnobAdmin/journey.html'

class Finance(TemplateView):
    template_name = 'hobnobAdmin/finance.html'

class Service(TemplateView):
    template_name = 'hobnobAdmin/service.html'

class Marketing(TemplateView):
    template_name = 'hobnobAdmin/marketting.html'

class Upload(TemplateView):
    template_name = 'hobnobAdmin/upload.html'

@login_required(login_url='/hobnobadmin/')
def hobnobAdminIndex(request):
    return render(request,'hobnobAdmin/index.html')

def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

@login_required
def logout_func(request):
    logout(request)
    return redirect("hobnobAdmin:hobnob_admin_login")

def hobnobAdminLogin(request):
    custom_error = ""
    if request.method == 'POST':

        form = LoginFormAdmin(request.POST)
        print(form)
       
        if form.is_valid():
            # form.save()

            username_email = form.cleaned_data.get('username')
            if validateEmail(username_email):
                
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username_email, password=password)
                print('userrrrr',user)
                if user is not None:
                    try:
                        if user.hobnobadmin.isHobnobAdmin == True:
                            print("hereee")
                            login(request, user)
                            print("logedin")
                            print("user: ",user.username)
                            print(user.hobnobadmin.isHobnobAdmin)
                            return render(request, 'hobnobAdmin/index.html')
                    except ValueError:
                        print("errorrr")
                        custom_error = "Sorry, You are not authorized to access the admin panel."
                        # raise forms.ValidationError("User is not Authorized")
                        # return HttpResponse(" user not authrized ")
                        
                else:
                    custom_error = "Sorry, You don't have a registered account yet. Create one?"
            else:
                custom_error = "Please enter a valid username. Use your email."
        else:
            custom_error = "Please enter a valid username. Use your email."
    else:
        form = LoginFormAdmin()

    return render(request, 'hobnobAdmin/login.html', {'form': form, 'custom_error': custom_error})
