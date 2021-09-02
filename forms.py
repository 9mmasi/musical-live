from django import forms
from . models import *

class CreatecategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for instance in Category.objects.all():
            if instance.name == name:
                raise forms.ValidationError(name + '  already created')

        return name    


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model= Photo
        fields=['category','description','image','Audio']  

          


class UpdatePhotoForm(forms.ModelForm):
    class Meta:
        model= Photo
        fields=['category','description','image']               