College Complaint Portal

A simple web application built to make handling college complaints easier.

The idea behind this project is pretty straightforward: students should have a place where they can submit complaints or suggestions, while  administrators can view them and respond accordingly.

I built this project as a Django-based project, with separate functionality for students and administrators.

Live Website

https://complaint-portal-txh4.onrender.com

What It Can Do

- Students can create an account and log in
- Students can submit complaints
- Complaints can be categorized as Faculty, College, Suggestion, or Other
- Students can view their complaint history
- Administrators can add, edit, view, and delete teacher records
- Teachers and administrators can view complaints
- Complaints can be replied to
- Student and teacher information can be managed through the portal

User Roles

Student

Students can:

- Register and log in
- Submit complaints
- Choose a complaint category
- View previously submitted complaints
- Check their complaint history

Administrator

The administrator has access to the management side of the portal and can:

- Manage teachers
- View students
- Manage complaints
- Respond to complaints
- Edit and remove teacher information

Tech Stack

This project was built using:

- Python
- Django
- PostgreSQL
- HTML
- CSS
- Gunicorn
- WhiteNoise
- Render

How the Project Works

The application is built with Django. The frontend provides the different pages for students, teachers, and administrators, while Django handles the application logic and database operations.

For the deployed version, PostgreSQL is used as the database and Render is used to host the application.

Running It Locally

Clone the repository:

git clone https://github.com/pip-DRGN0/demo.git
cd demo

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Run the database migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Then open:

http://127.0.0.1:8000/

Deployment

The project is deployed on Render.

Build command:

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

Start command:

gunicorn djangoproject.wsgi:application

The production database connection is handled using the "DATABASE_URL" environment variable.

Other environment variables used by the application include:

DATABASE_URL
SECRET_KEY
DEBUG
ALLOWED_HOSTS

Sensitive values should not be committed to GitHub.

Complaint Categories

Currently, complaints can be classified as:

- Faculty
- College
- Suggestion
- Other

Things I Want to Improve

There are still a few things I would like to add or improve in the future:

- Email notifications when a complaint is updated
- Complaint status tracking
- Better search and filtering
- File and image attachments
- A more detailed admin dashboard
- Better authentication and password security
- More refined mobile responsiveness
- Teacher specific section 

About

It started as a simple idea for managing college complaints and was developed into a working Django application with a PostgreSQL database and a live deployment.

Author

Karthik Sudhakaran