from rest_framework import serializers # Importing rest framework module
from projects.models import Project # Serializer based on our model (to recognize GET, POST, PUT and DELETE requests)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'technology', 'created_at']
        read_only_fields = ['created_at' ] # read_only_fields restric the fields defining just for reading