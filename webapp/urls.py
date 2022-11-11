"""webapp URL Configuration

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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from top_page.views import index
from kaup_index.views import kaup
from bmi_index.views import bmi
# from blog.views import blog
from valuation.views import valuation
from hinshi_checker.views import hinshi_checker
from .sitemaps import Static_Sitemap

sitemaps = {
    'static': Static_Sitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kaup/', kaup, name='kaup'),
    path('bmi/', bmi, name='bmi'),
    path('valuation/', valuation, name='valuation'),
    path('blog/', include('blog.urls')),
    path('hinshi-checker', hinshi_checker, name='hinshi_checker'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='sitemaps'),
]
