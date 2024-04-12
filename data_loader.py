import json

def save(recipes:list, file_path:str):
    with open(file_path, 'w') as f:
        json.dump(recipes, f)

def load(file_path:str):
    with open(file_path) as f:
        loaded_recipes = json.loads(f.read())

    return loaded_recipes

# TESTS

# test_recipes = [
#     {'title': 'American Pancakes',
#      'time': 40,
#      'ingredients': [('flour', 1, 'dl'), ('sugar', 0.5, 'dl'), ('butter', 50, 'g'), ('vanilla', 15, 'ml'), ('baking soda', 30, 'ml'), ('milk', 2, 'dl'), ('eggs', 2, 'st')],
#      'image_url': 'https://ichef.bbci.co.uk/food/ic/food_16x9_832/recipes/fluffyamericanpancak_74828_16x9.jpg',
#      'tags': ['breakfast', 'pancakes', 'sweet'],
#      'description': "American pancakes are a perfect breakfast if you want something sweet. They're easy to make and contain ingredients that most people have at home!",
#      'recipe': "Step 1:\nMelt the butter and add eggs and milk.\nStep 2:\nAdd the rest of the ingredients to the mixture.\nStep 3:\nCook on medium heat until golden. Grease your pan in between each set of pancakes."
#      },
#     {'title': 'Spaghetti Carbonara',
#      'time': 25,
#      'ingredients': [('spaghetti', 200, 'g'), ('bacon', 150, 'g'), ('eggs', 2, 'st'), ('parmesan cheese', 50, 'g'), ('black pepper', None, 'to taste')],
#      'image_url': 'https://www.inspiredtaste.net/wp-content/uploads/2019/03/Spaghetti-Carbonara-Recipe-3-1200.jpg',
#      'tags': ['dinner', 'pasta'],
#      'description': "Spaghetti Carbonara is a classic Italian pasta dish made with eggs, cheese, bacon, and black pepper. It's creamy, savory, and satisfying!",
#      'recipe': "Step 1:\nCook spaghetti according to package instructions.\nStep 2:\nWhile spaghetti cooks, fry bacon until crispy.\nStep 3:\nWhisk eggs, cheese, and black pepper in a bowl.\nStep 4:\nDrain spaghetti and add to bacon, then pour egg mixture over pasta. Toss until well coated. Serve immediately."
#      },
#     {'title': 'Chicken Stir-Fry',
#      'time': 30,
#      'ingredients': [('chicken breast', 400, 'g'), ('bell peppers', 2, 'st'), ('onion', 1, 'st'), ('garlic', 2, 'cloves'), ('soy sauce', 60, 'ml'), ('vegetable oil', 30, 'ml'), ('rice', 2, 'cups')],
#      'image_url': 'https://www.spendwithpennies.com/wp-content/uploads/2019/07/Chicken-Stir-Fry-SpendWithPennies-3.jpg',
#      'tags': ['dinner', 'chicken', 'stir-fry'],
#      'description': "Chicken Stir-Fry is a quick and flavorful dish loaded with tender chicken, crisp vegetables, and a savory sauce. It's perfect for a busy weeknight dinner!",
#      'recipe': "Step 1:\nSlice chicken, bell peppers, and onion.\nStep 2:\nHeat oil in a pan and sauté garlic until fragrant.\nStep 3:\nAdd chicken and cook until browned.\nStep 4:\nAdd vegetables and stir-fry until tender.\nStep 5:\nPour in soy sauce and cook until heated through. Serve over cooked rice."
#      },
#     {'title': 'Caprese Salad',
#      'time': 10,
#      'ingredients': [('tomatoes', 4, 'st'), ('fresh mozzarella cheese', 200, 'g'), ('fresh basil leaves', None, 'to taste'), ('balsamic vinegar', 30, 'ml'), ('extra virgin olive oil', 30, 'ml'), ('salt', None, 'to taste')],
#      'image_url': 'https://www.simplyrecipes.com/wp-content/uploads/2020/06/Caprese-Salad-LEAD-3.jpg',
#      'tags': ['salad', 'vegetarian'],
#      'description': "Caprese Salad is a simple Italian salad made with fresh tomatoes, mozzarella cheese, basil leaves, and a drizzle of balsamic vinegar and olive oil. It's light, refreshing, and bursting with flavor!",
#      'recipe': "Step 1:\nSlice tomatoes and mozzarella cheese into rounds.\nStep 2:\nArrange tomato and mozzarella slices on a plate, alternating with basil leaves.\nStep 3:\nDrizzle with balsamic vinegar and olive oil.\nStep 4:\nSeason with salt to taste. Serve immediately."
#      }
# ]

# save(test_recipes, './recipes/test.json')
# print(load('./recipes/test.json'))
