from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from BlogApp.models import Profile 

class ProfilePageForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("bio","profile_pic","website_url","fb_url","instagram_url")
        widgets = {
        'bio':forms.Textarea(attrs={'class':'form-control'}),
        'website_url':forms.TextInput(attrs={'class':'form-control'}),
        'fb_url':forms.TextInput(attrs={'class':'form-control'}),
        'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
        }



class PasswordChangingForm(PasswordChangeForm):
    
    old_password = forms.CharField(max_length=15)
    new_password1 = forms.CharField(max_length=15)
    new_password2 = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')
        widgets= {
            'old_password': forms.PasswordInput(attrs={'type' : 'password'}),
            'new_password1': forms.PasswordInput(attrs={'type' : 'password'}),
            'new_password2': forms.PasswordInput(attrs={'type' : 'password'}),
        }
    def __init__(self, *args, **kwargs):
            super(PasswordChangingForm,self).__init__(*args,**kwargs)
            self.fields['old_password'].widget.attrs['class'] = 'form-control'
            self.fields['new_password1'].widget.attrs['class'] = 'form-control'
            self.fields['new_password2'].widget.attrs['class'] = 'form-control'

class SignupForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_staff'].required = False
        self.fields['is_active'].required = False
        self.fields['is_superuser'].required = False