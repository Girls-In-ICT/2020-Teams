from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, ModelForm

from empowerment.models import UserProfile, BookComment


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'address', 'image', 'gender']


class BooksComment(ModelForm):
    class Meta:
        model = BookComment
        fields = ['bookId', 'userId', 'comment']
