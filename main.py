import random

def generate_recipe():
    recipe_names = ['Spaghetti Bolognese', 'Chicken Curry', 'Veggie Stir-fry', 'Fish Tacos', 'Beef Stroganoff']

    ingredients_list = [        ['spaghetti', 'minced meat', 'tomato sauce', 'onion', 'garlic', 'olive oil'],
        ['chicken breast', 'curry powder', 'coconut milk', 'rice', 'vegetables'],
        ['noodles', 'mixed vegetables', 'soy sauce', 'sesame oil'],
        ['fish fillets', 'taco shells', 'avocado', 'sour cream', 'lime'],
        ['beef', 'mushrooms', 'onion', 'sour cream', 'egg noodles']
    ]

    steps_list = [        ['Boil the spaghetti', 'Fry the minced meat', 'Add the tomato sauce', 'Serve with grated cheese'],
        ['Marinate the chicken in curry powder', 'Cook the chicken', 'Add the coconut milk', 'Serve with rice'],
        ['Stir-fry the vegetables', 'Boil the noodles', 'Mix the vegetables and noodles', 'Serve with soy sauce'],
        ['Grill the fish', 'Prepare the tacos with fish and avocado', 'Serve with sour cream and lime'],
        ['Fry the beef and onions', 'Add the sour cream', 'Serve with egg noodles']
    ]

    index = random.randint(0, len(recipe_names)-1)

    recipe = {
        "name": recipe_names[index],
        "ingredients": ingredients_list[index],
        "steps": steps_list[index]
    }

    return recipe

if __name__ == "__main__":
    while True:
        print("\nGenerating a random recipe...\n")
        recipe = generate_recipe()
        print(f"Recipe Name: {recipe['name']}")
        print("Ingredients:")
        for i, ingredient in enumerate(recipe['ingredients'], 1):
            print(f"{i}. {ingredient}")
        print("Steps:")
        for i, step in enumerate(recipe['steps'], 1):
            print(f"{i}. {step}")

        another = input("\nGenerate another recipe? (yes/no): ")
        if another.lower() != 'yes':
            break
