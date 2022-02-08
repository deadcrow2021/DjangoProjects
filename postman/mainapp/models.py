from django.db import models

class MailAddress(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email Address')
    
    def __str__(self):
        return self.name + ' --- ' + (self.email)