# yabe
Django + React

### Backend setup

Make sure you are in the backend folder.

Install Dependencies:
```shell script
pip install -r requirements.txt
```

Migrate Database: 
```shell script
python manage.py migrate
```

Create Superuser for login and admin uses:
```shell script
python manage.py createsuperuser
```

Run Django Server:
```shell script
python manage.py runserver
```
You can access the api at ```127.0.0.1:8000```.

## Frontend setup

Make sure you are in the frontend folder.

Install Dependencies:
```shell script
npm install axios react-router-dom jwt-decode
```

Run scripts in dev mode:
```shell script
npm run dev
```

You can access the page at ```http://localhost:5173/```