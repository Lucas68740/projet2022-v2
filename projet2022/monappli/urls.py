from django.urls import path

from . import views

urlpatterns = [
    path("bonjour/",views.bonjour),
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("", views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/",views.update),
    path("updatetraitement/", views.updatetraitement),
    path("delete/<int:id>/", views.delete),

]
