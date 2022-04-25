from django import forms
from django.urls import reverse_lazy

from squrteq.models import Forsqrt


class EnterNumbersHere(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Forsqrt
        fields = ['first_number', 'second_number', 'third_number']

    first_number = forms.FloatField()
    second_number = forms.FloatField()
    third_number = forms.FloatField()


# class Addfeedback(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['cat'].empty_label="category is not chosen"
    #
    #
    #     fields = ['title', 'slug', 'content', 'photo', 'cat']
    #
    #
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('length is more than 200 characters')
    #     return title