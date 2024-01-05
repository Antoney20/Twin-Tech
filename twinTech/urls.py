from django.urls import include, path
from . import views

urlpatterns = [
    
    path("", views.home, name="index"),
    path('job-listings/', views.job_listings, name='job_listings'), 
    
    path('submit-job/', views.submit_job, name='submit_job'),# adding a new job
    path('search-jobs/', views.search_jobs_view, name='search_jobs'), 
    path('candidate-profile/', views.candidate_profile, name='candidate_profile'), #show candidate profile
    path('save-profile/', views.save_profile, name='save_profile'),  # saving user 
    path('show-jobs-for-me/', views.show_jobs_for_me, name='show_jobs_for_me'), # available jobs for user 
    path('company-search/', views.company_search, name='company_search'),
    path('download-resume/<int:candidate_id>/', views.download_resume, name='download_resume'),  
    #login
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
   
]