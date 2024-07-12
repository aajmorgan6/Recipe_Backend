from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.

class RecipeAllView(APIView):

    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'ingredients': request.data.get('ingredients'),
            'steps': request.data.get('steps')
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetailView(APIView):

    def get(self, request, id, *args, **kwargs):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({'res': f'Recipe with id {id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({'res': f'Recipe with id {id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        recipe.delete()
        return Response({'res': 'Object deleted'}, status=status.HTTP_200_OK)