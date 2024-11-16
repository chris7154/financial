from django import forms
from .models import Course
import datetime


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'instructor', 'duration', 'start_date', 'video', 'price']
