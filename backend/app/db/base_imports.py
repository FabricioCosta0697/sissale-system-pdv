# Importa todos os models para que o Alembic detecte as tabelas no autogenerate
from app.db.base import Base  # noqa: F401
from app.models import Tenant, User  # noqa: F401
