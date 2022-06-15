from django import forms
from .models import Men, Category

class AddPostForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category do not choose"  # пустой выбор категории
    class Meta:
        model = Men
        fields = ('title', 'slug', 'content', 'photo', 'is_published', 'category', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': '30', 'rows': '10'}),
            
        }
        
    def clean_title(self):
        """Check the length of the title"""
        data = self.cleaned_data["title"]
        if len(data) > 200:
            raise forms.ValidationError("Title is too long")
        return data