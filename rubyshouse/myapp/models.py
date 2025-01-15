from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()  # Changed to TextField for longer messages
    
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Calendar(models.Model):
    date = models.DateField(unique=True)
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')