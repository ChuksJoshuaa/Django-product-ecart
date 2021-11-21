from django import forms

class ContactMeForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    Phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    Message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)

