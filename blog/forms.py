from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        # fields_all = '__all__'
        fields = ('title', 'body')  # 따옴표 주의