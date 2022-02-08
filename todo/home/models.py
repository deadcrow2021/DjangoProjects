from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    confirm = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title