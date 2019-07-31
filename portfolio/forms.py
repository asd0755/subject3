from django import forms
from .models import Portfolio

class NewPortfolio(forms.ModelForm):
    class Meta:
        model = Portfolio
        # fields_all = '__all__'
        fields = ['title', 'image','body']  # 따옴표 주의