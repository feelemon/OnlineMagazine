from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'magazine/post_list.html', {})