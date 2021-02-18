from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from . models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts' #can use object list in templates instead of this line
    ordering = ['-created_time']

class PostDetailView(DetailView):
    model = Post
    #template_name = 'posts/post_list.html'
    context_object_name = 'detail' #can use object list in templates instead of this line

class PostCreateView(CreateView):
    model = Post
    fields = ['question_title','question_description']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
