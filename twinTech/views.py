from django.shortcuts import render, redirect


# Create your views here.
import requests
from django.http import HttpResponse
from .models import Job
from .backend import filter_jobs, search_jobs, match_jobs,  search_candidates
from django.contrib.auth import authenticate, login, logout

#decorators.
from django.contrib.auth.decorators import login_required

def home(request):
    jobs = Job.objects.all()
    return render(request, 'twinTech/home.html',  {'jobs': jobs})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            pass

    return render(request, 'twinTech/Auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def candidate_profile(request):
    return render(request, 'twinTech/userprofile.html')

def save_profile(request):
    if request.method == 'POST':
        username = request.user
        job_title = request.POST.get('job_title')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        resume = request.POST.get('resume')
        experience = request.POST.get('experience')

        CandidateProfile.objects.create(
            user=username,
            job_title=job_title,
            email=email,
            skills=skills,
            resume = resume,
            experience = experience,
        )

        return redirect('job_listings')

    return redirect('candidate_profile')

def show_jobs_for_me(request):
    user = request.user
    matched_jobs = match_jobs(user)
    
    return render(request, 'twinTech/job_listings.html', {'listings': matched_jobs})


def job_listings(request):
    salary = request.GET.get('salary')
    title = request.GET.get('title')
    location = request.GET.get('location')
    keywords = request.GET.get('keywords')

    jobs = filter_jobs(salary=salary, title=title, location=location, keywords=keywords)
    
    return render(request, 'twinTech/job_listings.html', {'listings': jobs})

def search_jobs_view(request):
    query = request.GET.get('search')
    jobs = search_jobs(query)
    
    #context 
    return render(request, 'twinTech/job_listings.html', {'listings': jobs})

def submit_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        requirements = request.POST.get('requirements')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        salary = request.POST.get('salary')

        Job.objects.create(
            title=title,
            requirements=requirements,
            experience_required=experience,
            location=location,
            image = image,
            salary=salary
        )

        return redirect('job_listings')

    return render(request, 'twinTech/jobs.html')

def company_search(request):
    search_results = None

    if request.method == 'GET':
        skills = request.GET.get('skills')
        if skills:
            search_results = search_candidates(skills)

    return render(request, 'twinTech/company/talent_search.html', {'search_results': search_results})

def download_resume(request, candidate_id):
    candidate = CandidateProfile.objects.get(pk=candidate_id)
    if candidate.resume:
        file_path = settings.MEDIA_ROOT + candidate.resume.name
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/pdf")
            response['Content-Disposition'] = f'attachment; filename={candidate.user.username}_resume.pdf'
            return response
    else:
     
        return HttpResponse("No resume available.")