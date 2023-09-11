from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is start with a')

class Studentform(forms.Form):
    Sname = forms.CharField(max_length=100,validators=[check_for_a])
    Sid = forms.IntegerField()
    Sage = forms.IntegerField()
    Semail = forms.EmailField()
    Remail = forms.EmailField()
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    Repassword = forms.CharField(max_length=100,widget=forms.PasswordInput)
    botcatcher = forms.CharField(max_length=100)# 
    # moblie = forms.CharField(max_length=100)
    # for this clean method is used for check input elements

    def clean(self):  # self hold all objects
        e =self.cleaned_data['Semail']
        r = self.cleaned_data['Remail']
        password = self.cleaned_data['password']
        Repassword = self.cleaned_data['Repassword']

        if e != r or password != Repassword :
            raise forms.ValidationError('emails are not same')


    
        