from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.ConversationListView.as_view(), name='list'),
    path('<int:pk>/', views.ConversationDetailView.as_view(), name='detail'),
    path('notifications/', views.NotificationListView.as_view(), name='notifications'),
    path('create/', views.ConversationCreateView.as_view(), name='create'),

]