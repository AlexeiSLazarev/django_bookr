from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    book_name = request.GET.get("book_name") or "Web dev with Django"
    return render(request, "search.html", {"book_name": book_name})

