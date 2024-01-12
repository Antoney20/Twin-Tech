from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.EmailField()
    skills = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)


class Job(models.Model):
    JOB_LOCATIONS = [
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
    ]

    title = models.CharField(max_length=100)
    requirements = models.CharField(max_length=255)  
    experience_required = models.IntegerField()
    location = models.CharField(max_length=10, choices=JOB_LOCATIONS)
    image = models.FileField(upload_to='job_poster/', null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)