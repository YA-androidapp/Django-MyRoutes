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
