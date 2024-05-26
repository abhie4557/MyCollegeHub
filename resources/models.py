from django.db import models
import uuid
from db_connection import db
import os

#Defining collections from mongoDB
resources_pdfnote= db['resources_pdfnote']
resources_paper= db['resources_paper']

def get_upload_path(instance, filename):
    return os.path.join(str(instance.course),'PreviousYearPapers', str(instance.year), filename)
    return os.path.join(str(instance.course),'PDFNotes', str(instance.subject), filename)

# Create your models here.


class PDFDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')


class Paper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.IntegerField() 
    
    # Subject and course fields for categorizing notes
    subject = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    
    paper_file = models.FileField(upload_to=get_upload_path)  # Use the custom upload path function
    
    
# Model for PDF notes
class PDFNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Subject and course fields for categorizing notes
    subject = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)

    # File field to store the PDF notes
    pdf_file = models.FileField(upload_to='PDFNotes/')

    # Additional fields for metadata or description (optional)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Timestamps for created and updated dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title