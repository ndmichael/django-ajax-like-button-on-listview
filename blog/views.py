from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Post
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_published', 'id']
    paginate_by = 5



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    context_object_name = 'post'


    # the like button view
@login_required
def post_like(request):
    # if request.method == 'POST' and request.is_ajax():
    if request.POST.get('action') == 'post':
        print(request.POST.get('action'))
        flag = None
        postid = int(request.POST.get('post_id'))
        post_obj = get_object_or_404(Post, id=postid)

        if post_obj.likes.filter(id=request.user.id).exists():
            post_obj.likes.remove(request.user)
            post_obj.save()
            flag = False
        else:
            post_obj.likes.add(request.user)
            post_obj.save()
            flag = True
        
        return JsonResponse({'total_likes': post_obj.total_likes, 'flag': flag,})
    return HttpResponse("Error access denied")
