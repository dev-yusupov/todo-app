# TODO-APP

#### This is a Todo-app made by [Bobur Yusupov](https://github.com/dev-yusupov) in 2023

This is <b>Official documentation</b>

To run the app follow the steps below

1. Clone the repository
   ```
   git clone https://github.com/dev-yusupov/todo-app.git
   ```
2. Enter to the folder:
   ```
   cd todo-app
   ```
3. To run backend server in local machine:
   ```
   cd backend
   .venv\scripts\activate.bat (for Windows CMD)
   pip install -r requirements.txt
   python manage.py runserver
   ```
4. Now run Angular Server:
    ```
    cd frontend
    npm install
    npm install angular
    ng serve
    ```

# Backend
#### Backend is built in Python ([Django](https://djangoproject.com) and [Django REST Framework](https://www.django-rest-framework.org/))

Backend has following apps:
 - Accounts
 - Todo

Inside Accounts app following Model and Manager will be created

User:
-
 - Email
 - First Name
 - Last Name
 - Username
 - Password1
 - Password2

UserManager:
-
 - create_user()


##Todo App:

Model:
-
 - Task
 - Category
 - Tag

Task model:
-
 - Title
 - Description (optional)
 - Start Date
 - End Data
 - Category
 - User
 - Tag

Category model:
 -
 - Title
 - Description

Tag model:
 - 
 - name

Manager:
 - 
 - create_task()
 - create_category()