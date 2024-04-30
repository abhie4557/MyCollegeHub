from django.shortcuts import render
from .models import PDFDocument
from .models import PDFNotes

from django.http import FileResponse, Http404, HttpResponse
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import os

def url(request):
    pdf_id = 1  # Example: Set your dynamic PDF ID here
    context = {'pdf_id': pdf_id}
    return render(request,'resources/url.html', context)


# Create your views here.

   
def findpdf(request, pdf_cat):
    pdf_id={}

    if pdf_cat=='notes':
        pdf_notes_ids = list(PDFNotes.objects.values_list('Notes_id', flat=True))
    elif pdf_cat=='papers': 
        # papers_ids = list(Papers.objects.values_list('pdf_id', flat=True))
        pass
    elif pdf_cat=='assignments':
        # assignment_ids = list(Assignment.objects.values_list('pdf_id', flat=True))
        pass
    all_pdf_ids=pdf_notes_ids
    print(all_pdf_ids)
    # all_pdf_ids = pdf_notes_ids + papers_ids + assignment_ids
    context = {'all_pdf_ids': all_pdf_ids}
    return render(request, 'resources/pdf_view.html', context)


def index(request):
    pdf_file_path = os.path.join(settings.MEDIA_URL, 'invoice.pdf')
    return render(request, 'resources/index.html', {'pdf_file_path': pdf_file_path})


# def pdf_canvas_view(request, pdf_filename):
#     pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
#     print(pdf_path)
#     return render(request, 'resources/pdf_canvas.html', {'pdf_path': pdf_path})

# -----------Display pdf function for media files-----------------
# def display_pdf(request, filename):
#     storage = FileSystemStorage(location='/media/') # Change this to the path where your PDF files are stored
#     file_path = storage.path(filename)

#     with open(file_path, 'rb') as pdf_file:
#         response = FileResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = f'inline; filename="{filename}"'
#         return response

# -----------Display pdf function for static files-----------------
# def display_pdf(request):
#     # Path to your PDF file
#     pdf_file_path = os.path.join(settings.STATIC_ROOT, 'path_to_your_pdf_file.pdf')

#     # Check if the file exists
#     if os.path.exists(pdf_file_path):
#         pdf_url = f'/static/path_to_your_pdf_file.pdf'  # Update the URL based on your project structure
#         return render(request, 'pdf_display.html', {'pdf_url': pdf_url})
#     else:
#         return HttpResponse("PDF file not found.")

    
# -----------------Using FileResponse Class-------------------------
# def pdf_view1(request):
#     try:
#         return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         raise Http404()

# -----------------------Using With Keyword-----------
# def pdf_view2(request):
#     with open('/path/to/my/file.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed


# ----------Using with keyword and content disposition
def pdf_view(request, pdf_id):
    # Assuming you have a model named PDFDocument with a FileField named pdf_file
    try:
        # Retrieve the PDFDocument object by ID
        pdf_document = PDFDocument.objects.get(pk=pdf_id)
        pdf_path = pdf_document.pdf_file.path  # Get the absolute path to the PDF file
        
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            # Set the Content-Disposition header to force the browser to download the file
            response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf_path)}"'
            return response
    except PDFDocument.DoesNotExist:
        return HttpResponse("PDF not found", status=404)


# ---------------For Uploading pdfs-----------------------
# def Update(request):
#     fs = FileSystemStorage(location='/path/to/your/directory/')
#     uploaded_file = request.FILES['file_field_name']
#     fs.save(uploaded_file.name, uploaded_file)
    