import mysql.connector
from mysql.connector import Error
from file_reader import FileReader
from queries import insert_into_room, insert_into_student


class DBWorker():
    def create_connection(self, host_name, user_name, user_password, database):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database
            )
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")


    def create_index(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")


    def insert_into(self, connection, file_name_rooms, file_name_students):
        try:
            json_rooms = FileReader(file_name_rooms).read()
            json_students = FileReader(file_name_students).read()
        except FileNotFoundError as e:
            print(e)

        val_students = [(student['birthday'], student['id'], student['name'], student['room'], student['sex']) for student in json_students]
        val_rooms = [(room['id'], room['name']) for room in json_rooms]
        cursor = connection.cursor()
        cursor.executemany(insert_into_room, val_rooms)
        cursor.executemany(insert_into_student, val_students)
        connection.commit()    
