from app import app
from models import db, User, Guest, Episode, Appearance
from datetime import datetime

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()

    print("Creating tables...")
    db.create_all()

    print("Seeding user...")
    user = User(username='admin')
    user.set_password('password123')
    db.session.add(user)

    print("Seeding guests...")
    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Comedian')
    db.session.add_all([guest1, guest2])

    print("Seeding episodes...")
    episode1 = Episode(date=datetime(2025, 6, 1), number=101)
    episode2 = Episode(date=datetime(2025, 6, 8), number=102)
    db.session.add_all([episode1, episode2])

    db.session.commit()  # commit to generate IDs

    print("Seeding appearances...")
    appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=5, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=3, guest_id=guest1.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print(" Database seeded successfully!")
