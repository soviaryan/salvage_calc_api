from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CarData(BaseModel):
    year: int
    make: str
    model: str
    auction_price: float
    damage_type: str

@app.post("/calculate")
def calculate_profit(car: CarData):
    repair_cost = 5000  # Example repair cost
    total_investment = car.auction_price + repair_cost

    return {
        "repair_cost": repair_cost,
        "total_investment": total_investment
    }