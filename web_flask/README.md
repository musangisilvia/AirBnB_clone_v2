# AirBnB clone - Web framework

[Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight WSGI web application framework. It depends on the [Jinja](https://palletsprojects.com/p/jinja) template engine and the [Werkzeug](https://palletsprojects.com/p/werkzeug) WSGI toolkit. Flask aims to keep the core simple but extensible.

In the AirBnB Clone project Flask is used to make the static HTML files dynamic by using objects stored in a file (file.json) or database (hbnb_dev_db)

## Starting a Flask Web Application

The web application is listening on 0.0.0.0 port 5000. The storage variable defined in [models/__init__.py](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/models/__init__.py) is used to fetch data from the storage engine.
 ```
 - Import:
 	from models import storage

 - Usage:
 	storage.all(...)

 - Extra:
 	storage.closs() - closes the current SQLAlchemy Session.
	@app.teardown_appcontext - closes the application in case of an error. *
 ```


## 
