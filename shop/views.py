# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from models import Category, Item
import json

def shop(request):
    categories = Category.objects.all()
    for category in categories:
        category.items = Item.objects.filter(category__id=category.id)
    return render(request, 'shop/shop.html', {'categories': categories})

def checkout(request):
    cartInput = request.POST.get("cart")
    total = request.POST.get("total")
    return render(request, 'shop/checkout.html', {'cart_input': cartInput, 'total': total})

def placeorder(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    comment = request.POST.get("comment")
    cart = json.loads(request.POST.get("cart"))
    total = request.POST.get("total")

    buyed = ""
    for item in cart:
        buyed += u"%s ціна: %f; кількість: %d" % (item[u"name"], item[u"price"], item[u"quantity"])

    subject = u"Замовлення від %s " % name
    body = u"""
    Ім'я %s
    Номер телефону: %s
    Електронна адреса: %s
    Коментар: %s

    Придбав: %s
    Сумма: %s
    """ % (name, phone, email, comment, buyed, total)

    success = True
    try:
        send_mail(subject, body, "info@getmanstudio.com", ["getmanstudio@gmail.com", "a@mailinator.com"], fail_silently=False)
    except:
        success = False

    categories = Category.objects.all()
    for category in categories:
        category.items = Item.objects.filter(category__id=category.id)
    return render(request, 'shop/shop.html', { "checkout": True, "success": success, "categories": categories })
