from django.shortcuts import render
from models import Category, GalleryItem, Article, WorkshopParallaxItem

def gallery(request):
    items = {}
    categories = Category.objects.all();
    print "categories " + str(categories)
    for category in categories:
        try:
            items[category] = GalleryItem.objects.get(category = category)
        except:
            items[category] = []
        print str(category) + str(items)
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': items})

def workshop(request):
    articles = Article.objects.all()
    parallaxItems = list(WorkshopParallaxItem.objects.all())

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
