import uuid
import sqlite3

# new idea:
# execute_fetchmany(user_recipes_query("tagdan") + order_by_query("date"))


def database_connection():
    return sqlite3.connect("recipy.db")


def execute_fetchone(query: str):
    con = database_connection()
    cur = con.cursor()
    res = cur.execute(query).fetchone()
    cur.close()
    con.close()

    return res


def execute_fetchall(query: str):
    con = database_connection()
    cur = con.cursor()
    res = cur.execute(query).fetchall()
    cur.close()
    con.close()

    return res


def execute_fetchmany(query: str, n: int):
    con = database_connection()
    cur = con.cursor()
    res = cur.execute(query).fetchmany(n)
    cur.close()
    con.close()

    return res


def add_user(user_values: tuple):
    """
    Function to add user

    user_values is a tuple of type:
    (username: String, real_name: String, image: blob, description: String, password: String (hash))
    """
    con = database_connection()
    cur = con.cursor()
    if execute_fetchone(get_user_query(user_values[0])) is not None:
        return None
    command = """ INSERT INTO users 
    (username, real_name, image, description, password) 
    VALUES (?, ?, ?, ?, ?)"""
    cur.execute(command, user_values)
    con.commit()
    cur.close()
    con.close()
    return True


def add_recipe(recipe_values: tuple):
    """
    Function for adding recipe

    recipe_values is a tuple with the following values:
    (title: String, owner: String, time: int, ingredients: String (json), amount: String (json), unit: String (json), image: blob, tags: String (json), description: String, id: String (uuid), date: date)
    """
    con = database_connection()
    cur = con.cursor()
    if execute_fetchone(get_user_query(recipe_values[1])) is None:
        return False
    command = """ INSERT INTO recipes 
    (title, owner, time, ingredients, amount, unit, image, tags, description, id, date)
    VALUES
    (?,?,?,?,?,?,?,?,?,?,?)"""
    cur.execute(command, recipe_values)
    con.commit()
    cur.close()
    con.close()
    return True


def delete_recipe(recipe_id: str, username: str):
    con = database_connection()
    cur = con.cursor()
    command = """
    DELETE FROM recipes WHERE id = ? AND owner = ?
    """
    cur.execute(
        command,
        (
            recipe_id,
            username,
        ),
    )
    con.commit()
    cur.close()
    con.close()


def safe(parameter: str) -> str:
    return parameter.replace("'", "''")


def get_user_query(username: str):
    return f"SELECT * FROM users WHERE username='{safe(username)}'"  # use fetch one


def get_user_recipes_query(username: str):
    return f"SELECT * FROM recipes WHERE owner='{safe(username)}'"  # use fetch all


def get_recipe_by_id_query(recipe_id: str):
    return f"SELECT * FROM recipes WHERE id='{safe(recipe_id)}'"  # use fetch one


def get_all_recipes_query():
    return f"SELECT * FROM recipes"  # use fetch many to get n recipes


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

    if func == "get_user":
        print(execute_fetchone(get_user_query(input("username: "))))

    if func == "get_user_recipes":
        print(
            [
                item[0]
                for item in execute_fetchall(
                    get_user_recipes_query(input("username: "))
                )
            ]
        )

    if func == "get_recipe_by_id":
        print(
            execute_fetchone(
                get_recipe_by_id_query("19a7c874-2201-4045-bd21-d8af45533151")
            )[0]
        )  # should output pasta

    if func == "get_n_recipes":
        print(
            [
                item[0]
                for item in execute_fetchmany(
                    get_all_recipes_query(), int(input("amount of recipes: "))
                )
            ]
        )
