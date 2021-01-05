from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    choices = (
        ('Influencer', 'Influencer'),
        ('Makeup Artist', 'Makeup Artist'),
        ('Photographer', 'Photographer')
    )

    profile_category = models.CharField(max_length=255, choices=choices)

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('accounts:reports_detail', kwargs={"pk": self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Accounts.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.accounts.save()


class InfluencerList(models.Model):
    account = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='signup/profile_pictures')
    name = models.CharField(max_length=50, blank=False)
    email = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    dob = models.DateField(blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.TextField(max_length=500, blank=False)
    cat1 = "Social Media Star"
    cat2 = "Mom/Dad Influencer"
    cat3 = "Free Lancer"
    cat4 = "Campus Ambassador"
    cat5 = "Working Professional"
    CATEGORY_CHOICES = (
        (cat1, "Social Media Star"), (cat2, "Mom/Dad Influencer"), (cat3, "Free Lancer"), (cat4, "Campus Ambassador"),
        (cat5, "Working Professional"))
    category = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=40)

    instagram_username = models.CharField(max_length=256, default="")
    instagram_followers = models.IntegerField()

    twitter_username = models.CharField(max_length=256, blank=True, null=True)
    twitter_followers = models.IntegerField(blank=True, null=True)

    fb_username = models.CharField(max_length=256, blank=True, null=True)
    fb_followers = models.IntegerField(blank=True, null=True)

    youtube_username = models.CharField(max_length=256, blank=True, null=True)
    youtube_followers = models.IntegerField(blank=True, null=True)

    linkedin_username = models.CharField(max_length=256, blank=True, null=True)
    linkedin_followers = models.IntegerField(blank=True, null=True)

    snapchat_username = models.CharField(max_length=256, blank=True, null=True)
    snapchat_followers = models.IntegerField(blank=True, null=True)

    pinterest_username = models.CharField(max_length=256, blank=True, null=True)
    pinterest_followers = models.IntegerField(blank=True, null=True)

    tumbler_username = models.CharField(max_length=256, blank=True, null=True)
    tumbler_followers = models.IntegerField(blank=True, null=True)

    github_username = models.CharField(max_length=256, blank=True, null=True)
    github_followers = models.IntegerField(blank=True, null=True)

    dribble_username = models.CharField(max_length=256, blank=True, null=True)
    dribble_followers = models.IntegerField(blank=True, null=True)

    reddit_username = models.CharField(max_length=256, blank=True, null=True)
    reddit_followers = models.IntegerField(blank=True, null=True)

    fashion = models.BooleanField(default=True)
    beautyandmakeup = models.BooleanField(default=False)
    automobile = models.BooleanField(default=False)
    arts = models.BooleanField(default=False)
    movieandtv = models.BooleanField(default=False)
    foodandbeverage = models.BooleanField(default=False)
    musicanddance = models.BooleanField(default=False)
    lifestyle = models.BooleanField(default=False)
    technology = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)
    businessandstartup = models.BooleanField(default=False)
    educationandcareer = models.BooleanField(default=False)
    societyandpolitics = models.BooleanField(default=False)
    fitnessandhealth = models.BooleanField(default=False)
    marketingandsocialmedia = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    photography = models.BooleanField(default=False)

    bank_Full_Name = models.CharField(max_length=256, default="")
    bank_acccount_number = models.BigIntegerField()
    bank_IFSC_code = models.CharField(max_length=11, default="")

    paytm_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    paytm_Number = models.IntegerField(blank=True, null=True)

    gpay_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    gpay_Number = models.IntegerField(blank=True, null=True)

    upi_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    upi_ID = models.CharField(max_length=60, blank=True, null=True)

    sms_agency_name = models.CharField(max_length=256, blank=True, null=True)
    sms_agent_name = models.CharField(max_length=256, blank=True, null=True)
    sms_agent_email = models.EmailField(blank=True, null=True)
    sms_agent_number = PhoneNumberField(blank=True, null=True)

    mdi_old_age = models.CharField(blank=True, null=True, max_length=30)
    mdi_young_age = models.CharField(blank=True, null=True, max_length=30)
    CHILD_CHOICES = (("Do you have an active social circle of friends in your neighborhood?",
                      "Do you have an active social circle of friends in your neighborhood?"),
                     ("Yes, I'm popular and I know it! :)", "Yes, I'm popular and I know it! :)"),
                     ("No, I'm new & just getting to know people", "No, I'm new & just getting to know people"), (
                         "Sort of, I have some friends, and keen to grow my circle of friends",
                         "Sort of, I have some friends, and keen to grow my circle of friends"))
    influencer_choice = models.CharField(choices=CHILD_CHOICES, blank=True, null=True, max_length=280)

    free_assign_done = models.CharField(blank=True, null=True, max_length=40)
    free_no_experience = models.CharField(blank=True, null=True, max_length=40)
    free_date_assign = models.CharField(blank=True, null=True, max_length=42)

    ca_college_name = models.CharField(blank=True, null=True, max_length=256)
    ca_capacity = models.CharField(blank=True, null=True, max_length=256)
    ca_course = models.CharField(blank=True, null=True, max_length=256)
    ca_committee = models.CharField(blank=True, null=True, max_length=256)
    YEAR_OF_STUDY = (("First Year", "First Year"), ("Second Year", "Second Year"), ("Third Year", "Third Year"),
                     ("Forth Year", "Forth Year"), ("Fifth Year", "Fifth Year"))
    ca_year_of_study = models.CharField(choices=YEAR_OF_STUDY, blank=True, null=True, max_length=100)
    ca_worked_hobnob = models.CharField(blank=True, null=True, max_length=45)

    wp_company_name = models.CharField(blank=True, null=True, max_length=256)
    wp_designation = models.CharField(blank=True, null=True, max_length=256)

    def __str__(self):
        return '{}\t{}'.format(self.name, self.category)


class PhotographerList(models.Model):
    account = models.OneToOneField(Accounts, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='signup/profile_pictures')
    name = models.CharField(max_length=50, blank=False)
    email = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    dob = models.DateField(blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.TextField(max_length=500, blank=False)
    cat1 = "Social Media Photographer"
    cat2 = "Free Lancer"
    cat3 = "Student"
    cat4 = "Working Professional"
    CATEGORY_CHOICES = (
        (cat1, cat1), (cat2, cat2), (cat3, cat3), (cat4, cat4),
    )
    category = models.CharField(choices=CATEGORY_CHOICES, blank=False, max_length=40)

    instagram_username = models.CharField(max_length=256, default="")
    instagram_followers = models.IntegerField()

    twitter_username = models.CharField(max_length=256, blank=True, null=True)
    twitter_followers = models.IntegerField(blank=True, null=True)

    fb_username = models.CharField(max_length=256, blank=True, null=True)
    fb_followers = models.IntegerField(blank=True, null=True)

    youtube_username = models.CharField(max_length=256, blank=True, null=True)
    youtube_followers = models.IntegerField(blank=True, null=True)

    linkedin_username = models.CharField(max_length=256, blank=True, null=True)
    linkedin_followers = models.IntegerField(blank=True, null=True)

    snapchat_username = models.CharField(max_length=256, blank=True, null=True)
    snapchat_followers = models.IntegerField(blank=True, null=True)

    pinterest_username = models.CharField(max_length=256, blank=True, null=True)
    pinterest_followers = models.IntegerField(blank=True, null=True)

    tumbler_username = models.CharField(max_length=256, blank=True, null=True)
    tumbler_followers = models.IntegerField(blank=True, null=True)

    github_username = models.CharField(max_length=256, blank=True, null=True)
    github_followers = models.IntegerField(blank=True, null=True)

    dribble_username = models.CharField(max_length=256, blank=True, null=True)
    dribble_followers = models.IntegerField(blank=True, null=True)

    reddit_username = models.CharField(max_length=256, blank=True, null=True)
    reddit_followers = models.IntegerField(blank=True, null=True)

    landscape = models.BooleanField(default=True)
    macro = models.BooleanField(default=False)
    model_shoot = models.BooleanField(default=False)
    photo_jounalism = models.BooleanField(default=False)
    product_shoot = models.BooleanField(default=False)
    real_estate = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    wedding = models.BooleanField(default=False)
    wildlife = models.BooleanField(default=False)
    aerial = models.BooleanField(default=False)
    films = models.BooleanField(default=False)

    bank_Full_Name = models.CharField(max_length=256, default="")
    bank_acccount_number = models.BigIntegerField()
    bank_IFSC_code = models.CharField(max_length=11, default="")

    paytm_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    paytm_Number = models.IntegerField(blank=True, null=True)

    gpay_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    gpay_Number = models.IntegerField(blank=True, null=True)

    upi_Full_Name = models.CharField(max_length=256, blank=True, null=True)
    upi_ID = models.CharField(max_length=60, blank=True, null=True)

    sms_agency_name = models.CharField(max_length=256, blank=True, null=True)
    sms_agent_name = models.CharField(max_length=256, blank=True, null=True)
    sms_agent_email = models.EmailField(blank=True, null=True)
    sms_agent_number = PhoneNumberField(blank=True, null=True)

    free_assign_done = models.CharField(blank=True, null=True, max_length=40)
    free_no_experience = models.CharField(blank=True, null=True, max_length=40)
    free_date_assign = models.CharField(blank=True, null=True, max_length=42)

    ca_college_name = models.CharField(blank=True, null=True, max_length=256)
    ca_capacity = models.CharField(blank=True, null=True, max_length=256)
    ca_course = models.CharField(blank=True, null=True, max_length=256)
    ca_committee = models.CharField(blank=True, null=True, max_length=256)
    YEAR_OF_STUDY = (("First Year", "First Year"), ("Second Year", "Second Year"), ("Third Year", "Third Year"),
                     ("Forth Year", "Forth Year"), ("Fifth Year", "Fifth Year"))
    ca_year_of_study = models.CharField(choices=YEAR_OF_STUDY, blank=True, null=True, max_length=100)
    ca_worked_hobnob = models.CharField(blank=True, null=True, max_length=45)

    wp_company_name = models.CharField(blank=True, null=True, max_length=256)
    wp_designation = models.CharField(blank=True, null=True, max_length=256)

    def __str__(self):
        return '{}\t{}'.format(self.name, self.category)
