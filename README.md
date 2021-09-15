## Install instruction

Create .env file

`SECRET_KEY={}`

Apply migrations:

`python manage.py migrate`

To start a Redis server on port 6379, run the following command:

`docker run -p 6379:6379 -d redis:5`

Run local server:

`python manage.py runserver`
