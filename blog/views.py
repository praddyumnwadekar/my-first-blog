from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {'pk': pk})