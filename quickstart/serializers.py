#This is the serializers file where we will define serializers.

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# Here, we are using Hyperlinked relations with HyperlinkedModelSerializer. We
# can use primary key or any other relations but Hyperlinking is a good RESTful
# design.
