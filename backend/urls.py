"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from article import views as article_views
from trending import views as trending_views
from popular import views as popular_views
from latest import views as latest_views



router = routers.DefaultRouter()
router.register(r'article', article_views.ArticleView, 'article')
router.register(r'trending', trending_views.TrendingView, 'trending')
router.register(r'popular', popular_views.PopularView, 'popular')
router.register(r'latest', latest_views.LatestView, 'latest')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('article.urls')),
 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

