from .models import Job, CandidateProfile

def filter_jobs(salary=None, title=None, location=None, keywords=None):
    jobs = Job.objects.all()

    if salary:
        jobs = jobs.filter(salary__gte=salary)

    if title:
        jobs = jobs.filter(title__icontains=title)

    if location:
        jobs = jobs.filter(location=location)

    if keywords:
        keywords_list = keywords.split(',')
        for keyword in keywords_list:
            jobs = jobs.filter(requirements__icontains=keyword)

    return jobs

def search_jobs(query):
    return Job.objects.filter(title__icontains=query)

def match_jobs(user):
    candidate_profile = CandidateProfile.objects.get(user=user)
    user_skills = set(candidate_profile.skills.split(','))

    matching_jobs = []

    for job in Job.objects.all():
        job_skills = set(job.requirements.split(','))
        if user_skills.intersection(job_skills):
            matching_jobs.append(job)

    return matching_jobs
        
#candidate search

def search_candidates(skills):
    return CandidateProfile.objects.filter(skills__icontains=skills)