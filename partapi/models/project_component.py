from django.db import models


class ProjectComponent(models.Model):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="project_components"
    )
    component = models.ForeignKey(
        "Component", on_delete=models.CASCADE, related_name="project_components"
    )
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ("project", "component")
