from django.shortcuts import render

def start(request):
    context = {}
    return render(request, 'CV/start.html', context)
