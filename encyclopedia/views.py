from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        # "link": util.
    })

def create(request):
    return render(request, "encyclopedia/create.html", {

    })

def open(request, title):
    page = util.get_entry(title)
    return render(request, "encyclopedia/page.html", {
        "page": page,
        "title": title,
    })
