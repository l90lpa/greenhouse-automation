##Setup database (PostgreSQL)

_____General PostgreSQL commands_____

- open PostgreSQL: pg_ctl -D /usr/local/var/postgres start
- start the PostgreSQL interface, PSQL: psql
- list current databases: \l
- select a database: \c database_name
- list current database tables: \d
- select a table: \d table_name
- create a database: CREATE DATABASE database_name
- create a table:
	
	CREATE TABLE table_name(
		column1_name	datatype	default_value,
		column2_name	datatype	default_value,
		column3_name	datatype	default_value,
		.....
		columnN_name	datatype	default_value,
		PRIMARY KEY( one or more column_names, comma separated )
		);
	
- close the PostgreSQL interface, PSQL, PostgreSQL will still be running: \q	
- close PostgreSQL: pg_ctl -D /usr/local/var/postgres stop

_____SETUP_____

- Install PostgreSQL, on raspbian:
	:sudo bash -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
	:wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
	:sudo apt-get update
	:sudo apt-get upgrade
	:sudo apt-get install pgadmin3 postgresql-server-dev-9.4
	:sudo apt-get install postgresql-9.4
- Open postgres: sudo -u postgres psql
- Create 'garden' database.
- Create 'greenhouse' table.

	CREATE TABLE GREENHOUSE (
	   ID INT PRIMARY KEY     		  NOT NULL,
       TIME         		  TIME	  NOT NULL,
       DATE					  DATE	  NOT NULL,
       MOISTURE_CONTENT       REAL    NOT NULL,
       TEMPERATURE            REAL,
       WATERED				  BOOLEAN);

- PostgreSQL server is generally run by default on; host=127.0.0.1, port=5432.
- PostgreSQL doesn't require user and password.


##Setup Python


_____General Python commands_____

- if using python that is not a system default app then find the file path of the
  installed copy in the system.
- run the python interrupter:
	- system default version: python
	- installed version: file_path/python
- installed version of python comes with 'pip' which is a package manager for installing python modules.
- install modules, from the command line: pip install module_name
- to execute python scripts:
	- system default version: python script_name.py
	- installed version: file_path/python script_name.py
	
_____SETUP_____

- install python
- install python modules: sudo apt install libpq-dev python-dev
- install psycopg2 module: pip install psycopg2
- install spidev module: pip install spidev
- install RPi.GPIO: pip install RPi.GPIO
- execute python script: python greenhouse.py (currently on my mac, /usr/local/Cellar/python/2.7.13/bin/python2.7)




