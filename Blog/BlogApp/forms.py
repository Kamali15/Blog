from django import forms
from .models import Post  , Category, Comment


choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)
    
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title','title_tag','snippet','author','category','content','header_image')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':"title"}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':"title"}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':"Author"}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'})           
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','header_image','title_tag','snippet','author','category','content')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':"title"}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':"title"}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':"Author"}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'})

           
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields ='__all__'
        widgets = {
            'post' : forms.Select(attrs = {'class' : 'form-control','placeholder':"Post"}),
            'name' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'body' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }