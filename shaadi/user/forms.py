from django import forms
from django.contrib.auth.forms import  AuthenticationForm

from django.contrib.auth.models import User

from .models import CustomUser,Chat,Preference

class CustomUserForm(forms.ModelForm):
    
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))

    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(label='Qualification', widget=forms.TextInput(attrs={'class': 'form-control'}))
    job = forms.CharField(label='Job', widget=forms.TextInput(attrs={'class': 'form-control'}))
    selfdescription = forms.CharField(label='Self Description', widget=forms.Textarea(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='Photo', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    password2 = forms.CharField(label='Password confirmation',strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
  

    class Meta:
        
        photo = forms.ImageField()
        model = CustomUser
        fields = ['username','first_name','last_name','gender', 'email','phone', 'religion', 'community', 'living_country','livewithfamily','maritalstatus','diet','height','city','age','qualification','job','selfdescription','photo']     
        
        
        widgets = {
                'gender' : forms.Select(attrs={'class':'form-control'}),
                'religion' : forms.Select(attrs={'class':'form-control'}),
                'community' : forms.Select(attrs={'class':'form-control'}),
                'living_country' : forms.Select(attrs={'class':'form-control'}),
                'livewithfamily' : forms.Select(attrs={'class':'form-control'}),
                'maritalstatus' : forms.Select(attrs={'class':'form-control'}),
                'diet' : forms.Select(attrs={'class':'form-control'}),
                'height' : forms.Select(attrs={'class':'form-control'}),
  
        }   

        
        
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
        


class signinform(AuthenticationForm):
    def confirm_login_allowed(self, user):
        username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
        password = forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
        pass
    
    
    
class userprofileform(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','gender', 'email','phone', 'religion', 'community', 'living_country','livewithfamily','maritalstatus','diet','height','city','age','qualification','job','selfdescription']
    


# class chatform(forms.ModelForm):
    
#     class Meta:
#         model=Chat
#         fields=["message"]
        
        
class userprofileeditform(forms.ModelForm):
    
    class Meta:
        photo = forms.ImageField()
        model=CustomUser
        fields=['username','age','email','phone','community', 'living_country','livewithfamily','maritalstatus','diet','living_country','livewithfamily','maritalstatus','diet','height','city','age','qualification','job','selfdescription','photo']
        
        
        
class PreferenceForm(forms.ModelForm):
    min_height = forms.IntegerField(label='Minimum height', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_height = forms.IntegerField(label='Maximum height', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    min_age = forms.IntegerField(label='Min age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_age = forms.IntegerField(label='Max age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = Preference
        fields = ['preferred_gender','preferred_religion','preferred_community','preferred_maritalstatus','min_height','max_height','min_age','max_age']
        
        
    widget={
        'preferred_gender' : forms.Select(attrs={'class':'form-control'}),
        'preferred_religion' : forms.Select(attrs={'class':'form-control'}),
        'preferred_community' : forms.Select(attrs={'class':'form-control'}),
        'preferred_maritalstatus' : forms.Select(attrs={'class':'form-control'}),
    }




    

