
## Setup Instructions for the Library Management System

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:<br>
   ```bash
   git clone <repository-url>
   cd library_management_system
Create a Virtual Environment:<br>
It is recommended to create a virtual environment to manage dependencies. You can create one using:<br>

python -m venv venv<br>
Activate the Virtual Environment:<br>
Activate the virtual environment with the following command:<br>

venv\Scripts\activate<br>

Install Dependencies:<br>
pip install django mysqlclient<br>

Configure Database:<br>
Update the database settings in library_management_system/settings.py:<br>

Ensure the DATABASES section is configured correctly with your MySQL credentials:<br>
DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.mysql',<br>
        'NAME': 'library_db',  # Change this to your database name<br>
        'USER': 'root',        # Change this to your MySQL username<br>
        'PASSWORD': '12345',   # Change this to your MySQL password<br>
        'HOST': 'localhost',<br>
        'PORT': '3306',<br>
    }<br>
}<br>
Run Migrations:<br>
Apply the database migrations to set up the initial database structure:<br>

python manage.py migrate<br>

Run the Development Server:<br>
Start the Django development server with the following command:<br>

python manage.py runserver<br>
Access the Application:<br>
Open your web browser and go to http://127.0.0.1:8000/ to access the application. <br>
