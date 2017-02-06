def slug(request):
    slug = request.path.split("/")[1]
    if slug != "furmanova":
        slug = "comsomoll"
    return {"slug": slug}
