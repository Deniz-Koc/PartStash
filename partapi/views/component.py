from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from partapi.models import Component
from partapi.serializers import ComponentSerializer


class ComponentViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):
        components = Component.objects.filter(user=request.auth.user)
        serializer = ComponentSerializer(components, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        component = Component.objects.get(pk=pk, user=request.auth.user)
        serializer = ComponentSerializer(component)
        return Response(serializer.data)

    def create(self, request):
        serializer = ComponentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        component = Component.objects.get(pk=pk, user=request.auth.user)
        serializer = ComponentSerializer(component, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        component = Component.objects.get(pk=pk, user=request.auth.user)
        component.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
