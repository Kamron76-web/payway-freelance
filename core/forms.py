from django import forms
from django.contrib.auth.models import User
from .models import FreelancerProfile, Job, Bid

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    full_name = forms.CharField(max_length=100)
    skill = forms.CharField(max_length=100, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    is_seller = forms.BooleanField(required=False, label='Seller/Freelancer bo‘lib ro‘yxatdan o‘tish')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )

        FreelancerProfile.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            skill=self.cleaned_data.get('skill', ''),
            bio=self.cleaned_data.get('bio', ''),
            is_seller=self.cleaned_data.get('is_seller', False)
        )

        return user


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'budget']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'message']
