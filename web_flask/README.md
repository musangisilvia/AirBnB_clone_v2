# AirBnB clone - Web framework

[Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight WSGI web application framework. It depends on the [Jinja](https://palletsprojects.com/p/jinja) template engine and the [Werkzeug](https://palletsprojects.com/p/werkzeug) WSGI toolkit. Flask aims to keep the core simple but extensible.

In the AirBnB Clone project Flask is used to make the static HTML files dynamic by using objects stored in a file (file.json) or database (hbnb_dev_db)

## Starting a Flask Web Application

The web application will be listening on 0.0.0.0 port 5000. The storage variable defined in [models/__init__.py](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/models/__init__.py) is used to fetch data from the storage engine.
 - Import:
 	from models import storage

 - Usage:
 	* storage.all(...) - fetch the data from the storage engine
 	* storage.close() - closes the current SQLAlchemy Session.

## Setting up flask
Import Flask from flask module in python.

### Session removal
After each request, the current SQLAlchemy Session is removed by:
- the method ``` @app.teardown_appcontext ```, where ``` storage.close() ``` is called.

### Routes

These routes are defined to enable access to the different data from the storage engine ( database for this case )
To have some data in the database, import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql)

```
musangi@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
musangi@ubunutu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password:
musangi@ubuntu:~/AirBnB_v2$
```

1. /state_list - display a HTML page [7-states_list.html](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/web_flask/templates/7-states_list.html)

- Display format: 
	* H1: "States"
	* UL: List of all states.
		* LI: ``` <state.id>: <B><state.name></B>```, in ascending order. <br>

To run it: <br>

On terminal 1 <br>

```
musangi@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...

```

On Terminal 2 <br>

```
musangi@ubuntu:~/AirBnB_clone_v2$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
	<HEAD>
		<TITLE>HBNB</TITLE>
	</HEAD>
	<BODY>
		<H1>States</H1>
		<UL>
			<LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>
		</UL>
	</BODY>
</HTML>
```

2. /cities_by_states - display a HTML page [8-cities_by_states.html](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/web_flask/templates/8-cities_by_states.html)
- Display format:
	* H1: "States"
	* UL: List of all State objects in the database storage.
		* LI: ``` <state.id>: <B><state.name></B>```, in ascending order.
		* UL: list of all city objects linked to the State, in ascending order.
			*LI: ``` <city.id>: <B><city.name></B> ```. <br>

To run it: <br>

On terminal 1 <br>

```
musangi@ubuntu:~/AirBnB_clone_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```

On terminal 2 <br>

```
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
		<H1>States</H1>
		<UL>
			<LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
				<UL>
					<LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>
					<LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>
					<LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>
					<LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>
				</UL>
			</LI>
			<LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
				<UL>
					<LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>
					<LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>
					<LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>
				</UL>
			</LI>
			...
		</UL>
	</BODY>
</HTML>
```

3. /states and /states/<id> display a HTML page [9-states.html](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/web_flask/templates/9-states.html)
- Display format for /states route:
	* H1: "States"
	* UL: list of all State objects present in database storage
		* LI: <state.id>: <B><state.name></B> , sorted in ascending order.

- Display format for /states/<id> route:
	* H1: "States"
	* H3: "Cities"
	* UL: list of all City objects linked to the state, sorted in ascending order.
		* LI: <city.id>: <B><city.name></B>
	* If <id> is not found:
		* H1: "Not found!"

- Run similar to the first two routes, only chaning the python module name to web_flask.9-states.

4. /hbnb_filters: displays a HTML page [10-hbnb_filters.html](https://github.com/musangisilvia/AirBnB_clone_v2/blob/master/web_flask/templates/10-hbnb_filters.html)

- Display format is as shown in the pictures:
![image](https://user-images.githubusercontent.com/27401241/133841192-ef3e3642-8dc2-49ea-b321-33a14c6b119d.png)
![image](https://user-images.githubusercontent.com/27401241/133841211-a66bcac2-da3e-4b85-9272-39c5fbe111a0.png)
![image](https://user-images.githubusercontent.com/27401241/133841236-a8d8070a-3110-44c5-9221-3168ad31d853.png)
![image](https://user-images.githubusercontent.com/27401241/133841253-8f8cb256-74b7-42ee-a20e-32dc5472ad16.png)



