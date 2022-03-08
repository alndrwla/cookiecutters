# cookiecutters
## Start project in django 3.2.* with sqlite3, environments, custom user and test.

### First Move in django_sqlite3 folder and create an environment in python
```bash
python3 -m venv venv
```
### Second install requirements depends local, test or production

```python
pip install -r requirements/local.txt
```

### Third Create local file with SECRET_KEY in .envs and Exec makemigrations and migrate

```python
python manage.py makemigrations
python manage.py migrate
```

### Fourth Create superuser and complete data: user, email and password

```python
python manage.py createsuperuser
```

### Fifth Exec test "Optional"

```python
python manage.py test
```

### Finally Exec runserver

```python
python manage.py runserver
```
