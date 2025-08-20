from django.http import HttpResponse
from django.shortcuts import render

import pathlib

def home_page_view(request):
    
    my_title = "my page"
    mycontext = {
        "pageTitle": my_title,
    }

    html_template = "home.html"
    return render(request, html_template, mycontext)