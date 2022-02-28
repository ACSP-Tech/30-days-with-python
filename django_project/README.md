# Employee Directory 
CRUD operations in a Django application mean performing create, read, update, and delete operations on the database. DjonAn admin user can do all these operations using the Django admin site. But in this article, we will learn how to implement it within the website using the Django ModelForm.

- [ ]  Creating the Views and URL patterns
- [ ]  First Read the Database
    - employee_list view function:
    - list.html:
    - base.html:
    
- [ ]  Creating New Employee
    - Form Models:
    - create.html:
    - create_employee view function:
    
- [ ]  Updating/Editing existing data
    - edit_employee view function:
    - edit.html:
    
- [ ]  Deleting Employee
    - delete_employee view function:
    - delete.html:
    

```text
.
├── employee
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates
│   │   └── employee
│   │       ├── create.html
│   │       ├── delete.html
│   │       ├── edit.html
│   │       └── list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── main
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── templates
    └── base.html
```

## Settings
```python
# /settings.py 

'DIRS': [os.path.join(BASE_DIR, 'templates')],


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## URLs
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
```

## ListView
```python
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/list.html'
		context_object_name = 'employee'
```

## HTML BASE
```html
<!-- ./templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    
    {% block title %}
    {% endblock title %}
</head>
<body>
    <div class="container">
        {% block content %}
        {% endblock content %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```