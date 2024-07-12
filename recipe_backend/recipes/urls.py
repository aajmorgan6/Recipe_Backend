from django.urls import path
from .views import RecipeAllView, RecipeDetailView

urlpatterns = [
    path('all/', RecipeAllView.as_view()),
    path('<int:id>/', RecipeDetailView.as_view())
]