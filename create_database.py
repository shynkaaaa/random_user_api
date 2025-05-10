from src.database import Base, engine
from src.models import User

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
