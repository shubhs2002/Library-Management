## PROBLEM STATEMENT
**Library Management System** <br>
Brief:<br>
You have to build a library management system using Django where an admin can
perform CRUD ( create, read, update and delete) operations like <br>
● Add a Book<br>
● Update an entry of a book<br>
● Delete a book<br>
● Get all books<br><br>
Develop web services using Python (Django Framework)
and front end technologies which can be used for the front end.<br>
1. Admin Signup:<br>
a) Insert admin details in tables.<br>
b) An admin records should be unique based on email, which means
duplicates records should not be able to enter in DB.<br><br>
2. Admin Login:<br>
a) The Admin can log in based on email and password.<br><br>
3. Create an entry for Books.<br>
a) The admin can create a new entry of a book.<br><br>
4. Retrieve all the books.<br>
a) Retrieve all the books.<br><br>
5. Update a book.<br>
a) The book records should be able to update.<br><br>
6. Delete a book.<br>
a) The book record should be deleted<br><br>
Student View:<br>
1. View all the records of book <br><br>
Conditions:<br>
1. For Front end, you can use any library / framework to build the UI.<br>
2. Write the documentation for backend code.<br>
3. Use MySQL database to store the data<br><br><br>
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
