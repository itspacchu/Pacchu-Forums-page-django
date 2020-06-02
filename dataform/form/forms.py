from django import forms
from .models import Snippet 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(SnipperForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['body'].widget.attrs['cols'] = 25
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
            value.help_text = None

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
        widgets = {
        #'languages': forms.RadioSelect(),
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

