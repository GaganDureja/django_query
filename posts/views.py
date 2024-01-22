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
    all_blogs = Entry.objects.order_by('-id')
    html = "Blogs with latest/order by id desc <br><br>"
    for entry in all_blogs:
        html+= f"Heading - {entry.headline}, ID - {entry.id} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_values(request):
    all_blogs = Entry.objects.values('id','headline')
    html = "Blogs with only 2 values of id and headline  <br><br>"
    for entry in all_blogs:
        html+= f"Heading - {entry['headline']}, ID - {entry['id']} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_distinct(request):
    dis_auth = Entry.objects.values('authors').distinct()
    html = "  Distinct author if repeated in entry  <br><br>"
    for entry in dis_auth:
        author_name = Author.objects.filter(id=entry['authors'])[0]
        html+= f"Author - {author_name} <br>"        
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_slicing(request):
    first_2blogs = Blog.objects.all()[:2]
    html = "  First 2 blogs  <br><br>"
    for blog in first_2blogs:
        html+= f"{blog} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

def test_chaining(request):
    all_blogs = (
        Entry.objects.filter(authors='1')
                .exclude(rating='1')
                .filter(pub_date__gt='2020-01-01')
                .order_by('-id')
    )
    html = "  Multiple filter used above if used in single its called chaining  <br><br>"
    for entry in all_blogs:
        html+= f"Heading - {entry.headline}, ID - {entry.id} <br>"
    html+= '<br><button onclick="self.close()">Close</button>'

    return HttpResponse(html)

