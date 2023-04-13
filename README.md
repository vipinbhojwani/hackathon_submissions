# Hackathon Submission API
### This is a Django RESTful API for submitting and managing hackathon projects.


## Prerequisites
* Python 3.6 or higher
* Django 3.2 or higher
* Django REST framework 3.12 or higher


## Installation
* Clone the repository.
* Create a virtual environment and activate it:
  
    ```python -m venv venv```

    ```source venv/bin/activate```

* Install the dependencies:
  
    ```pip install -r requirements.txt```

* Create the database tables:

    ```python manage.py migrate```

* Create a superuser account:

    ```python manage.py createsuperuser```

* Start the development server:

    ```python manage.py runserver```


## Usage

### Authentication

To use the API, you need to authenticate by obtaining a token. You can get a token by sending a POST request to the /api/auth/token/ endpoint with your username and password in the request body. The response will contain an access token, which you can use in subsequent requests by setting the Authorization header:


```Authorization: Bearer <access_token>```

### Endpoints

The API provides the following endpoints:
* /api/hackathons/: List all hackathons or create a new hackathon.
* /api/hackathons/<id>/: Retrieve, update, or delete a specific hackathon.
* /api/hackathons/<id>/submit/: Submit a project for a specific hackathon.
* /api/hackathons/<id>/projects/: List all submitted projects for a specific hackathon.
* /api/hackathons/<id>/projects/<id>/: Retrieve, update, or delete a specific project.

### Examples
Here are some examples of how to use the API with curl:

List all hackathons:

```curl http://localhost:8000/api/hackathons/ -H "Authorization: Bearer <access_token>"```

Create a new hackathon:

```curl -X POST http://localhost:8000/api/hackathons/ -H "Authorization: Bearer <access_token>" -d '{"name": "Hackathon 2023", "start_date": "2023-05-01", "end_date": "2023-05-02"}'```

Submit a project for a hackathon:

```curl -X POST http://localhost:8000/api/hackathons/1/submit/ -H "Authorization: Bearer <access_token>" -d '{"name": "Project 1", "description": "This is a cool project!"}'```

List all submitted projects for a hackathon:

```curl http://localhost:8000/api/hackathons/1/projects/ -H "Authorization: Bearer <access_token>"```
