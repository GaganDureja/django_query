from django.shortcuts import render
from django.http import HttpResponse
from django.urls import get_resolver
from .models import *
# Create your views here.





def home(request):
    url_patterns = get_resolver().url_patterns
    html = "<html><body><ul>"

    for pattern in url_patterns:
        html+= '<a href="{}" target="_blank">{}</a><br>'.format(pattern.pattern, pattern.pattern)
    html+="</ul></body></html>"

    return HttpResponse(html)

def test_annotate(request):
    authors_with_total_books = Author.objects.annotate(total_written=models.Count('entry__blog'))
    html = "This is a annotate of blogs written by author<br><br>"

    for author in authors_with_total_books:
        html += f"Author: {author.name}, Total Written: {author.total_written} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'
    return HttpResponse(html)


def test_aggregate(request):
    authors_with_total_books = Entry.objects.aggregate(total_blogs=models.Count('blog__id'))
    html = "This is a aggregate of blogs written by all author %s" %authors_with_total_books['total_blogs']
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)


def test_filter(request):
    top_rated = Entry.objects.filter(rating__gt=3)
    html = "Blogs with rating greater than 3<br><br>"

    for entry in top_rated:
        html+= f"Heading - {entry.headline}, Rating - {entry.rating} <br>"

    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_exclude(request):
    least_rated = Entry.objects.exclude(rating__gt=3)
    html = "Blogs with exclude rating greater than 3<br><br>"
    for entry in least_rated:
        html+= f"Heading - {entry.headline}, Rating - {entry.rating} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_order_by(request):
    html = "This"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_values(request):
    html = "This"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_distinct(request):
    html = "This"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_slicing(request):
    html = "This"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_chaining(request):
    html = "This"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

