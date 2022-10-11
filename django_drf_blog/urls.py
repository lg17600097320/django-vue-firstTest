"""django_drf_blog URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from  article.views import *
from  comment.views import CommentModelViewSet
from  django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from  user_info.views import UserModelViewSet
router = DefaultRouter()
router.register('article',ArticleModelViewSet)
router.register('category',CategoryModelViewSet)
router.register('tag',TagModelViewSet)
router.register('avatar',AvatarModelViewSet)
router.register('comment',CommentModelViewSet)
router.register('user',UserModelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    # path('api/article/',include('article.urls',namespace='article'))
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    # path('test',TestRelated_name)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

