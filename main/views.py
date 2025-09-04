from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Main page',
        'content': 'Main page of the internet shop - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': False
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')