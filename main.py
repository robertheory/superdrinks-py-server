from fastapi import FastAPI
from pydantic import BaseModel
import shortuuid


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

drink_list = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/drinks")
async def read_drinks():
    return drink_list


@app.get("/drink/{drink_id}")
async def read_drink(drink_id):
    for drink in drink_list:
        if drink['id'] == drink_id:
            return drink
    return {"message": "Drink not found"}


@app.post("/drink")
async def create_drink(drink: Drink):

    drink_list.append({
        "id": shortuuid.uuid(),
        "name": drink.name,
        "description": drink.description,
        "prepare_method": drink.prepare_method,
        "ingredients": drink.ingredients
    })
    return drink


@app.delete("/drink/{drink_id}")
async def delete_drinks(drink_id):
    for drink in drink_list:
        if drink['id'] == drink_id:
            drink_list.remove(drink)
            return {"message": "Drink deleted"}
    return {"message": "Drink not found"}


@app.patch("/drink/{drink_id}")
async def update_drink(drink_id, newDrink: Drink):
    for drink in drink_list:
        if drink['id'] == drink_id:
            drink['name'] = newDrink.name
            drink['description'] = newDrink.description
            drink['prepare_method'] = newDrink.prepare_method
            drink['ingredients'] = newDrink.ingredients
            return drink
    return {"message": "Drink not found"}
