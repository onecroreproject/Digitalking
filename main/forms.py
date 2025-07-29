from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control shadow-none'}),
        label="First Name"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control shadow-none'}),
        label="Email"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control shadow-none'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control shadow-none'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'] 
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6,widget=forms.TextInput(attrs={
        'class' : 'form-control shadow-none',
        'placeholder':'Enter OTP'
    }))
    
    
    
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()
    
    
    def clean_data(self):
        email = self.cleaned_data.get('email')
        return email
    
class PasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm New Password")

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError("The passwords do not match.")
        return new_password2
    

class BillingDetailForm(forms.ModelForm):
    class Meta:
        model = BillingDetail
        fields = ['first_name', 'last_name', 'company_name', 'address', 'city', 'pin_code', 'state', 'country','phone', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
        
class CustomerQueryForm(forms.ModelForm):
    class Meta:
        model = CustomerQuery
        fields = ['subject', 'message', 'attachment']
