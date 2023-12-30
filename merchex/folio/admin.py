from django.contrib import admin

# Register your models here.

from folio.models import UserProfile
from folio.models import Skill
from folio.models import Item
from folio.models import Experience
from folio.models import Task
from folio.models import Formation

class UserAdminAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'adresse', 'city') # liste les champs que nous voulons sur l'affichage de la liste
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'item') 
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name') 
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('institution', 'type', 'title', 'city', 'country','started_at', 'ended_at', 'task') 
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'technology') 
class FormationAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'type', 'city', 'country','started_at', 'ended_at', 'in_progress') 

admin.site.register(UserProfile, Skill, Item, Experience, Task, Formation, UserAdminAdmin, SkillAdmin,
                    ItemAdmin, ExperienceAdmin, TaskAdmin, FormationAdmin)

