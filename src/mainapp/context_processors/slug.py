from mainapp.models import Club

def slug(request):
    slug = request.path.split("/")[1]
    clubs = [(str(club.slug)) for club in Club.objects.all()]
    if slug not in clubs:
        # slug = None
        club = Club.objects.get(order=0)
        slug = str(club.slug)

    return {"slug": slug}
