from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib import messages
from .models import User, StudentProfile, TeacherProfile
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.db import models
from django.views.generic.detail import DetailView
from .models import User

class ProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'  # à adapter à ton template


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        # Create profile based on user type
        if user.user_type == 'student':
            StudentProfile.objects.create(user=user, student_id=f"STU{user.id:05d}")
        elif user.user_type == 'teacher':
            TeacherProfile.objects.create(user=user, department="Non spécifié")
        
        messages.success(self.request, 'Compte créé avec succès!')
        return redirect('accounts:dashboard')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'accounts/edit_profile.html'
    
    def get_object(self):
        return self.request.user

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        if user.user_type == 'student':
            from binomes.models import Binome, BinomeRequest
            context['my_binome'] = Binome.objects.filter(
                models.Q(student1=user) | models.Q(student2=user)
            ).first()
            context['pending_requests'] = BinomeRequest.objects.filter(
                to_student=user, status='pending'
            ).count()
        
        elif user.user_type == 'teacher':
            from projects.models import Project
            context['my_projects'] = Project.objects.filter(teacher=user)
        
        return context

