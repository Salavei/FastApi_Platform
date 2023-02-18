""" File with settings and configs for the project """

from envparse import Env

env = Env()


# postgresql+asyncpg://login:password@0.0.0.0:5432/db_name
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5433/postgres"
)  # connect string for the real database


TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5434/postgres_test"
)  # connect string for the test database