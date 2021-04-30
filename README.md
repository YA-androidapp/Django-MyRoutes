# Django-MyRoutes

---

```sh
python -m venv myenv
source myenv/bin/activate
python -m pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD="Passw0rd#" DJANGO_SUPERUSER_USERNAME="Admin" DJANGO_SUPERUSER_EMAIL="admin@example.net" python manage.py createsuperuser --noinput
python manage.py runserver
```

## DB Setting

`DATABASE_URL` in the `.env` file

| Engine       | Django Backend                              | URL                                        |
| ------------ | ------------------------------------------- | ------------------------------------------ |
| PostgreSQL   | `django.db.backends.postgresql_psycopg2`    | `postgres://USER:PASSWORD@HOST:PORT/NAME`  |
| PostGIS      | `django.contrib.gis.db.backends.postgis`    | `postgis://USER:PASSWORD@HOST:PORT/NAME`   |
| MSSQL        | `sql_server.pyodbc`                         | `mssql://USER:PASSWORD@HOST:PORT/NAME`     |
| MySQL        | `django.db.backends.mysql`                  | `mysql://USER:PASSWORD@HOST:PORT/NAME`     |
| MySQL (GIS)  | `django.contrib.gis.db.backends.mysql`      | `mysqlgis://USER:PASSWORD@HOST:PORT/NAME`  |
| SQLite       | `django.db.backends.sqlite3`                | `sqlite:///PATH`                           |
| SpatiaLite   | `django.contrib.gis.db.backends.spatialite` | `spatialite:///PATH`                       |
| Oracle       | `django.db.backends.oracle`                 | `oracle://USER:PASSWORD@HOST:PORT/NAME`    |
| Oracle (GIS) | `django.contrib.gis.db.backends.oracle`     | `oraclegis://USER:PASSWORD@HOST:PORT/NAME` |
| Redshift     | `django_redshift_backend`                   | `redshift://USER:PASSWORD@HOST:PORT/NAME`  |
