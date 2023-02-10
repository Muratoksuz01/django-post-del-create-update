from django.urls import path
from .views import *
urlpatterns = [
    path('index/',post_index,name="index"),
    path('datail/<int:id>',post_datail,name="datail"),#datail/sayı bıradakı : sondaki view.py parametre olarak gönderdiğimiz deger
    path('<int:id>/update',post_update,name="update"),
    path('<int:id>/delete',post_delete,name="delete"),
    path('create/',post_create,name="create"),



]



