from flask import Flask, request, jsonify
from flask_cors import CORS
from copart_scraper_script import fetch_vehicle_info  # Ensure correct import

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests

@app.route("/fetch_vehicle", methods=["GET"])
def fetch_vehicle():
    lot_number = request.args.get("lot")
    if not lot_number:
        return jsonify({"error": "Missing lot number"}), 400
    
    vehicle_data = fetch_vehicle_info(lot_number)
    if not vehicle_data:
        return jsonify({"error": "Vehicle not found"}), 404
    
    return jsonify(vehicle_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

