from django.shortcuts import render

def index(request):
    try:
        name = request.GET["name"]
    except:
        name = "world"
    return render(request, "base.html", {"name": name})

