from sqlalchemy import text
from app.db.session import engine

with engine.connect() as conn:
    rows = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")).fetchall()
    print("Tabelas:", [r[0] for r in rows])
