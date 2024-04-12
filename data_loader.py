import json

def save(recipe_list:list, file_path:str):
    with open(file_path, 'w') as f:
        json.dump(recipe_list, f)

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
#      }]

# save(test_recipes, './recipes/test.json')
# print(load('./recipes/test.json'))
