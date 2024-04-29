from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Customize field labels if needed
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['first_name', 'last_name', 'about', 'company', 'job', 'country', 'address', 'phone_number', 'email', 'twitter', 'facebook', 'instagram', 'linkedin', 'candidate_image']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }
        # Set required attribute for specific fields
        required_fields = {
            'first_name': True,
            'last_name': True,
            'email': True,
            # Add other required fields as needed
        }
        candidate_image = forms.FileField(label='Profile Image', required=False)  # Allow users to upload a profile image


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Update required attribute based on model's field requirements
        for field_name, required in self.Meta.required_fields.items():
            self.fields[field_name].required = required
