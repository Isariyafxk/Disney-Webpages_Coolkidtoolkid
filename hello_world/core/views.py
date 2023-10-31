from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def disney_webpage(request):
    context = {}
    return render(request, "DisneyWebpage/index.html", context=context)