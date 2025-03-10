from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CarData(BaseModel):
    year: int
    make: str
    model: str
    auction_price: float
    damage_type: str

# Placeholder repair costs (expand this later)
REPAIR_COSTS = {
    "Front-End Damage": 5000,
    "Rear-End Damage": 4000,
    "Side Damage": 4500,
    "Flood Damage": 10000,
    "Frame Damage": 8000
}

@app.post("/calculate")
def calculate_profit(car: CarData):
    repair_cost = REPAIR_COSTS.get(car.damage_type, 6000)
    auction_fees = car.auction_price * 0.10
    transport_cost = 1000
    total_investment = car.auction_price + repair_cost + auction_fees + transport_cost

    rebuilt_value = car.auction_price * 1.8 if "Frame" not in car.damage_type else car.auction_price * 1.5

    profit_best_case = rebuilt_value - total_investment
    profit_worst_case = (rebuilt_value * 0.85) - total_investment  

    return {
        "repair_cost": repair_cost,
        "auction_fees": auction_fees,
        "transport_cost": transport_cost,
        "total_investment": total_investment,
        "rebuilt_value": rebuilt_value,
        "profit_best_case": profit_best_case,
        "profit_worst_case": profit_worst_case
    }