# Django URLs and Views Project

A beginner-friendly Django project created to understand the core concepts of Django URL routing and Views.  
This project demonstrates how user requests are handled and how responses are returned using Django views.

## Project Overview

In this project, I learned how Django connects the browser request with backend logic using:

- URL Configuration (`urls.py`)
- Views (`views.py`)
- Templates
- HTTP Responses
- Request Handling

## Concepts Covered

### URL Routing

Django URL routing is used to map browser URLs to specific view functions.

The `urls.py` file defines which view should execute when a user visits a particular URL.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

### Views

Views are Python functions or classes that handle user requests and return responses.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

A view receives a request and sends a response back to the user.

### Request and Response

Django follows the request-response cycle:

1. User enters URL in browser
2. Django checks URL patterns
3. Matching view function is called
4. View processes the request
5. Response is returned to browser

## Project Structure

```
project/
│
├── app/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

## Skills Demonstrated

- Django Framework
- URL Routing
- Views Creation
- Request Handling
- HTTP Response
- Django Project Structure
- Python Programming
- HTML Templates

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite Database

## How to Run Project

Clone the repository:

```bash
git clone repository_url
```

Install dependencies:

```bash
pip install django
```

Run server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

## Learning Outcomes

Through this project, I gained practical knowledge about:

- Creating Django projects and applications
- Connecting URLs with views
- Handling user requests
- Returning dynamic responses
- Understanding Django backend workflow

## Future Improvements

- Add database integration
- Create forms
- Connect templates dynamically
- Build CRUD operations

## Author

Ramya Kaviya

Aspiring Python Full Stack Developer
