
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('ajouter/', views.add_review, name='add_review'),
]
