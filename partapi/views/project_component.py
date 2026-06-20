from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from partapi.models import ProjectComponent, Project, Component
from partapi.serializers import ProjectComponentSerializer


class ProjectComponentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        project_components = ProjectComponent.objects.filter(
            project__user=request.auth.user
        )
        project = request.query_params.get("project", None)
        if project is not None:
            project_components = project_components.filter(project_id=project)
        component = request.query_params.get("component", None)
        if component is not None:
            project_components = project_components.filter(component_id=component)
        serializer = ProjectComponentSerializer(project_components, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project_component = ProjectComponent.objects.get(
            pk=pk, project__user=request.auth.user
        )
        serializer = ProjectComponentSerializer(project_component)
        return Response(serializer.data)

    def create(self, request):
        project = Project.objects.get(
            pk=request.data["project_id"], user=request.auth.user
        )
        component = Component.objects.get(
            pk=request.data["component_id"], user=request.auth.user
        )
        project_component = ProjectComponent.objects.create(
            project=project,
            component=component,
            quantity=request.data.get("quantity", 1),
        )
        serializer = ProjectComponentSerializer(project_component)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        project_component = ProjectComponent.objects.get(
            pk=pk, project__user=request.auth.user
        )
        project_component.quantity = request.data.get(
            "quantity", project_component.quantity
        )
        project_component.save()
        serializer = ProjectComponentSerializer(project_component)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        project_component = ProjectComponent.objects.get(
            pk=pk, project__user=request.auth.user
        )
        project_component.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
