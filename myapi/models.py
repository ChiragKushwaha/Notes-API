from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_on_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-creation_date','-updated_on_date']
    
    def __str__(self):
        return self.title