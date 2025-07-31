from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.urls import reverse

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Étudiant'),
        ('teacher', 'Professeur'),
        ('admin', 'Administrateur'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    phone = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField(max_length=500, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)
    def get_absolute_url(self):
        return reverse('edit_profile')




class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    level = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    skills = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.student_id}"

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    expertise = models.TextField()
    office = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"Prof. {self.user.get_full_name()}"
