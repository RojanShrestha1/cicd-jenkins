from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create Flask app
app = Flask(__name__)

# Read DATABASE_URL from environment (provided by docker-compose)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://user:password@db:5432/app_db'  # fallback safety
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define a table/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Create tables if they do not exist
with app.app_context():
    db.create_all()

# Route
@app.route('/')
def hello():
    user_count = User.query.count()
    return f'Hello from Flask! There are {user_count} users in the database.'

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
