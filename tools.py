import uuid
import sqlite3


def database_connection():
    return sqlite3.connect("recipy.db")


def add_user(user_values: tuple):
    """
    Function to add user

    user_values is a tuple of type:
    (username: String, real_name: String, image: blob, description: String, password: String (hash))
    """
    con = database_connection()
    cur = con.cursor()
    if get_user(user_values[0]) is not None:
        return None
    command = """ INSERT INTO users 
    (username, real_name, image, description, password) 
    VALUES (?, ?, ?, ?, ?)"""
    cur.execute(command, user_values)
    con.commit()
    cur.close()
    con.close()


def add_recipe(recipe_values: tuple):
    """
    Function for adding recipe

    recipe_values is a tuple with the following values:
    (title: String, owner: String, time: int, ingredients: String (json), amount: String (json), unit: String (json), image: blob, tags: String (json), description: String, id: String (uuid))
    """
    con = database_connection()
    cur = con.cursor()
    if get_user(recipe_values[1]) is None:
        return None
    command = """ INSERT INTO recipes 
    (title, owner, time, ingredients, amount, unit, image, tags, description, id)
    VALUES
    (?,?,?,?,?,?,?,?,?,?)"""
    cur.execute(command, recipe_values)
    con.commit()
    cur.close()
    con.close()


# def filter(recipes:list, ingredients:list):

#     filtered_recipes = []

#     for recipe in recipes:

#         valid = True
#         for needed_ingredient in ingredients:

#             if valid == True:

#                 valid = False
#                 for ingredient in recipe['ingredients']:
#                     if ingredient[0] == needed_ingredient:
#                         valid = True
#                         break

#                 continue
#             break

#         if valid:
#             filtered_recipes.append(recipe)

#     return filtered_recipes

# TESTING FILTER
# print([item['title'] for item in filter(data_loader.load('./recipes/test.json'), ['eggs'])]) # output ['American Pancakes', 'Spaghetti Carbonara']


def get_user(username: str):

    con = database_connection()
    cur = con.cursor()
    res = cur.execute(f"SELECT * FROM users WHERE username='{username}'")
    user_data = res.fetchone()
    cur.close()
    con.close()

    return user_data


if __name__ == "__main__":
    print("tests!")
    func = input("input function to test: ")

    if func == "add_user":
        username = input("username: ")
        real_name = input("real_name: ")
        image = open(input("image (filepath): "), "rb").read()
        description = input("description: ")
        password = input("password: ")
        add_user((username, real_name, image, description, password))

    if func == "get_user":
        print(get_user(input("username: ")))

    if func == "add_recipe":
        title = input("title: ")
        owner = input("owner: ")
        time = int(input("time: "))
        ingredients = input("ingredients: ")
        amount = input("amount: ")
        unit = input("unit: ")
        image = open(input("image (filepath): "), "rb").read()
        tags = input("tags: ")
        description = input("description: ")
        id = str(uuid.uuid4())
        add_recipe(
            (
                title,
                owner,
                time,
                ingredients,
                amount,
                unit,
                image,
                tags,
                description,
                id,
            )
        )
