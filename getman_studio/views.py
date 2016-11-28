from django.shortcuts import render
from models import Category, GalleryItem, Article, WorkshopParallaxItem

def gallery(request):
    categories = Category.objects.all();
    gitems = GalleryItem.objects.all();
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': gitems})

def workshop(request):
    articles = Article.objects.all()
    parallaxItems = list(WorkshopParallaxItem.objects.all())

    firstParallax = None
    lastParallax = None
    if (len(parallaxItems) >= 2):
        firstParallax = parallaxItems.pop(0)
        lastParallax = parallaxItems.pop(-1)

    particles = {}
    for i, article in enumerate(articles):
        i = i + 1
        if i % 2 == 0 and i < articles.count() and len(parallaxItems) > i / 2:
            particles[article] = parallaxItems[i / 2]
        else:
            particles[article] = None

    print str(particles)
    return render(request, 'workshop/workshop.html', { 'firstParallax': firstParallax, 'lastParallax': lastParallax, 'particles': particles })

def contacts(request):
    return render(request, 'contacts/contacts.html')
