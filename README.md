# cs320-final-project-repo

# Potassium

## Project Description
Fall 2022 - Final project for the User Interace class
Project client: MicroGoo
The goal of this project is to implement the project idea of another group. Our clients' project idea was a comprehensive web service for the job searching process -- specifically in Computer Science. This web service addresses three main aspects of the cs job searching process: Leetcode preparation, task management, and links to other useful resources. Our web service has an application that lets users work on their own 'Leetcode question collections.' We already have 3 default collections built-in, all of which are really popular: Blind 75, NeetCode 150, NeetCode All. However, we only added a portion of each collection and not the entirety due to time constraints. Users also have the option to personalize their collections: add and delete questions and edit collection names. Users can also create their own custom collections. The second component is a task list manager that is essentially a to-do list. And finally there's a resource page that provides links to other useful information for the job searching process. 
For this project, Django and Python are used for server-side, HTML, CSS, Javascript and Bootstrap are used for client-side, and SQLite3 is used for the database. 

## Developer Bios
The two developers are Kevin Yuan and Moe Ko.
Both of the developers are students at The College of Wooster and are enrolled in the User Interface class. 

## Project Setup
First download or clone the repo.
In the parent directory, there should be a setup.sh bash script.
If you are on Mac, you can run the command 'source setup.sh' to automatically create venv and install dependencies.
Otherwise, you can manually create venv and install dependnecies, which are listed in the requirements.txt file in the same directory. 

### Configuring Django
Next we need to configure some Django stuff before we can run the project. 
Navigate to the potassium directory. You will know you're in the right directory if it contains the manage.py file. 
In this directory, you'll need to create a .env file that has the following line of code:

SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

Then, in the same directory, run the following command: 'python3 manage.py runserver' to make the web service active

In some cases, Django might want you to first configure the databases. So if there's an error mentioning the database not being setup, run the following commands:

python3 manage.py makemigrations

python3 manage.py migrate

### Running the project
After you run the command 'python3 manage.py runserver', the web service becomes live. Navigate to the link: http://127.0.0.1:8000/
If that link doesn't work, try http://127.0.0.1:8000/mangareader


You should now have access to the project!

## User Documentation

User documentation information is detailed in the 'User Documentation - Mangareader.pdf' file that is in the docs folder. 
