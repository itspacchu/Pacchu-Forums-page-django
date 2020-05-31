from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper

choices = [('python','Python'),('c','C'),('java','JAVA'),('javascript','Javascript'),('c++','C++'),('ruby','Ruby'),('csharp','C#'),('brainfuck','BrainFuck')]

class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    rollno = forms.CharField(max_length=10,label='Roll No')
    sec = forms.CharField(max_length=5,label='Class:Section')
    email = forms.EmailField(label='E-Mail',required=False)
    language = forms.ChoiceField(choices=choices,label='Languages')
    githublink = forms.URLField(required=False)
    body = forms.CharField(widget=forms.Textarea,required=False)
    field_order = []
    
class SnipperForm(forms.ModelForm):
    helper = FormHelper()
    class Meta:
        model = Snippet
        fields = {
            'name',
            'rollno',
            'sec',
            'phoneno',
            'languages',
            'email',
            'githubusername',
            'githublink',
            'body',
        }
    field_order =  [
        'name',
        'rollno',
        'sec',
        'phoneno',
        'languages',
        'email',
        'githubusername',
        'githublink',
        'body',
    ]