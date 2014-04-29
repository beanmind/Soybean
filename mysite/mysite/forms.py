from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super (LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            if password != 'sesame' or email != 'pierre@lxs.be':
                raise forms.ValidationError("Wrong email or password")
            
        return cleaned_data