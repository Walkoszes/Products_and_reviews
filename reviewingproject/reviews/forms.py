from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author", "text", "rating"]
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }