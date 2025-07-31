from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from .models import Binome, BinomeRequest
from accounts.models import User

class BinomeListView(LoginRequiredMixin, ListView):
    template_name = 'binomes/list.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        # Show available students (not already in a binome)
        return User.objects.filter(
            user_type='student'
        ).exclude(
            Q(binome_as_student1__status='accepted') | 
            Q(binome_as_student2__status='accepted')
        ).exclude(id=self.request.user.id)

class BinomeRequestListView(LoginRequiredMixin, ListView):
    template_name = 'binomes/requests.html'
    context_object_name = 'requests'
    
    def get_queryset(self):
        return BinomeRequest.objects.filter(
            to_student=self.request.user,
            status='pending'
        )

@login_required
def send_binome_request(request, user_id):
    to_student = get_object_or_404(User, id=user_id, user_type='student')
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        BinomeRequest.objects.get_or_create(
            from_student=request.user,
            to_student=to_student,
            defaults={'message': message}
        )
        messages.success(request, f'Demande envoyée à {to_student.get_full_name()}')
    
    return redirect('binomes:list')

@login_required
def accept_binome_request(request, request_id):
    binome_request = get_object_or_404(BinomeRequest, id=request_id, to_student=request.user)
    
    binome_request.status = 'accepted'
    binome_request.save()
    
    # Create binome
    Binome.objects.create(
        student1=binome_request.from_student,
        student2=binome_request.to_student,
        status='accepted'
    )
    
    messages.success(request, f'Binôme formé avec {binome_request.from_student.get_full_name()}!')
    return redirect('binomes:requests')

@login_required
def reject_binome_request(request, request_id):
    binome_request = get_object_or_404(BinomeRequest, id=request_id, to_student=request.user)
    binome_request.status = 'rejected'
    binome_request.save()
    
    messages.info(request, 'Demande refusée.')
    return redirect('binomes:requests')
