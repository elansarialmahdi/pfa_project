from django.db import models
from django.conf import settings
from django.urls import reverse

class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('full', 'Complet'),
        ('closed', 'Fermé'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    prerequisites = models.TextField(blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    max_binomes = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def available_spots(self):
        return self.max_binomes - self.binomes.filter(status='accepted').count()
    from django.urls import reverse

    def get_absolute_url(self):
        return reverse('projects:detail', args=[str(self.id)])


