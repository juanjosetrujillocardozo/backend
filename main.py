from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()

class Car(BaseModel):
    id: int
    marca: str
    sucursal: str
    aspirante: str

cars = []

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    cars.append(car)
    return car

@app.get("/cars/", response_model=List[Car])
def get_cars():
    return cars

@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, updated_car: Car):
    for car in cars:
        if car.id == car_id:
            car.marca = updated_car.marca
            car.sucursal = updated_car.sucursal
            car.aspirante = updated_car.aspirante
            return car
    return {"error": "Car not found"}

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car.id != car_id]
    return {"message": "Car deleted"}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Car Dealership</title>
            <link rel="icon" href="/favicon.ico" type="image/x-icon">
        </head>
        <body>
            <h1>Welcome to the Car Dealership API</h1>
        </body>
    </html>
    """

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {"message": "No favicon found"}