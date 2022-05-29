from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choices_l = []
for item in choices:
    choices_l.append(item)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'snip')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Let\'s write some title to your Post'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            'category': forms.Select(choices=choices_l, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snip': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snip')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write title for post'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snip': forms.Textarea(attrs={'class':'form-control'}),
        }

