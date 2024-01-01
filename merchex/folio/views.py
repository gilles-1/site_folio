from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from django.shortcuts import render
from folio.models import Skill, Item, Experience, Formation, Task, UserProfile
from folio.serializers import SkillSerializer


# Create your views here.
def index(request):
    #bands = Band.objects.all()
    dd = 15
    return render(request, 'folio/index.html', {'d': dd})

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
 
from folio.models import Skill, Item, Experience, Formation, Task, UserProfile
from folio.serializers import SkillSerializer, ItemSerializer, ExperienceSerializer, FormationSerializer, TaskSerializer, UserProfileSerializer
 
class ItemViewset(ReadOnlyModelViewSet):
 
    serializer_class = ItemSerializer
 
    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset
    
class SkillViewset(ReadOnlyModelViewSet):
 
    serializer_class = SkillSerializer
 
    def get_queryset(self):
        queryset = Skill.objects.all()
        return queryset
    
