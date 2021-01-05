def branding(request):
    if request.method == 'POST':

        form = BrandingForm(request.POST)

        if form.is_valid():
            fx = form.cleaned_data
            x = BrandingForm(
                brand_logo = fx['brand_logo'],
                brand_name = fx['brand_name'],
                tag_line = fx['tag_line'],
                title_1_tag_line = fx['title_1_tag_line'],
                description = fx['description'],
                phone_number = fx['phone_number'],
                heading = fx['heading'],
                gender = fx['gender'],
                age_range = fx['age_range'],
                location = fx['location'],
                social_media_required = fx['social_media_required'],
                minimum_fellowship_required = fx['minimum_fellowship_required']
            )

            try:
                x.save()
            except IntegrityError:
                raise Http404("Integrity Error")
            else:
                return HttpResponse("Campaign Created")
        else:
            return HttpResponse('Form is not valid')
    else:
        form = CampaignForm()

    return render(request,"campaigns/campaign-new.html",{'form': form})
