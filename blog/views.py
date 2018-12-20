from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
