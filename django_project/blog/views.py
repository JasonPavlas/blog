from django.shortcuts import render
from django.views.generic import(
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    ##prediction
    ###I think we will add a message in here for sucess
    ###I think we will return a redirct to /home/
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})