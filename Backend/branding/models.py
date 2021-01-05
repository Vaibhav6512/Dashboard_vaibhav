from django.db import models

class Branding(models.Model):
    role_model = models.CharField(max_length=100, null=False, blank=False)
    secret_person = models.CharField(max_length=100, null=False, blank=False)
    friend_say = models.CharField(max_length=100, null=False, blank=False)
    question_ask = models.CharField(max_length=100, null=False, blank=False)
    nerver_say = models.CharField(max_length=100, null=False, blank=False)
    achievement = models.CharField(max_length=100, null=False, blank=False)
    failure = models.CharField(max_length=100, null=False, blank=False)

    learn_failure = models.CharField(max_length=100, null=False, blank=False)
    things_proud = models.CharField(max_length=100, null=False, blank=False)
    change_about = models.CharField(max_length=100, null=False, blank=False)
    first_things = models.CharField(max_length=100, null=False, blank=False)
    abstacle = models.CharField(max_length=100, null=False, blank=False)
    waste_time = models.CharField(max_length=100, null=False, blank=False)
    ritual = models.CharField(max_length=100, null=False, blank=False)

    favourite_place = models.CharField(max_length=100, null=False, blank=False)
    prefer = models.CharField(max_length=100, null=False, blank=False)
    happiest_period = models.CharField(max_length=100, null=False, blank=False)
    memory = models.CharField(max_length=100, null=False, blank=False)
    game = models.CharField(max_length=100, null=False, blank=False)
    injustice = models.CharField(max_length=100, null=False, blank=False)
    perfect_day = models.CharField(max_length=100, null=False, blank=False)

    take_time = models.CharField(max_length=100, null=False, blank=False)
    greatfull = models.CharField(max_length=100, null=False, blank=False)
    average_life = models.CharField(max_length=100, null=False, blank=False)
    marriage = models.CharField(max_length=100, null=False, blank=False)
    invent = models.CharField(max_length=100, null=False, blank=False)
    illegal = models.CharField(max_length=100, null=False, blank=False)
    discover = models.CharField(max_length=100, null=False, blank=False)

