from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(min_length=3, max_length=500, widget=forms.TextInput(attrs={'class': 'awesome'}),
                           required=True)

