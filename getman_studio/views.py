from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, GalleryItem, Article, WorkshopParallaxItem


def gallery(request):
    categories = Category.objects.filter(active=True);
    gitems = GalleryItem.objects.all();
    return render(request, 'gallery/gallery.html', {'categories': categories, 'items': gitems})


def workshop(request, page="1"):
    print("page: " + page)
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 3)
    parallax_items = list(WorkshopParallaxItem.objects.all())
    articles = paginator.page(page).object_list

    first_parallax = None
    last_parallax = None
    if len(parallax_items) >= 1:
        first_parallax = parallax_items.pop(0)
    if len(parallax_items) >= 2:
        last_parallax = parallax_items.pop(-1)

    x = 0
    for article in articles:
        i = x + 1
        if i % 2 == 0 and i < articles.count() and len(parallax_items) > i / 2:
            article.parallax = parallax_items[i / 2]
        x += 1

    print(str(articles))
    return render(request, 'workshop/workshop.html', {'firstParallax': first_parallax, 'lastParallax': last_parallax,
                                                      'articles': articles, 'currentpage': int(page),
                                                      'pages': range(1, paginator.num_pages + 1)})


def contacts(request):
    return render(request, 'contacts/contacts.html')
