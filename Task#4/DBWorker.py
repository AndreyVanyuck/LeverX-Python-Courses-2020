import mysql.connector
from mysql.connector import Error
from FileReader import FileReader
from Queries import insert_into_room, insert_into_student


class DBWorker():
    pass
def create_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def insert_into(connection, file_name_rooms, file_name_students):
  json_rooms = FileReader(file_name_rooms).read()
  json_students = FileReader(file_name_students).read()
  val_students = [(student['birthday'], student['id'], student['name'], student['room'], student['sex']) for student in json_students]
  val_rooms = [(room['id'], room['name']) for room in json_rooms]
  cursor = connection.cursor()
  cursor.executemany(insert_into_room, val_rooms)
  cursor.executemany(insert_into_student, val_students)
  connection.commit()    
