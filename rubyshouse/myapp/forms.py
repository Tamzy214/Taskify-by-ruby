from django import forms
from django.forms import ModelForm
from .models import Task, Contact, Calendar


class FormContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # Fixed widget for email
            'message': forms.Textarea(attrs={'class': 'contact-message', 'rows': 4}),  # Changed to Textarea
        }


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class FormTask(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),  # Changed to Textarea
            'due_date': DateTimePickerInput(attrs={'class': 'form-control'}),
        }

class FormCalendar(ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),  # Use DateInput widget
        }
