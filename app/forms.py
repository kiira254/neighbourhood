from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile,Neighborhood,Business,Post,Comment

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name','bio','neighborhood','email')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']

class PostForm(forms.ModelForm):
    CHOICES = (('1', 'Amber',), ('2', 'Normal',))
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    class Meta:
        model = Post
        fields = ('title','content','type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

