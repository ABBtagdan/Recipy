import data_loader

def filter(recipes:list, ingredients:list):

    filtered_recipes = []

    for recipe in recipes:

        valid = True
        for needed_ingredient in ingredients:

            if valid == True:

                valid = False
                for ingredient in recipe['ingredients']:
                    if ingredient[0] == needed_ingredient:
                        valid = True
                        break

                continue
            break

        if valid:
            filtered_recipes.append(recipe)

    return filtered_recipes

# TESTING FILTER
# print([item['title'] for item in filter(data_loader.load('./recipes/test.json'), ['eggs'])]) # output ['American Pancakes', 'Spaghetti Carbonara']

def sort():
    pass
