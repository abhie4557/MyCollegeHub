from django.shortcuts import render
from .models import PDFDocument, Paper, PDFNote
from .models import resources_pdfnote, resources_paper,resources_assignment
from django.http import FileResponse, Http404, HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from bson import ObjectId  # Import ObjectId from bson package


# Create your views here.

def index(request):
    # Get the path of the request
    request_path = request.path
    context ={}
    
    if request_path == '/resources/BCA':
        context['course'] = "BCA"
    elif request.path == '/resources/BBA':
        context['course'] = "BBA"
    elif request.path == '/resources/BHM':
        context['course'] = "BHM"
        
    return render(request, 'resources/index.html', context)


def filter(request):
    return render(request, 'resources/filters.html')

def bcadocs(request, type):
    course= "BCA"
    type = type
    filter_query = {}
          
    filter_query['course'] = course
    
 
    print(filter_query)
    
    # return render(request, 'resources/index.html', {'data':filtered_docs} )
    if type == "Previous Year Papers":
        filtered_documents = list(resources_paper.find(filter_query))
    elif type == "Notes":
        filtered_documents = list(resources_pdfnote.find(filter_query))
    elif type == "Assignments":
        filtered_documents = list(resources_assignment.find(filter_query))
    
    # Convert MongoDB documents to Python dictionaries
    python_documents = [doc for doc in filtered_documents]
    
    docs={'data':python_documents}
    
    # Merge the two dictionaries
    context = {**filter_query, **docs, **{'type':type}}
    
    print(filtered_documents)
    print(python_documents)
    return render(request, "resources/alldocs.html", context)

def bbadocs(request, type):
    course= "BBA"
    type = type
    filter_query = {}
          
    filter_query['course'] = course
    
 
    print(filter_query)
    
    # return render(request, 'resources/index.html', {'data':filtered_docs} )
    if type == "Previous Year Papers":
        filtered_documents = list(resources_paper.find(filter_query))
    elif type == "Notes":
        filtered_documents = list(resources_pdfnote.find(filter_query))
    elif type == "Assignments":
        filtered_documents = list(resources_assignment.find(filter_query))
    
    # Convert MongoDB documents to Python dictionaries
    python_documents = [doc for doc in filtered_documents]
    
    docs={'data':python_documents}
    
    # Merge the two dictionaries
    context = {**filter_query, **docs, **{'type':type}}
    
    print(filtered_documents)
    print(python_documents)
    return render(request, "resources/alldocs.html", context)

def bhmdocs(request, type):
    course= "BHM"
    type = type
    filter_query = {}
          
    filter_query['course'] = course
    
 
    print(filter_query)
    
    # return render(request, 'resources/index.html', {'data':filtered_docs} )
    if type == "Previous Year Papers":
        filtered_documents = list(resources_paper.find(filter_query))
    elif type == "Notes":
        filtered_documents = list(resources_pdfnote.find(filter_query))
    elif type == "Assignments":
        filtered_documents = list(resources_assignment.find(filter_query))
    
    # Convert MongoDB documents to Python dictionaries
    python_documents = [doc for doc in filtered_documents]
    
    docs={'data':python_documents}
    
    # Merge the two dictionaries
    context = {**filter_query, **docs, **{'type':type}}
    
    print(filtered_documents)
    print(python_documents)
    return render(request, "resources/alldocs.html", context)

    
def filtered_data(request):
    course= request.GET['courseSelect']
    semester= request.GET['semesterSelect']
    year = request.GET['year']
    type = request.GET['resourceSelect']
    
    filter_query = {}
    if course:
        filter_query['course'] = course
    if semester:
        filter_query['semester'] = semester
    if year:
        filter_query['year'] = int(year)
    
    if not course and not year:
        print("no filter query")
    
    if type == "paper":
        filtered_documents = list(resources_paper.find(filter_query))
    elif type == "notes":
        filtered_documents = list(resources_pdfnote.find(filter_query))
    elif type == "assignment":
        filtered_documents = list(resources_assignment.find(filter_query))
        
    # Convert MongoDB documents to Python dictionaries
    python_documents = [doc for doc in filtered_documents]
    
    print(filter_query)
    print(python_documents)
    
    docs={'data':python_documents}
    
    # Merge the two dictionaries
    context = {**filter_query, **docs}
    print("filter query passed to filter page")
    print(filter_query)
    return render(request, "resources/filters.html", context)
   

# -----------Display pdf function for media files-----------------
def display_pdf(request, filename):
    storage = FileSystemStorage(location='/media/') # Change this to the path where your PDF files are stored
    file_path = storage.path(filename)

    with open(file_path, 'rb') as pdf_file:
        response = FileResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response

# -----------Display pdf function for static files-----------------
def display_pdf(request):
    # Path to your PDF file
    pdf_file_path = os.path.join(settings.STATIC_ROOT, 'path_to_your_pdf_file.pdf')

    # Check if the file exists
    if os.path.exists(pdf_file_path):
        pdf_url = f'/static/path_to_your_pdf_file.pdf'  # Update the URL based on your project structure
        return render(request, 'pdf_display.html', {'pdf_url': pdf_url})
    else:
        return HttpResponse("PDF file not found.")


# ----------Using with keyword and content disposition
def pdf_viewtest(request, pdf_id):
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
def Update(request):
    fs = FileSystemStorage(location='/media/User/')
    uploaded_file = request.FILES['file_field_name']
    fs.save(uploaded_file.name, uploaded_file)
    