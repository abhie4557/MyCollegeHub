from django.shortcuts import render
from .models import PDFDocument, Paper, PDFNote
from .models import resources_pdfnote, resources_paper
from django.http import FileResponse, Http404, HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from bson import ObjectId  # Import ObjectId from bson package

def convert_to_json(obj):
    if isinstance(obj, ObjectId):
        return str(obj)  # Convert ObjectId to string
    elif isinstance(obj, dict):
        return {key: convert_to_json(value) for key, value in obj.items()}  # Recursively convert nested dicts
    elif isinstance(obj, list):
        return [convert_to_json(item) for item in obj]  # Recursively convert lists
    return obj  # For other types, return as-is


def filtered_data(request):
    course= request.GET.get('course')
    year = request.GET.get('year')

    filter_query = {}
    if course:
        filter_query['course'] = course
    if year:
        filter_query['year'] = int(year)

    filtered_documents = list(resources_paper.find(filter_query))
    # Convert MongoDB documents to Python dictionaries
    python_documents = [doc for doc in filtered_documents]
    # Convert Python dictionaries to JSON-compatible format
    json_documents = convert_to_json(python_documents)
    
    return JsonResponse(json_documents, safe=False)


def url(request):
    pdf_id = 1  # Example: Set your dynamic PDF ID here
    context = {'pdf_id': pdf_id}
    return render(request,'resources/url.html', context)


# Create your views here.
def getalldocs(request):
    docs = resources_pdfnote.find({'course':'BCA'},{'pdf_file':1, '_id':0})
    print(type(docs))
    return HttpResponse(docs)
   
def findpdf(request, pdf_cat):
    pdf_id={}

    if pdf_cat=='notes':
        pdf_notes_ids = list(PDFNote.objects.values_list('id', flat=True))
    elif pdf_cat=='papers': 
        papers_ids = list(Paper.objects.values_list('id', flat=True))
        pass
    elif pdf_cat=='assignments':
        # assignment_ids = list(Assignment.objects.values_list('pdf_id', flat=True))
        pass
    pdf_id=papers_ids
    print(pdf_id)
    # all_pdf_ids = pdf_notes_ids + papers_ids + assignment_ids
    context = {'pdf_id': pdf_id}
    return render(request, 'resources/pdf_view.html', context)


def index(request):
    return render(request, 'resources/filters.html')


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
    