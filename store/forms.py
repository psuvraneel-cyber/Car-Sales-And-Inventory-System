from datetime import datetime
from django import forms
from .models import ( NewsletterSubscriber)
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Car, Customer, Sale, TestDrive, Testimonial, Inquiry
        
class Meta:
        model = TestDrive
        fields = ['car', 'customer', 'scheduled_date', 'notes']
        widgets = {
            'scheduled_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
        


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'car', 'sale_amount', 'sale_date', 'payment_method', 'notes']
        widgets = {
            'sale_date': forms.DateInput(attrs={'type': 'date'}),
            'sale_amount': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0',
                'placeholder': 'Enter amount'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(is_available=True)
        


# forms.py
class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = ['customer_name', 'customer_email', 'customer_phone', 
                 'car', 'scheduled_date', 'notes']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['car', 'content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'car', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }