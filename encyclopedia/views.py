from django.shortcuts import render

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        # "link": util.
    })

def create(request):
    return render(request, "encyclopedia/create.html", {

    })

def open(request, title):
    page = markdown2.markdown(util.get_entry(title))

    return render(request, "encyclopedia/page.html", {
        "page": page,
        "title": title,
    })
