from django import forms

# form that takes the name, birthdate, position, salary
class EmployeeForm(forms.Form):
    name = forms.CharField()
    birthdate = forms.DateField()
    position = forms.IntegerField()
    salary = forms.DecimalField()


