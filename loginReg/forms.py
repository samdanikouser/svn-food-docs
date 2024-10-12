from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UsernamePasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Username")

    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a new password'}),
        help_text="Your password must contain at least 8 characters."
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('new_password1')
        # Add custom validation here if needed
        if len(password1) < 10:  # Example: Ensure password length is at least 10 characters
            raise forms.ValidationError("The new password must be at least 10 characters long.")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username does not exist.")
        return self.cleaned_data