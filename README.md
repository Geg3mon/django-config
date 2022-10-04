# DJANGO DEVELOPMENT CONFIG #

# Fast start to development Django project
This is template for Django projects with environment and Postgres DB.
Also I use django-debug-toolbar

### In terminal:
`cd` - go to main folder
`mkdir "name"` - create new folder with your "name"
`cd "name"` - change directory to created
`git clone https://github.com/Geg3mon/django-config` - clone repository
`python3 -m venv venv` - create virtual environment
`source venv/bin/activate` - activate your environment
`pip install -r requirements.txt` - install requirments

### Update .env file with your configuration
In basic .env file you can find next settings:
```bash
DEBUG = True
SECRET_KEY = ' '
DB_NAME = ' '
DB_USER = 'postgres'
DB_PASSWORD= '1234'
DB_HOST = 'localhost'
```
If you don't put secret key in '.env', you project crashed.
`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` - generate and print random SECRET_KEY in bash terminal.
You can add what ever you want in settings.
Some example: you need add some service api key

#### In .env:
```bash
SOME_SERVICE_API_KEY = 'my_string_api_key'
SOME_PORT = 1234
SOME_BOOLEAN = True
```
#### In settings.py
```python
import os
from dotenv import load_dotenv

load_dotenv() #default = '.env'

API_KEY = os.getenv('SOME_SERVICE_API_KEY')
API_PORT = os.getenv('SOME_PORT')
API_LOGS = os.getenv('SOME_BOOLEAN')
```
### .gitignore
Remember, when you push to git or deploy repository, add '.env' to .gitignore

### Migrate and run your project
`python manage.py makemigrations` - make migrations
`python manage.py migrate` - apply migrations
`python manage.py runserver` - run your Django server
