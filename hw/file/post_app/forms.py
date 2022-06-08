from django import forms
from post_app.models import News
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = 'title text tags'.split()

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": 'form-control',
                    'placeholder': 'Enter a news title'

                }
            ),
            'text': forms.Textarea(
                attrs={
                    "class": 'form-control',
                    'placeholder': 'Enter a news text'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control-custom',
                    'placeholder': ''
                }
            )

        }


class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))


class Registerform(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Repeat password'
        }
    ))
    def clean_username(self ):
        username = self.cleaned_data['user_name']
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('User with this username already exists!')
        return username

    def save(self):
        username = self.cleaned_data['user_name']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        return user


