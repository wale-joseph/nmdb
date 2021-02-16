from django import forms
from django.core.validators import FileExtensionValidator


validate_file = FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'],
                                        message='Wrong File Format',
                                        code='200')

class newMovie(forms.Form):
    Title = forms.CharField(max_length=128)
    coverArt = forms.FileField(validators=[validate_file])
    Comment = forms.CharField(max_length=200, widget=forms.Textarea)
