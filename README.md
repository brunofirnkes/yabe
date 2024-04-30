# yabe
Django + React

### Set up virtual environment
```shell script
python -m venv venv/
source venv/bin/activate
```

### Install Dependencies
```shell script
pip install -r requirements.txt
```

### Migrate Database
```shell script
python manage.py migrate
```

### Run Django Server
```shell script
python manage.py runserver
```
Now you can access the api at ```127.0.0.1:8000```.
