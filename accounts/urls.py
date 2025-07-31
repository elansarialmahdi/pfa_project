from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileDetailView 

app_name = 'accounts'



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    
    

    
]