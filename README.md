# Twin-Tech
AI powered job search application
# Twin-Tech Job Marketplace

## Overview
Twin-Tech is an AI-powered job marketplace platform that matches job seekers with their ideal twin technology jobs based on their skill set, experience, and preferences. The platform offers personalized guidance to interns in the twin technology industry, helping them optimize their job search strategies and career development. Companies can scan resumes and profiles to identify the most suitable candidates for job openings.

## Setup

### Prerequisites
- Python 3.x installed
- Django installed
- Virtual environment (optional - we are good to go.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Antoney20/Twin-Tech.git  
   cd project ```

   Optionally, you can download the Zip folder, and extract the contents of the project.

## Database Setup.
- Here we are primarily using MySQLite as our default DB.
* steps;
1.   Apply migrations, (optional)
Run the following commands. 
    ``` bash
    python manage.py makemigrations
    python manage.py migrate        

2. Create super-user (Optional);

    ```python manage.py createsuperuser```
follow the prompts to create your own ADMIN,  you can also use my already created credentials.

# Running the application. 

1. Starting the development server/ Localhost. 

python manage.py runserver
# The application will be accessible under localhost.  http://localhost:8000/.
Access the admin panel:

# Visit http://localhost:8000/admin/
Log in with the superuser credentials created earlier.
Access the main application:

# Visit http://localhost:8000/
Explore and test the features.

# Happy coding:
