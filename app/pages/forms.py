from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class RequestPostForm(forms.Form):
    post_number = forms.NumberInput()


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
