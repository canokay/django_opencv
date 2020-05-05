from django import forms
from django_opencv_app.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image', 'title']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
        }

class ImageEditForm(forms.Form):
    thresh = forms.IntegerField(label='value of treshold', min_value=0, max_value=255)
