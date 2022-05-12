from django import forms
from .models import Events, Featured, Vids, Category
from django.forms.widgets import DateInput, Textarea

class UploadForm(forms.ModelForm):
	class Meta:
		model = Vids
		fields = ['caption', 'date', 'remarks', 'thumbnail', 'video', 'playlist']
		widgets = {
            'date': DateInput(attrs={'type': 'date'}),
			'remarks': forms.TextInput(attrs={'placeholder': 'Video description'}),
			'remarks': forms.Textarea(attrs={'placeholder': 'Video description'})
        }


class FeaturedForm(forms.ModelForm):
	class Meta:
		model = Featured
		fields = ['title', 'date_uploaded', 'description', 'featured']
		widgets = {
            'date_uploaded': DateInput(attrs={'type': 'date'}),
			'description': forms.TextInput(attrs={'placeholder': 'Video description'}),
			'description': forms.Textarea(attrs={'placeholder': 'Video description'})
        }


class EventsForm(forms.ModelForm):

	class Meta:
		model = Events
		fields = ['title', 'image', 'narrative']
		widgets = {
			'narrative':forms.TextInput(attrs={'placeholder': 'Write a short description of the event'}),
			'narrative':forms.Textarea(attrs={'placeholder': 'Write a short description of the event'}),
	}


class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ['name', 'category']
