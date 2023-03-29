from django import forms

class EmployeeForm(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Farmer`s Name'}))
    Mobile_NO=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Enter Farmer`s Mobile No'}))
    Whatsapp_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Enter Farmer`s Whatsapp No'}),required=False)
    Village=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Farmer`s Village'}))
    District=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Farmer`s District'}))
    Pin_code=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Enter Farmer`s Pin code'}))
    

