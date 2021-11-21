from django import forms

from . models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'image',
            'name',
            'category',
            'price',
            'description'
        ]



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': (forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'false'})
        )}


    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            'autocomplete': 'false'
        })