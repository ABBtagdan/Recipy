import data_loader
import sqlite3


def database_connection():
    return sqlite3.connect("recipy.db")
    

def add_user(user_values: tuple):
    con = database_connection()
    cur = con.cursor();
    command = """ INSERT INTO users 
    (username, real_name, image, description, password) 
    VALUES (?, ?, ?, ?, ?)"""
    cur.execute(command, user_values)
    con.commit()
    cur.close()
    con.close()


def add_recipe(recipe_values: tuple):
    pass 

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

if __name__ == "__main__":
    print("tests!")
    func = input("input function to test: ")
    if func == "add_user":
        username = input("username: ")
        real_name = input("real_name: ")
        image = open(input("image (filepath): "), 'rb').read()
        description = input("description: ")
        password = input('password: ')
        add_user((username, real_name, image, description, password))
