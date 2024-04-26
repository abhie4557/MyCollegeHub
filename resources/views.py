from django.shortcuts import render
from .models import PDFDocument
from django.http import FileResponse, Http404, HttpResponse
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import os

def pdf_canvas_view(request, pdf_filename):
    pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)
    print(pdf_path)
    return render(request, 'resources/pdf_canvas.html', {'pdf_path': pdf_path})

# Create your views here.
def index(request):
    pdf_document = PDFDocument.objects.all()
    return render(request,'resources/index.html', {'pdf_document': pdf_document})
    return render(request, 'index.html')

# def pdf_view1(request):
#     try:
#         return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         raise Http404()
    
# def pdf_view2(request):
#     with open('/path/to/my/file.pdf', 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#         return response
#     pdf.closed

def pdf_view3(request, pdf_id):
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

def Update(request):
    fs = FileSystemStorage(location='/path/to/your/directory/')
    uploaded_file = request.FILES['file_field_name']
    fs.save(uploaded_file.name, uploaded_file)
    