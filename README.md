
## Setup Instructions for the Library Management System

1. **Clone the Repository:** <br>
   Clone the repository to your local machine using the following command:<br>
   ```bash
   git clone <repository-url>
   cd library_management_system
2. **Create a Virtual Environment:** <br>
   python -m venv venv<br>

3. **Activate the Virtual Environment:** <br>
  venv\Scripts\activate<br>

4. **Install Dependencies:** <br>
   pip install django mysqlclient<br>

5. **Configure Database:** <br>
   Update the database settings in library_management_system/settings.py:<br>
   Ensure the DATABASES section is configured correctly with your MySQL credentials:<br>
   DATABASES = {<br>
       'default': {<br>
            'ENGINE': 'django.db.backends.mysql',<br>
            'NAME': 'library_db',  # Change this to your database name<br>
            'USER': 'root',        # Change this to your MySQL username<br>
            'PASSWORD': 'your_password',   # Change this to your MySQL password<br>
            'HOST': 'localhost',<br>
            'PORT': '3306',<br>
       }<br>
   }<br>
6. **Run Migrations:** <br>
   Apply the database migrations to set up the initial database structure:<br>
   python manage.py migrate<br>

7. **Run the Development Server:** <br>
   Start the Django development server with the following command:<br>

   python manage.py runserver<br>
   
9. **Access the Application:** <br>
   Open your web browser and go to http://127.0.0.1:8000/ to access the application. <br>
