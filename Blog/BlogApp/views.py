from django.shortcuts import render , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Post, Category, Comment
from .forms import *
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


# # Create your views here.

def LikeView(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked= False
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked= False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))


class HomeView(generic.ListView):
    model= Post
    template_name = 'home.html'
    cats =Category.objects.all()
    ordering = ['-created_at']

    def get_context_data(self,*args,**kwargs):
        cat_menu =  Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'Categories.html',{'cats':cats.replace('-',' ').title(), 'category_post':category_post})
    
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,['CategoryList.html'],{'cat_menu_list':cat_menu_list})


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu =  Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
     

        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'AddPost.html'
    #fields = "__all__"
    # success_url = '/'

class AddCategoryView(generic.CreateView):

    form_class = CategoryForm
    template_name = 'AddCategory.html'
    # success_url = '/article'

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # success_url = "/"

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = "/"

class AddCommentView(generic.CreateView):
    model = Comment
    template_name = 'add_comments.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')