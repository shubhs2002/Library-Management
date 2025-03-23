
## Setup Instructions for the Library Management System

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   cd library_management_system
Create a Virtual Environment:
It is recommended to create a virtual environment to manage dependencies. You can create one using:

python -m venv venv
Activate the Virtual Environment:
Activate the virtual environment with the following command:

venv\Scripts\activate

Install Dependencies:
pip install django mysqlclient

Configure Database:
Update the database settings in library_management_system/settings.py:

Ensure the DATABASES section is configured correctly with your MySQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',  # Change this to your database name
        'USER': 'root',        # Change this to your MySQL username
        'PASSWORD': '12345',   # Change this to your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run Migrations:
Apply the database migrations to set up the initial database structure:

python manage.py migrate
Create a Superuser (Optional):
If you want to access the Django admin panel, create a superuser:

python manage.py createsuperuser
Run the Development Server:
Start the Django development server with the following command:

python manage.py runserver
Access the Application:
Open your web browser and go to http://127.0.0.1:8000/ to access the application. If you created a superuser, you can access the admin panel at http://127.0.0.1:8000/admin/.
