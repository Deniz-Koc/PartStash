from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from partapi.models import Project
from partapi.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        projects = Project.objects.filter(user=request.auth.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = Project.objects.get(pk=pk, user=request.auth.user)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        project = Project.objects.get(pk=pk, user=request.auth.user)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        project = Project.objects.get(pk=pk, user=request.auth.user)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
