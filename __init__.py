from main import User, passwords, app, db

with app.app_context():
    db.create_all()