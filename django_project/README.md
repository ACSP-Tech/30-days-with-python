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