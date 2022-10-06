# Test task for "Just Host"

## Run project:
```shell
docker-compose up --build -d
docker-compose exec web bash
python manage.py migrate
```
Server will be available at http://0.0.0.0:8000

Documentation will be available at http://0.0.0.0:8000/api/doc
