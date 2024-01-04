"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from folio import views

from folio.views import SkillViewset, ItemViewset, ExperienceViewset, FormationViewset, TaskViewset, UserProfileViewset

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('skill', SkillViewset, basename='skill')
router.register('item', ItemViewset, basename='item')
router.register('experience', ExperienceViewset, basename='experience')
router.register('formation', FormationViewset, basename='formation')
router.register('task', TaskViewset, basename='task')
router.register('info', UserProfileViewset, basename='info')
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #path('sil', SkillWithItemListView.as_view(), name='sil'),
    path('', views.index),
]
