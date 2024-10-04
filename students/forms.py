from datetime import date
from django import forms
from django.core.exceptions import ValidationError
import re

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    enrollment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    grade = forms.IntegerField(min_value=1, max_value=12)

    # Custom validation for first name
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        # Ensure the name contains only alphabetic characters
        if not re.match(r'^[A-Za-z]+$', first_name):
            raise ValidationError('First name must contain only letters.')
        
        return first_name

    # Custom validation for last name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        
        # Ensure the name contains only alphabetic characters
        if not re.match(r'^[A-Za-z]+$', last_name):
            raise ValidationError('Last name must contain only letters.')
        
        return last_name
    
    
    # Custom validation for enrollment_date
    def clean_enrollment_date(self):
        enrollment_date = self.cleaned_data.get('enrollment_date')
        
        # Ensure the date is in the past
        if enrollment_date > date.today():
            raise ValidationError('Enrollment date must be in the past.')
        
        return enrollment_date

    # Custom validation for date_of_birth
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        
        # Ensure the date is in the past
        if date_of_birth >= date.today():
            raise ValidationError('Date of birth must be in the past.')
        
        return date_of_birth

class StudentSearchForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False, label='First Name')
    last_name = forms.CharField(max_length=100, required=False, label='Last Name')

    # Custom validation for first name
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            # Ensure the name contains only alphabetic characters
            if not re.match(r'^[A-Za-z]+$', first_name):
                raise ValidationError('First name must contain only letters.')
        
        return first_name

    # Custom validation for last name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if last_name:
            # Ensure the name contains only alphabetic characters
            if not re.match(r'^[A-Za-z]+$', last_name):
                raise ValidationError('Last name must contain only letters.')
        
        return last_name