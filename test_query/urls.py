"""test_query URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('annotate/', test_annotate),
    path('aggregate/', test_aggregate),
    path('filter/', test_filter),
    path('exclude/', test_exclude),
    path('order_by/', test_order_by),
    path('values/', test_values),
    path('distinct/', test_distinct),
    path('slicing/', test_slicing),
    path('chaining/', test_chaining),
    
]
