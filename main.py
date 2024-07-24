import json
import os

RECIPE_FILE = "recipes.json"

def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as f:
        json.dump(recipes, f, indent=4)

def display_recipes(recipes):
    if not recipes:
        print("No recipes found.")
        return
    for recipe_name in recipes:
        print(f"- {recipe_name}")

def view_recipe(recipes, name):
    recipe = recipes.get(name)
    if recipe:
        print(f"Recipe: {name}")
        print("Ingredients:")
        for ingredient in recipe.get("ingredients", []):
            print(f"  - {ingredient}")
        print("Instructions:")
        print(recipe.get("instructions", "No instructions provided."))
    else:
        print("Recipe not found.")

def add_recipe(recipes):
    name = input("Enter recipe name: ")
    if name in recipes:
        print("Recipe already exists.")
        return
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    instructions = input("Enter instructions: ")
    recipes[name] = {
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions
    }
    save_recipes(recipes)
    print("Recipe added.")

def delete_recipe(recipes):
    name = input("Enter recipe name to delete: ")
    if name in recipes:
        del recipes[name]
        save_recipes(recipes)
        print("Recipe deleted.")
    else:
        print("Recipe not found.")

def main():
    recipes = load_recipes()
    
    while True:
        print("\nRecipe Manager Application")
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. Delete Recipe")
        print("4. List Recipes")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            name = input("Enter recipe name to view: ")
            view_recipe(recipes, name)
        elif choice == "3":
            delete_recipe(recipes)
        elif choice == "4":
            display_recipes(recipes)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

