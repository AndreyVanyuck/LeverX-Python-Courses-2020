import argparse
from file_reader import FileReader
from file_writer import FileWriter
from models import StudentRoom, Student, Room


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--students_path",required=True, type=str, help="Path to students.json")
    parser.add_argument("-r", "--rooms_path",required=True, type=str, help="Path to rooms.json")
    parser.add_argument("-f", "--format", choices=["json", "xml"], type=str, help="Format", default="json")
    return parser.parse_args()


def main():
    args = parse_args()
    
    try:
        rooms = FileReader(args.rooms_path).read()
        students = FileReader(args.students_path).read()
    except FileNotFoundError as e:
        print(e)
        return

    studentRooms = []
    for room in rooms:
        studentRooms.append(StudentRoom(Room(room['id'], room['name'])))
    for student in students:
        studentRooms[student['room']].students.append(Student(student['id'], student['name']))
    
    if args.format == "json":
        FileWriter.write_as_json(studentRooms)
    else:
        FileWriter.write_as_xml(studentRooms)

if __name__ == "__main__":
    main()
