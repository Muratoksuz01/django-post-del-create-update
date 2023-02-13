from django.urls import path
from .views import *
urlpatterns = [
    path('index/',post_index,name="index"),
    path('create/',post_create,name="create"),
    path('<slug:slug>/',post_datail,name="datail"),#datail/sayı bıradakı : sondaki view.py parametre olarak gönderdiğimiz deger
    path('<slug:slug>/update/',post_update,name="update"),
    path('<slug:slug>/delete/',post_delete,name="delete"),



]



