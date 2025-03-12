from flask import Flask, request, jsonify
from flask_cors import CORS
from copart_scraper_script import fetch_vehicle_info  # Ensure this exists

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Salvage Car Profit Calculator API is live!"})

@app.route('/fetch_vehicle', methods=['GET'])
def fetch_vehicle():
    lot_number = request.args.get('lot')
    if not lot_number:
        return jsonify({"error": "No lot number provided"}), 400

    vehicle_data = fetch_vehicle_info(lot_number)  # Call scraper function
    if not vehicle_data:
        return jsonify({"detail": "Not Found"}), 404

    return jsonify(vehicle_data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render uses port 10000
    app.run(host="0.0.0.0", port=port)
