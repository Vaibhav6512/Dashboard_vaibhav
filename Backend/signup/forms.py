from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import InfluencerList, PhotographerList
from .models import InfluencerList
from phonenumber_field.widgets import PhoneNumber


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField()
    choices = (
        ('Influencer', 'Influencer'),
        ('Makeup Artist', 'Makeup Artist'),
        ('Photographer', 'Photographer')
    )
    profile_category = forms.ChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone_number', 'profile_category', 'first_name')
        labels = {
            'first_name': 'Name',
            'username': 'Email Address'
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class DateInput(forms.DateInput):
    input_type = 'date'


class InfluencerForm(forms.ModelForm):
    class Meta:
        model = InfluencerList
        exclude = ['account', 'email']
        labels = {
            'location': 'Address',
        }
        widgets = {
            'dob': DateInput(),
            'sms_agency_name': forms.TextInput(attrs={'placeholder': 'Agency Name'}),
            'sms_agent_name': forms.TextInput(attrs={'placeholder': 'Agent Name'}),
            'sms_agent_email': forms.EmailInput(attrs={'placeholder': 'Your Agent Email ID'}),
            'sms_agent_number': forms.TextInput(attrs={'placeholder': 'Agent Number'}),
            'mdi_old_age': forms.TextInput(attrs={'placeholder': 'Age of your oldest child'}),
            'mdi_young_age': forms.TextInput(attrs={'placeholder': 'Age of your youngest child'}),
            'free_assign_done': forms.TextInput(attrs={'placeholder': 'No of Assignments Done'}),
            'free_no_experience': forms.TextInput(attrs={'placeholder': 'No of years of experience'}),
            'free_date_assign': forms.TextInput(attrs={'placeholder': 'Date of Last Assignment'}),
            'ca_college_name': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'ca_capacity': forms.TextInput(attrs={'placeholder': 'What capacity were/are you involved'}),
            'ca_committee': forms.TextInput(attrs={'placeholder': 'Which committees/societies'}),
            'ca_course': forms.TextInput(attrs={'placeholder': 'Course'}),
            'ca_worked_hobnob': forms.TextInput(attrs={'placeholder': 'Have You Worked with Hobnob'}),
            'wp_company_name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'wp_designation': forms.TextInput(attrs={'placeholder': 'Designation'}),
            'gender': forms.Select(attrs={'class': 'select'}),
            'instagram_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'instagram_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'twitter_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'twitter_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'fb_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'fb_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'youtube_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'youtube_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'linkedin_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'linkedin_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'snapchat_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'snapchat_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'pinterest_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'pinterest_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'tumbler_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'tumbler_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'github_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'github_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'dribble_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'dribble_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'reddit_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'reddit_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
        }


class PhotographerForm(forms.ModelForm):
    class Meta:
        model = PhotographerList
        fields = "__all__"
        labels = {
            'location': 'Address',
        }
        widgets = {
            'dob': DateInput(),
            'sms_agency_name': forms.TextInput(attrs={'placeholder': 'Agency Name'}),
            'sms_agent_name': forms.TextInput(attrs={'placeholder': 'Agent Name'}),
            'sms_agent_email': forms.EmailInput(attrs={'placeholder': 'Your Agent Email ID'}),
            'sms_agent_number': forms.TextInput(attrs={'placeholder': 'Agent Number'}),
            'free_assign_done': forms.TextInput(attrs={'placeholder': 'No of Assignments Done'}),
            'free_no_experience': forms.TextInput(attrs={'placeholder': 'No of years of experience'}),
            'free_date_assign': forms.TextInput(attrs={'placeholder': 'Date of Last Assignment'}),
            'ca_college_name': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'ca_capacity': forms.TextInput(attrs={'placeholder': 'What capacity were/are you involved'}),
            'ca_committee': forms.TextInput(attrs={'placeholder': 'Which committees/societies'}),
            'ca_course': forms.TextInput(attrs={'placeholder': 'Course'}),
            'ca_worked_hobnob': forms.TextInput(attrs={'placeholder': 'Have You Worked with Hobnob'}),
            'wp_company_name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'wp_designation': forms.TextInput(attrs={'placeholder': 'Designation'}),
            'gender': forms.Select(attrs={'class': 'select'}),
            'instagram_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'instagram_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'twitter_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'twitter_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'fb_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'fb_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'youtube_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'youtube_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'linkedin_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'linkedin_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'snapchat_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'snapchat_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'pinterest_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'pinterest_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'tumbler_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'tumbler_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'github_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'github_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'dribble_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'dribble_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
            'reddit_username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'reddit_followers': forms.TextInput(attrs={'placeholder': 'No of followers'}),
        }

    def __str__(self):
        self.email = User.objects.order_by('-id')[0].email
