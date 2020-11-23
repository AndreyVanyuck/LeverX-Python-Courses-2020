
#import json
from FileReader import FileReader
from FileWriter import FileWriter 
from Queries import *

import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-s", "--students_path",required=True, type=str, help="Path to students.json")
parser.add_argument("-r", "--rooms_path",required=True, type=str, help="Path to rooms.json")
parser.add_argument("-f", "--format", choices=["json", "xml"], type=str, help="Format", default="json")
args = parser.parse_args()


def main():
    rooms = FileReader(args.rooms_path).read()
    students = FileReader(args.students_path).read()

    if args.format == "json":
        FileWriter.write_as_json(studentRooms)
    else:
        FileWriter.write_as_xml(studentRooms)

if __name__ == "__main__":
    main()

connection = create_connection("localhost", "root", "user", "python_student")


number_of_students_in_room = execute_read_query(connection, select_number_of_students_in_room)
FileWriter().write_as_json(number_of_students_in_room, "query_1.json")

top_five_small_avg_age_rooms = execute_read_query(connection, select_top_five_small_avg_age_rooms)
FileWriter().write_as_json(top_five_small_avg_age_rooms, "query_2.json")

top_five_big_diff_age_rooms = execute_read_query(connection, select_top_five_big_diff_age_rooms)
FileWriter().write_as_json(top_five_big_diff_age_rooms, "query_3.json")

different_sexes_rooms = execute_read_query(connection, select_different_sexes_rooms)
FileWriter().write_as_json(different_sexes_rooms, "query_4.json")




number_of_students_in_room = execute_read_query(connection, select_number_of_students_in_room)
FileWriter().write_as_xml(number_of_students_in_room, "query_1.xml", is_two_argument=True)

top_five_small_avg_age_rooms = execute_read_query(connection, select_top_five_small_avg_age_rooms)
FileWriter().write_as_xml(top_five_small_avg_age_rooms, "query_2.xml")

top_five_big_diff_age_rooms = execute_read_query(connection, select_top_five_big_diff_age_rooms)
FileWriter().write_as_xml(top_five_big_diff_age_rooms, "query_3.xml")

different_sexes_rooms = execute_read_query(connection, select_different_sexes_rooms)
FileWriter().write_as_xml(different_sexes_rooms, "query_4.xml")

#print(number_of_students_in_room)

