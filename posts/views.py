from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver

# Create your views here.





def home(request):
    url_patterns = get_resolver().url_patterns
    html = "<html><body><ul>"

    for pattern in url_patterns:
        html+= '<a href="{}" target="_blank">{}</a><br>'.format(pattern.pattern, pattern.pattern)
    html+="</ul></body></html>"
    print(html)

    return HttpResponse(html)

def test_annotate(request):
    return HttpResponse("Hi")