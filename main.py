from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

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
    raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car.id != car_id]
    return {"message": "Car deleted"}
