from django import forms

class requestInvitation(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'awesome'}), required=True)
    about = forms.CharField(min_length=200, max_length=1000, widget=forms.Textarea(attrs={'class': 'awesome'}),
                            required=True)

