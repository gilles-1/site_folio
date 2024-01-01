from rest_framework.serializers import ModelSerializer
 
from folio.models import Skill, Item, Experience, Formation, Task, UserProfile

class ItemSerializer(ModelSerializer):
 
    class Meta:
        model = Item
        fields = '__all__'
 
class SkillSerializer(ModelSerializer):
    item_set = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Skill
        fields = '__all__'



class ExperienceSerializer(ModelSerializer):
 
    class Meta:
        model = Experience
        fields = '__all__'

class FormationSerializer(ModelSerializer):
 
    class Meta:
        model = Formation
        fields = '__all__'

class TaskSerializer(ModelSerializer):
 
    class Meta:
        model = Task
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
 
    class Meta:
        model = UserProfile
        fields = '__all__'

