from app import app
from models import db, Article, User

db.init_app(app)

fake = Faker()

with app.app_context():
