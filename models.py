from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the DeliveryRequest model
class DeliveryRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pickup = db.Column(db.String(100), nullable=False)
    dropoff = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="pending")
