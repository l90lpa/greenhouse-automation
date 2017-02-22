#Greenhouse Automation, Project Geoff

This Python program designed to be run on a Raspberry Pi 3 to automate the watering of greenhouse plants when connected to the appropriate peripherals. The program also interacts with a PostgreSQL database to store the environmental data that is collected.

Schematics for the hardware side of the project will be added in the near future but the main component list is: MCP3008 ADC microchip, analog soil moisture sensor, 12v 400mA water valve solenoid, raspberry pi 1, 2 or 3.

## 1. Folder structure
- main.py: the main script which runs the program.
- ADConverter: functions required to convert analog signal to 10-bit digital signal
- MoistureContent: class to handle getting moisture sesnor readings, determining the average, and holding the result
- DBInterface: class to handle inserting a row of data to the database and retrieving the N most recent rows.


## 2. Setup
### 2.1 Install

- Ensure dependencies are installed:
	- Python (modules: libpq-dev, python-dev, psycopg2, spidev, RPi.GPIO)
	- PostgreSQL9.4 (packages: postgresql-server-dev9.4)
- Create a directory named greenhouse.
- Download the project from GitHub into greenhouse.

### 2.2 Configure

- In PostgreSQL:
	- Create a database named 'garden'
	- Create a table named 'greenhouse' with columns:
		- ID SERIAL PRIMARY KEY NOT NULL
		- TIME TIME NOT NULL
		- DATE DATE NOT NULL
		- MOISTURE_CONTENT REAL NOT NULL
		- TEMPERATURE REAL NOT NULL
		- WATERED BOOLEAN NOT NULL
- In DBInterface.py set the user, password, host and port appropriately. Default host and port should probably work but alter/remove the user and password if necessary.
- If desired alter the watering duration, sensor check interval and moisture content limit at the top of main.py

### 2.3 Run

- In the terminal open the greenhouse directory
- Run the command: python main.py
- To stop the program use the keyboard command: ctl+c

## 3. Dependencies

### 3.1 Setup database (PostgreSQL)

####_____General PostgreSQL commands_____

- open PostgreSQL PSQL interface: sudo -u postgres psql
- list current databases: \l
- select a database: \c database_name
- list current database tables: \d
- select a table: \d table_name
- create a database: CREATE DATABASE database_name;
- create a table:
	
	CREATE TABLE table_name(column1_name	data_type	default_value,
				column2_name	data_type	default_value,
				column3_name	data_type	default_value,
				.....
				columnN_name	data_type	default_value,
				PRIMARY KEY( one or more column_name )
				);
	
- close the PostgreSQL PSQL interface: \q	

####_____setup_____

- To install PostgreSQL, on raspbian OS enter the following commands in the command line:
	- sudo bash -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
	- wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
	- sudo apt-get update
	- sudo apt-get upgrade
	- sudo apt-get install pgadmin3 postgresql-server-dev-9.4
	- sudo apt-get install postgresql-9.4
- Open postgreSQL: sudo -u postgres psql
- Create 'garden' database.
- Create 'greenhouse' table.

### 3.2 Setup Python


####_____General Python commands_____

- If using python that is not a system default program then find the file path of this version in the system and use the full file path to run python commands e.g 'file_path/pythonX.Y' instead of 'python'
- To run the python interrupter enter: python OR file_path/pythonX.Y
- 'pip' is a python package manager for installing python modules.
- install modules, from the command line: pip install module_name
- to execute python scripts:
	- system default version: python script_name.py
	- installed version: file_path/python script_name.py
	
####_____setup_____

- To install python on raspbian OS, in the command line:
	- install python modules: sudo apt install libpq-dev python-dev
	- install psycopg2 module: pip install psycopg2
	- install spidev module: pip install spidev
	- install RPi.GPIO: pip install RPi.GPIO




