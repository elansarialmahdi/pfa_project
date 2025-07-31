from django.db import models
from django.conf import settings

class Binome(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('accepted', 'Accepté'),
        ('rejected', 'Refusé'),
    ]
    
    student1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='binome_as_student1')
    student2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='binome_as_student2', null=True, blank=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='binomes', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_validated_by_teacher = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['student1', 'student2']
    
    def __str__(self):
        if self.student2:
            return f"{self.student1.get_full_name()} & {self.student2.get_full_name()}"
        return f"{self.student1.get_full_name()} (Solo)"

class BinomeRequest(models.Model):
    from_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    to_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_requests')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Accepté'),
        ('rejected', 'Refusé'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['from_student', 'to_student']