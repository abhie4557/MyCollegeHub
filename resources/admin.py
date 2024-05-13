from django.contrib import admin
from resources.models import PDFDocument, PDFNote,Paper
# Register your models here.

admin.site.register(PDFDocument)
admin.site.register(PDFNote)
admin.site.register(Paper)