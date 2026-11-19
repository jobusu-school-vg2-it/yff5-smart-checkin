import sqlite3
from pathlib import Path
from database_types import Visit


DB = Path(__file__).with_name('visits.db')


def connect():
	connection = sqlite3.connect(DB)
	connection.row_factory = sqlite3.Row
	return connection


def initialize_db():
	with connect() as connection:
		connection.execute(
			'''
			CREATE TABLE IF NOT EXISTS visits (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				purpose TEXT NOT NULL,
				in_time TEXT NOT NULL DEFAULT (datetime('now','localtime')),
				out_time TEXT
			)
   			'''
		)


def save_visit(name: str, purpose: str) -> bool:
	connection = connect()
	
	try:
		cursor = connection.execute(
			'''
			INSERT INTO visits (name, purpose)
			VALUES (?, ?)
   			''',
			(name, purpose)
		)
  
		connection.commit()
		return cursor.rowcount == 1
	
	except sqlite3.Error as error:
		connection.rollback()
		raise error
	
	finally:
		connection.close()


def get_visits() -> list[Visit]:
	connection = connect()
	
	try:
		return connection.execute(
			'''
			SELECT * FROM visits
			ORDER BY in_time DESC, id DESC
        	'''
		).fetchall()
	
	except sqlite3.Error as error:
		raise error
	
	finally:
		connection.close()


def check_out(visit_id: int) -> bool:
	connection = connect()
	
	try:
		cursor = connection.execute(
			'''
			UPDATE visits
			SET out_time = datetime('now','localtime')
			WHERE id = ?
   			AND out_time IS NULL
			''',
			(str(visit_id))
		)
  
		connection.commit()
		return cursor.rowcount == 1
	
	except sqlite3.Error as error:
		connection.rollback()
		raise error
	
	finally:
		connection.close()