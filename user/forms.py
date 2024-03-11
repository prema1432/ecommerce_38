from django import forms

from user.models import CustomerUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ["first_name", "last_name", "username", "password", "email", "phone_number", "dob"]
