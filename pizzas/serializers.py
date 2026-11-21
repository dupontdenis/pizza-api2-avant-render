from rest_framework import serializers
from .models import Pizza, Ingredient




class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "price", "calories"]




class PizzaSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    # def get_price(self, pizza):
    #     return sum(
    #         (ingredient.price for ingredient in pizza.ingredients.all()),
    #         Decimal("0.00")
    #     )

    class Meta:
        model = Pizza
        fields = ["id", "name", "ingredients"]
     # fields = ["id", "name", "ingredients", "price"]
