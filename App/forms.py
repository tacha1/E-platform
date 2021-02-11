from django import forms
from .models import Rating, Profile
from django.forms import ModelForm,Textarea,IntegerField
    
class VotingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']