import argparse
from file_reader import FileReader
from file_writer import XMLWriter, JSONWriter 
from dB_worker import DBWorker
from queries import (select_different_sexes_rooms, select_number_of_students_in_room,
                    select_top_five_big_diff_age_rooms, select_top_five_small_avg_age_rooms,
                    create_index_room, create_index_birthday, create_index_sex)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--students_path",required=True, type=str, help="Path to students.json")
    parser.add_argument("-r", "--rooms_path",required=True, type=str, help="Path to rooms.json")
    parser.add_argument("-f", "--format", choices=["json", "xml"], type=str, help="Format", default="json")
    return parser.parse_args()


def main():
    HOST_NAME = "localhost"
    USER_NAME = "root"
    USER_PASSWORD = "user"
    DATABASE = "python_student"

    args = parse_args()
    
    dBWorker = DBWorker()

    connection = dBWorker.create_connection(HOST_NAME, USER_NAME, USER_PASSWORD, DATABASE)
    
    dBWorker.insert_into(connection, args.rooms_path, args.students_path) 
    
    dBWorker.create_index(connection, create_index_room)
    dBWorker.create_index(connection, create_index_sex)
    dBWorker.create_index(connection, create_index_birthday)

    number_of_students_in_room = dBWorker.execute_read_query(connection, select_number_of_students_in_room)
    top_five_small_avg_age_rooms = dBWorker.execute_read_query(connection, select_top_five_small_avg_age_rooms)
    top_five_big_diff_age_rooms = dBWorker.execute_read_query(connection, select_top_five_big_diff_age_rooms)
    different_sexes_rooms = dBWorker.execute_read_query(connection, select_different_sexes_rooms)
    
    formats = {'json': JSONWriter(), 'xml': XMLWriter()}
    formats[args.format].write(number_of_students_in_room, f"query_1.{args.format}")
    formats[args.format].write(top_five_small_avg_age_rooms, f"query_2.{args.format}")
    formats[args.format].write(top_five_big_diff_age_rooms, f"query_3.{args.format}")
    formats[args.format].write(different_sexes_rooms, f"query_4.{args.format}")

if __name__ == "__main__":
    main()