from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Car(BaseModel):
    id: int
    marca: str
    sucursal: str
    aspirante: str

class CarCreate(BaseModel):
    marca: str
    sucursal: str
    aspirante: str

cars = []
car_id_counter = 1

@app.post("/cars/", response_model=Car)
def create_car(car: CarCreate):
    global car_id_counter
    new_car = Car(id=car_id_counter, **car.dict())
    cars.append(new_car)
    car_id_counter += 1
    return new_car

@app.get("/cars/", response_model=List[Car])
def get_cars():
    return cars

@app.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarCreate):
    for existing_car in cars:
        if existing_car.id == car_id:
            existing_car.marca = car.marca
            existing_car.sucursal = car.sucursal
            existing_car.aspirante = car.aspirante
            return existing_car
    raise HTTPException(status_code=404, detail="Car not found")

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car.id != car_id]
    return {"message": "Car deleted successfully"}
