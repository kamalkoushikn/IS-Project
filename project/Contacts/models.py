from django.db import models
# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    
    # Name of the user
    name = models.CharField(max_length=100, null=False)
    
    # Email address of the user (must be unique)
    email = models.EmailField(unique=True, null=False)
    
    # # Hashed password for security
    # password = models.CharField(max_length=255, null=False)
    
    # Timestamp of when the record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp of the last update
    updated_at = models.DateTimeField(auto_now=True)