from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid


class Discussion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_by = models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.created_by

class DiscussionComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Discussion=models.ForeignKey(Discussion, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
