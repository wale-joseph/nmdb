from django import forms

class newMovie(forms.Form):
    Title = forms.CharField(max_length=128)
    #coverArt = forms.ImageField()
    Comment = forms.CharField(max_length=200, widget=forms.Textarea)
