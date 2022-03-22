# Authentication and registration in Django
Application with two functions - authorization and authentication. I'll use code from here in my future applications.

## Description

### Registation

You need to fill form with four fields: username, email, password and password confirmation.
Password shouldn't be entirely numeric, use common words and phrases and less than 8 characters long.

If form was filled right, you'll be redirected to login form and you'll see a message about successful account creation.

If user is already authenticated, he cannot visit this page. He'll be redirected to main page.

### Login

You need to fill form with two fields: username and password. If user does not exist, you'll see an error message.

If user exists in database, you'll be redirected logged in to main page.

If user is already authenticated, he cannot visit this page. He'll be redirected to main page.

### Logout

Just click the button on main page while you are logged in and you'll be redirected logged out to login page.

## Installation

1. Copy a repository on your computer.
2. Create a virtual environment with `python -m venv venv`.
3. Activate it using `./venv/Scripts/activate`.
4. Install requirements with `pip install -r requirements.txt`.
5. Change your directory to `Auth_Django` using `cd Auth_Django`.
6. Apply all migrations using `python manage.py makemugrations` & `python manage.py migrate`.
7. Launch application with `python manage.py runserver` and follow the link `http://127.0.0.1:8000`.
