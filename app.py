from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/db_monitoring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Désactive le suivi des modifications
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#db = SQLAlchemy()

# Modèle pour les End devices (pc, switch, imprimante, ...)
class EndDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    memory_usage = db.Column(db.Float)
    cpu_usage = db.Column(db.Float)
    disk_usage = db.Column(db.Float)

# Modèle pour les IoT devices
class IoTDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(50), unique=True, nullable=False)
    temperature = db.Column(db.Float)

# Modèle pour les villes
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

# Importe tes routes ici (par exemple, import routes)

if __name__ == '__main__':
    app.run(debug=True)
