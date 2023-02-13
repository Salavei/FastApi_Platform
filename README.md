# FastApi_Platform

To add migrations, if the alembic.ini file is missing, run the command in the terminal:

```
alembic init migrations
```

This will create a directory with migrations and a configuration file for the Alembic.

- In alembic.ini you need to set the address of the database, in which we will add migrations.
- Then go to the directory with migrations and open env.py, there make changes in the block, where it says

```
from myapp import mymodel
```

- Then we enter: ``` alembic revision --autogenerate -m "comment" ```
- Migration will be created
- Next, we enter: ``` alembic upgrade heads ```