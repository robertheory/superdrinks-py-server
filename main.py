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
