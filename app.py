from flask import Flask, request, jsonify
from flask_cors import CORS
from copart_scraper_script import fetch_vehicle_info  # Import your scraper function

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/")
def home():
    return jsonify({"message": "Salvage Car Profit Calculator API is live!"})

@app.route("/fetch_vehicle", methods=["GET"])
def fetch_vehicle():
    lot_number = request.args.get("lot")  # Get the lot number from the request
    if not lot_number:
        return jsonify({"error": "Missing lot number"}), 400
    
    vehicle_data = fetch_vehicle_info(lot_number)  # Call scraper function
    if not vehicle_data:
        return jsonify({"error": "Vehicle not found"}), 404
    
    return jsonify(vehicle_data)  # Return vehicle data as JSON

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
