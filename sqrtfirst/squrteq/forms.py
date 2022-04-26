from django import forms


from squrteq.models import Forsqrt


class EnterNumbersHere(forms.ModelForm):
    class Meta:
        model = Forsqrt
        fields = ['first_number', 'second_number', 'third_number']

class Answers(forms.ModelForm):
    class Meta:
        model = Forsqrt
        fields = ['res_1', 'res_2', 'unsolvable']



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