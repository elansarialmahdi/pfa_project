from django.urls import path
from . import views

app_name = 'binomes'

urlpatterns = [
    path('', views.BinomeListView.as_view(), name='list'),
    path('requests/', views.BinomeRequestListView.as_view(), name='requests'),
    path('request/<int:user_id>/', views.send_binome_request, name='send_request'),
    path('accept/<int:request_id>/', views.accept_binome_request, name='accept_request'),
    path('reject/<int:request_id>/', views.reject_binome_request, name='reject_request'),
]