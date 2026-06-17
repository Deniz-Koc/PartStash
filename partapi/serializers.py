from rest_framework import serializers
from partapi.models import Project, Component, Category, ProjectComponent


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "label"]


class ComponentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Component
        fields = ["id", "name", "part_number", "description", "category", "category_id"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_on"]


class ProjectComponentSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)
    component_id = serializers.IntegerField(write_only=True)
    project_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProjectComponent
        fields = ["id", "component", "component_id", "project_id", "quantity"]
