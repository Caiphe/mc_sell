from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    ''' Here I'm just customising some placeholder and setting the labels to empty '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].label = ''
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"
        self.fields["password1"].label = ''
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].label = ''
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"


#  Updated
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "Placeholder": "Address Email",
            'type' : 'email'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email']

    # ''' Remove the label on my Update profile form '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["email"].label = ''

#  This is the profile update class


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
