from django.contrib import admin

# Register your models here.

from folio.models import UserProfile
from folio.models import Skill
from folio.models import Item
from folio.models import Experience
from folio.models import Task
from folio.models import Formation



admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Item)
admin.site.register(Experience)
admin.site.register(Task)
admin.site.register(Formation)



