from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Query all the data
    permission_classes = [permissions.AllowAny] # Who has permissions to request
    serializer_class = ProjectSerializer # To which serializer is applied to this configurations