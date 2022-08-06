# default form for user form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from django import forms
from .models import Men, Category


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # пустой выбор категории
        self.fields['category'].empty_label = "Category do not choose"

    class Meta:
        model = Men
        fields = ('title', 'slug', 'content', 'photo',
                  'is_published', 'category', )
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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TimeInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # Metadata
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            
        }
    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols' : 60, 'rows' : 10}))
    captcha = CaptchaField()