from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blogs import forms
from blogs import models
from pprint import pprint

def index (request):
    return render_to_response('index.html')

def create_blog(request):
    return render(request, 'create_blog.html')

def view_blog_data(request):
    if request.method == 'POST':
        data = forms.BlogForm(request.POST)
        if data.is_valid():
            get_detail=data.cleaned_data.get
            author=models.Author(first_name=get_detail("first_name"),last_name=get_detail("last_name"), gender=get_detail("gender"), profession=get_detail("profession"))
            blog=models.Blog(author=author, title=get_detail("title"), description=get_detail("blog_content"), likes=0, dislikes=0)
    else:
        data = forms.BlogForm()
    return render(request, 'success.html', {'author': author, 'blog':blog})

def save_blog_data(request):
    if request.method == 'POST':
        get_field=request.POST.get
        get_keys=request.POST.keys
        author=models.Author()
        blog=models.Blog()
        for fields in get_keys():
            if hasattr(author,fields):
               setattr(author,fields,get_field(fields))
            elif hasattr(blog,fields):
                setattr(blog,fields,get_field(fields))
        blog.author=author
        pprint(vars(author))
        pprint(vars(blog))
    return render(request, 'test.html')


def liked_blog(request):
    if request.method == 'POST':
         print("Likes:"+request.POST.get('likes'))
    return render(request, 'test.html')


def disliked_blog(request):
    if request.method == 'POST':
        print("Dislikes:"+request.POST.get('dislikes'))
    return render(request, 'test.html')


# Create your views here.
