from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     desc= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email