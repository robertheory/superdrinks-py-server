from fastapi import FastAPI
from pydantic import BaseModel
import shortuuid
import sqlite3

connection = sqlite3.connect("./sqlitedata.sqlite3")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS drinks (id TEXT PRIMARY KEY, name TEXT, description TEXT, prepare_method TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS ingredients (id TEXT PRIMARY KEY, name TEXT, quantity REAL, prepare TEXT, description TEXT, unit TEXT, drink_id TEXT, FOREIGN KEY(drink_id) REFERENCES drinks(id))")

connection.commit()
connection.close()


class Ingredient(BaseModel):
    _id: str
    name: str
    quantity: float
    prepare: str
    description: str
    unit: str


class Drink(BaseModel):
    _id: str
    name: str
    description: str
    prepare_method: str
    ingredients: list[Ingredient]


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/drinks")
async def list_drinks():
    connection = sqlite3.connect("./sqlitedata.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM drinks")
    drinks = cursor.fetchall()
    cursor.execute("SELECT * FROM ingredients")
    ingredients = cursor.fetchall()
    connection.close()

    drink_list = []
    for drink in drinks:
        drink_list.append({
            "id": drink[0],
            "name": drink[1],
            "description": drink[2],
            "prepare_method": drink[3],
            "ingredients": []
        })
    
    for ingredient in ingredients:
        for drink in drink_list:
            if ingredient[6] == drink['id']:
                drink['ingredients'].append({
                    "id": ingredient[0],
                    "name": ingredient[1],
                    "quantity": ingredient[2],
                    "prepare": ingredient[3],
                    "description": ingredient[4],
                    "unit": ingredient[5]
                })
    return drink_list


@app.get("/drink/{drink_id}")
async def get_drink(drink_id):
    connection = sqlite3.connect("./sqlitedata.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM drinks WHERE id=?", (drink_id,))
    drink = cursor.fetchone()
    cursor.execute("SELECT * FROM ingredients WHERE drink_id=?", (drink_id,))
    ingredients = cursor.fetchall()
    connection.close()

    drink_list = {
        "id": drink[0],
        "name": drink[1],
        "description": drink[2],
        "prepare_method": drink[3],
        "ingredients": []
    }

    for ingredient in ingredients:
        drink_list['ingredients'].append({
            "id": ingredient[0],
            "name": ingredient[1],
            "quantity": ingredient[2],
            "prepare": ingredient[3],
            "description": ingredient[4],
            "unit": ingredient[5]
        })
    return drink_list


@app.post("/drink")
async def create_drink(drink: Drink):
    connection = sqlite3.connect("./sqlitedata.sqlite3")
    cursor = connection.cursor()
    newDrinkId = shortuuid.uuid()
    cursor.execute("INSERT INTO drinks VALUES (?, ?, ?, ?)", (newDrinkId, drink.name, drink.description, drink.prepare_method))
    for ingredient in drink.ingredients:
        cursor.execute("INSERT INTO ingredients VALUES (?, ?, ?, ?, ?, ?, ?)", (shortuuid.uuid(), ingredient.name, ingredient.quantity, ingredient.prepare, ingredient.description, ingredient.unit, newDrinkId))
    connection.commit()
    connection.close()
    return drink


@app.delete("/drink/{drink_id}")
async def delete_drinks(drink_id):
    connection = sqlite3.connect("./sqlitedata.sqlite3")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM drinks WHERE id=?", (drink_id,))
    cursor.execute("DELETE FROM ingredients WHERE drink_id=?", (drink_id,))
    connection.commit()
    connection.close()
    return {"message": "Drink deleted"}

@app.patch("/drink/{drink_id}")
async def update_drink(drink_id, newDrink: Drink):
    
    if newDrink.name:
        connection = sqlite3.connect("./sqlitedata.sqlite3")
        cursor = connection.cursor()
        cursor.execute("UPDATE drinks SET name=? WHERE id=?", (newDrink.name, drink_id))
        connection.commit()
        connection.close()

    if newDrink.description:
        connection = sqlite3.connect("./sqlitedata.sqlite3")
        cursor = connection.cursor()
        cursor.execute("UPDATE drinks SET description=? WHERE id=?", (newDrink.description, drink_id))
        connection.commit()
        connection.close()
    
    if newDrink.prepare_method:
        connection = sqlite3.connect("./sqlitedata.sqlite3")
        cursor = connection.cursor()
        cursor.execute("UPDATE drinks SET prepare_method=? WHERE id=?", (newDrink.prepare_method, drink_id))
        connection.commit()
        connection.close()

    if newDrink.ingredients:
        connection = sqlite3.connect("./sqlitedata.sqlite3")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ingredients WHERE drink_id=?", (drink_id,))
        for ingredient in newDrink.ingredients:
            cursor.execute("INSERT INTO ingredients VALUES (?, ?, ?, ?, ?, ?, ?)", (shortuuid.uuid(), ingredient.name, ingredient.quantity, ingredient.prepare, ingredient.description, ingredient.unit, drink_id))
        connection.commit()
        connection.close()
    
    return {"message": "Drink updated"}

