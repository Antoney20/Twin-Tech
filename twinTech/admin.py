from django.contrib import admin

# Register your models here.
from .models import CandidateProfile, Job

admin.site.register(CandidateProfile),
admin.site.register(Job),