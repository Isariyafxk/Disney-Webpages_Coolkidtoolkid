from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def disney_webpage(request):
    context = {}
    return render(request, "DisneyWebpage/home.html", context=context)

def places(request):
    context = {}
    return render(request, "DisneyWebpage/places.html", context=context)

def helpcenter(request):
    context = {}
    return render(request, "DisneyWebpage/helpcenter.html", context=context)

def aboutus(request):
    context = {}
    return render(request, "DisneyWebpage/aboutus.html", context=context)