from flask import Flask, request, jsonify
from copart_scraper_script import fetch_vehicle_info
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allow all origins to access the API

@app.route('/fetch_vehicle', methods=['GET'])
def fetch_vehicle():
    lot_number = request.args.get('lot')
    if not lot_number:
        return jsonify({"error": "Lot number is required"}), 400

    vehicle_data = fetch_vehicle_info(lot_number)
    if not vehicle_data:
        return jsonify({"detail": "Not Found"}), 404  # If vehicle data is empty, return 404

    return jsonify(vehicle_data)

if __name__ == '__main__':
    app.run(debug=True)
