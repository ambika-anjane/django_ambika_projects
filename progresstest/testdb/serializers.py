from django.contrib.auth.models import User, Group
from rest_framework import serializers
from testdb.models import Sources

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SourcesSerializers(serializers.ModelSerializer):
    #setCode = serializers.CharField(read_only=True, source="set.code")

    class Meta:
        model = Sources
        fields = ['name','column1']
        '''
        extra_fields = ['setCode', 'name']

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(SourcesSerializers, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
        '''