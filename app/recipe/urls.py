"""
URL mappings for the recipe app.
"""

from django.urls import (  # type: ignore
    path,
    include,
)

from rest_framework.routers import DefaultRouter  # type: ignore

from recipe import views


router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)
router.register("tags", views.TagViewSet)

app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
