"""Docstring"""
# Dein Code kommt hier hin
import json


def adjust_recipe(recipe, number_of_people):
    people = number_of_people/recipe["servings"]
    adjusted_ingreds = {}
    for i, a in recipe["ingredients"].items():
        adjusted_ingreds[i] = a*people

    adjusted_recipe = {
        "title": recipe["title"],
        "ingredients": adjusted_ingreds,
        "servings": number_of_people
    }
    return adjusted_recipe


def load_recipe(json_recipe):
    return json.loads(json_recipe)


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti":' \
                  ' 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    # Dein Code kommt hier hin
    print(adjust_recipe(load_recipe(recipe_json), 8))
