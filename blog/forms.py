from django import forms
from .models import Men, Category

class AddPostForm(forms.Form): 
    title = forms.CharField(max_length=255, label='Theme', widget=forms.TextInput(attrs={'class': 'form-input'})) 
    slug = forms.SlugField(max_length=255, label='URL') 
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Text', help_text='Text of the post') 
    is_published = forms.BooleanField(label='Publication', required=False, initial=True) 
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Select category') 