from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required.")
    email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
