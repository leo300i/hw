from django import forms
from post_app.models import News
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = 'title text tags'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'enter a news title!'
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'enter news text'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-conrtol'

                }
            )
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter password'
        }
    ))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('User with this username already exists')
        return username

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username=username, password=password)
        return user
