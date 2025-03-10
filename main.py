from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow requests from your website
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pitstop-usa.com"],  # ✅ Add your actual website URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarData(BaseModel):
    year: int
    make: str
    model: str
    auction_price: float
    damage_type: str

# Define repair costs based on damage type
REPAIR_COSTS = {
    "Front-End Damage": 5000,
    "Rear-End Damage": 4000,
    "Side Damage": 4500,
    "Flood Damage": 10000,
    "Frame Damage": 8000
}

@app.get("/")
def home():
    return {"message": "Salvage Car Profit Calculator API is live!"}

@app.post("/calculate")
def calculate_profit(car: CarData):
    repair_cost = REPAIR_COSTS.get(car.damage_type, 6000)  # Default repair cost
    auction_fees = car.auction_price * 0.10  # 10% auction fees
    transport_cost = 1000  # Estimated transport cost
    total_investment = car.auction_price + repair_cost + auction_fees + transport_cost

    # Estimated rebuilt value
    rebuilt_value = car.auction_price * 1.8 if "Frame" not in car.damage_type else car.auction_price * 1.5

    # Profit calculations
    profit_best_case = rebuilt_value - total_investment
    profit_worst_case = (rebuilt_value * 0.85) - total_investment  # If sold at 85% of expected value

    return {
        "repair_cost": repair_cost,
        "auction_fees": auction_fees,
        "transport_cost": transport_cost,
        "total_investment": total_investment,
        "rebuilt_value": rebuilt_value,
        "profit_best_case": profit_best_case,
        "profit_worst_case": profit_worst_case
    }
}