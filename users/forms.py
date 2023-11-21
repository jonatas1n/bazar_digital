from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'name', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
