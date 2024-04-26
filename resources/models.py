from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    
# Model for PDF notes
class PDFNotes(models.Model):
    Notes_id = models.AutoField(primary_key=True)

    # Subject and course fields for categorizing notes
    subject = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

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