Redzone
---

Demo app for KnoxPy Talk on 10-06-16


### Setup

- Run `python manage.py db init`, `python manage.py db migrate`, and `python manage.py db migrate` first before anything else.
- To start the application, run `honcho start`, but make sure to do `pip install -r requirements.txt` first to install all dependencies.
- You may need to set the Redzone settings environment variable. If so, simply run `export REDZONE_SETTINGS="redzone.settings.ProdConfig"` in your shell.
