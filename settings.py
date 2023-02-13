""" File with settings and configs for the project """

from envparse import Env

env = Env()


# postgresql+asyncpg://login:password@0.0.0.0:5432/db_name
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
)  # connect string for the database
