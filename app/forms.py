from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name is start with a')
def check_for_age(values):
    if values<25:
        raise forms.ValidationError('age is more the 25')
class Studentform(forms.Form):
    Sname = forms.CharField(max_length=100,validators=[check_for_a])
    Sid = forms.IntegerField(validators=[check_for_age])
    Sage = forms.IntegerField(validators=[check_for_age]    )