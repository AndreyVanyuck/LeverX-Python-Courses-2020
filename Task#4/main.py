import argparse
from FileReader import FileReader
from FileWriter import FileWriter 
from DBWorker import DBWorker
from Queries import (select_different_sexes_rooms, select_number_of_students_in_room,
                    select_top_five_big_diff_age_rooms, select_top_five_small_avg_age_rooms)


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--students_path",required=True, type=str, help="Path to students.json")
parser.add_argument("-r", "--rooms_path",required=True, type=str, help="Path to rooms.json")
parser.add_argument("-f", "--format", choices=["json", "xml"], type=str, help="Format", default="json")
args = parser.parse_args()


def main():
    dBWorker = DBWorker()
    connection = dBWorker.create_connection("localhost", "root", "user", "python_student")
    dBWorker.insert_into(connection, args.rooms_path, args.students_path) 

    number_of_students_in_room = dBWorker.execute_read_query(connection, select_number_of_students_in_room)
    top_five_small_avg_age_rooms = dBWorker.execute_read_query(connection, select_top_five_small_avg_age_rooms)
    top_five_big_diff_age_rooms = dBWorker.execute_read_query(connection, select_top_five_big_diff_age_rooms)
    different_sexes_rooms = dBWorker.execute_read_query(connection, select_different_sexes_rooms)
    
    if args.format == "json":
        FileWriter().write_as_json(number_of_students_in_room, "query_1.json")
        FileWriter().write_as_json(top_five_small_avg_age_rooms, "query_2.json")
        FileWriter().write_as_json(top_five_big_diff_age_rooms, "query_3.json")
        FileWriter().write_as_json(different_sexes_rooms, "query_4.json")
    else:
        FileWriter().write_as_xml(number_of_students_in_room, "query_1.xml", is_two_argument=True)
        FileWriter().write_as_xml(top_five_small_avg_age_rooms, "query_2.xml")
        FileWriter().write_as_xml(top_five_big_diff_age_rooms, "query_3.xml")
        FileWriter().write_as_xml(different_sexes_rooms, "query_4.xml")

if __name__ == "__main__":
    main()