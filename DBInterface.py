
#Edit the user and password of psycopg2.connect appropriately

import psycopg2
	
class DB:
	"database interface"

	def __init__(self, database):
		self.database = database
		self.conn = psycopg2.connect(database=self.database, user="postgres", password="1234", host="127.0.0.1", port="5432")
		print "Database connection: successful"
		self.cur = self.conn.cursor()
		print "Database cursor: successful"
		
	def insertRow(self, data):
		query = "INSERT INTO GREENHOUSE (ID,TIME,DATE,MOISTURE_CONTENT,TEMPERATURE,WATERED) \
      		VALUES ('%i','%s', '%s', %i, %i, '%s')" % tuple(data)
		self.cur.execute(query)
		self.conn.commit()
		
	def selectLatestRow(self):
		self.cur.execute("SELECT id, time, date, moisture_content from GREENHOUSE ORDER BY id \
			DESC LIMIT 1")
		info = self.cur.fetchall()
		return info
	
	def selectMultiRows(self, rows):
		query = "SELECT id, time, date, moisture_content from GREENHOUSE ORDER BY id \
			DESC LIMIT %c" % (rows,)
		self.cur.execute(query) 
		return self.cur.fetchall()
	
	def closeDB(self):
		self.conn.commit()
		self.conn.close()
		
	
	def __del__(self):
		self.conn.commit()
		self.conn.close()
      	print "Database interface terminated."


