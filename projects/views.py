from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView




class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:project_list') 


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'
    paginate_by = 12
    
    def get_queryset(self):
        return Project.objects.filter(status='active').order_by('-created_at')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    context_object_name = 'project'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        messages.success(self.request, 'Projet créé avec succès!')
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/edit.html'
    
    def get_queryset(self):
        return Project.objects.filter(teacher=self.request.user)

@login_required
def apply_to_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Logic for applying to project
    messages.success(request, f'Candidature soumise pour le projet: {project.title}')
    return redirect('projects:detail', pk=pk)
