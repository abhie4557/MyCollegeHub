from django import forms
from .models import UserProfile, UserDocument

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

class UserDocumentForm(forms.ModelForm):
    class Meta:
        model = UserDocument
        fields = ['document']
