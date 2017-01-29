from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shop/checkout/', views.checkout, name='checkout'),
    url(r'^shop/placeorder/', views.placeorder, name='placeorder'),
]
