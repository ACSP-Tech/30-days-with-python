from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    position = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=200)
    image = models.ImageField(upload_to='employee')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
