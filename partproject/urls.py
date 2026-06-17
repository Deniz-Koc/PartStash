from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from partapi.views import (
    register_user,
    login_user,
    logout_user,
    ProjectViewSet,
    ComponentViewSet,
    CategoryViewSet,
    ProjectComponentViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"components", ComponentViewSet, basename="component")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(
    r"project-components", ProjectComponentViewSet, basename="projectcomponent"
)

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("logout", logout_user),
]
