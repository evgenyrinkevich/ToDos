from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .pagination_settings import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter
from mainapp.models import Project, Todo
from mainapp.serializers import ProjectModelSerializer, TodoModelSerializer, TodoModelGetSerializer


class ProjectModelViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class TodoModelViewSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    filterset_class = ToDoFilter
    pagination_class = ToDoLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoModelGetSerializer
        return TodoModelSerializer

