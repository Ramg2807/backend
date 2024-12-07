from flask import Flask, request, jsonify
from models import db, DeliveryRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Route to create a delivery request
@app.route('/create_request', methods=['POST'])
def create_request():
    data = request.json
    new_request = DeliveryRequest(pickup=data['pickup'], dropoff=data['dropoff'])
    db.session.add(new_request)
    db.session.commit()
    return jsonify({"message": "Request created", "id": new_request.id}), 201

# Route to get all delivery requests
@app.route('/get_requests', methods=['GET'])
def get_requests():
    requests = DeliveryRequest.query.all()
    return jsonify([{
        "id": r.id, "pickup": r.pickup, "dropoff": r.dropoff, "status": r.status
    } for r in requests])

if __name__ == '__main__':
    app.run(debug=True)
