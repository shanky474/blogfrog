from django import forms

class BlogForm(forms.Form):
    first_name = forms.CharField(label='First Name:', max_length=100)
    last_name = forms.CharField(label='Last Name:', max_length=100)
    gender = forms.CharField(label='Sex:')
    profession = forms.CharField(label='Profession:',max_length=100)
    title = forms.CharField(label='Title:', max_length=100)
    blog_content = forms.CharField(widget=forms.Textarea(attrs={'rows': 100, 'cols': 150}))

