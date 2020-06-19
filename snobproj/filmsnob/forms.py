from django import forms
from .models import Movies, Review

class AddMovie(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class AddReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'