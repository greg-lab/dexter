from django.contrib.auth.models import User, Group
from api.models import Translation
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Translation
		fields = ['polish', 'english']        		