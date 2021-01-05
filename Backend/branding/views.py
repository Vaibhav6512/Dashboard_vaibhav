from django.shortcuts import render
from branding.forms import BrandingForm
from django.http import HttpResponse
from branding import models


# Create your views here.
def branding(request):
    form = BrandingForm()
    return render(request,'branding.html',{'form': form})
    
def brandAdd(request):
    if request.method == 'POST':
        form = BrandingForm(request.POST)
        brand = models.Branding()
        if form.is_valid():
            fx = form.cleaned_data
            # x = BrandingForm(
            brand.role_model = fx['Who_is_your_role_model_and_why_do_they_inspire_you'],
            brand.secret_person = fx['Who_is_the_person_who_knows_all_your_secrets'],
            brand.friend_say = fx['What_would_your_friends_say_about_you'],
            brand.question_ask = fx['What_is_the_question_people_ask_you_most_often'],
            brand.nerver_say = fx['what_is_the_thing_you_did_never_say_to_another_person'],
            brand.achievement = fx['what_is_your_greatest_achievement'],
            brand.failure = fx['what_is_your_greatest_failure'],

            brand.learn_failure = fx['What_did_you_learn_from_your_greatest_failure'],
            brand.things_proud = fx['What_is_the_things_you_are_most_proud_of'],
            brand.change_about = fx['What_would_you_like_to_change_about'],
            brand.first_things = fx['If_something_in_your_house_breaker_what_is_the_first_things_you_do'],
            brand.abstacle = fx['what_is_the_greatest_obstacles_you_have_facing_right_now'],
            brand.waste_time = fx['what_is_the_greatest_obstacles_you_have_facing_right_now'],
            brand.ritual = fx['What_is_the_ritual_that_helps_you_calm_down'],

            brand.favourite_place = fx['what_is_your_favourite_place_in_town'],
            brand.prefer = fx['What_do_you_prefer_a_book_movie_or_a_theatre_play'],
            brand.happiest_period = fx['What_was_the_happiest_period_of_your_life'],
            brand.memory = fx['what_is_your_most_preasured_memory_from_childhood'],
            brand.game = fx['What_was_your_favourite_game_when_you_were_child'],
            brand.injustice = fx['What_is_the_greatest_injustice_you_have_lined_through'],
            brand.perfect_day = fx['What_does_a_perfect_day_look_like_to_you'],

            brand.take_time = fx['Before_you_all_someone_do_you_take_time_to_think_about_what_you_are_going_to_say_to_them'],
            brand.greatfull = fx['What_is_the_one_thing_you_are_most_greatfull_for_in_your_entire_life'],
            brand.average_life = fx['If_the_average_life_span_is_40_ear_how_would_you_live_your_life_differently'],
            brand.marriage = fx['Would_you_rather_be_married_in_an_arranged_marriage_or_spend_the_rest_of_your_life_single'],
            brand.invent = fx['If_you_could_invent_anything_what_could_it_be_and_why'],
            brand.illegal = fx['Would_you_rather_have_50_lakhs_free_and_clear_or_one_crore_that_is_illegal'],
            brand.discover = fx['Would_you_rather_discover_something_great_and_share_it_or_discover_something_evil_and_prevent_it'],
            # )

            try:
                brand.save()
            except IntegrityError:
                raise Http404("Integrity Error")
            else:
                return HttpResponse("Brand Created")   
        else:
            return HttpResponse('Form is not valid')
    else:
        form = CampaignForm()

    return render(request,"branding.html",{'form': form})