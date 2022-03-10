from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from mainapp.models import Project, Todo
from users.models import User
from users.serializers import UserModelSerializer


class UserListingSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

    def to_representation(self, value):
        return f'{value.get_username()}'


class ProjectListingSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = UserListingSerializer(many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    project = ProjectListingSerializer(queryset=Project.objects.all())
    author = User.objects.all()

    class Meta:
        model = Todo
        fields = ('project', 'author', 'text', 'created_at', 'updated_at', 'is_active', 'url')

    def create(self, validated_data):
        project_data = validated_data.pop('project')
        Project.objects.create(users=[self.author], **project_data)
        todo = Todo.objects.create(**validated_data)

        return todo

