from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserDocument
from .forms import UserProfileForm, UserDocumentForm

# Create your views here.

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = UserDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect('uploaded_documents')
    else:
        form = UserDocumentForm()
    return render(request, 'users/upload_document.html', {'form': form})

@login_required
def uploaded_documents(request):
    documents = UserDocument.objects.filter(user=request.user)
    return render(request, 'users/uploaded_documents.html', {'documents': documents})
