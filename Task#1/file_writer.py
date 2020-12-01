import json
import xml.etree.ElementTree as ET
from custom_encoder import CustomEncoder


class Writer:
    def write(self, student_rooms: list):
        raise NotImplementedError


class JSONWriter(Writer):
    def write(self, student_rooms: list):
        with open("student_rooms.json", "w") as write_file:
            json.dump(student_rooms, write_file, cls=CustomEncoder)


class XMLWriter(Writer):
    def write(self, student_rooms: list):
        with open("student_rooms.xml", "w") as write_file:
            root = ET.Element("root")
            for student_room in student_rooms:
                item = ET.SubElement(root, "StudentRoom")

                room = ET.SubElement(item, "Room")
                item_id_room = ET.SubElement(room, "id")
                item_name_room = ET.SubElement(room, "name")
                item_id_room.text = str(student_room.room.id)
                item_name_room.text = student_room.room.name

                students = ET.SubElement(item, "Students")
                for val in student_room.students:
                    student = ET.SubElement(students, "Student")
                    item_id_student = ET.SubElement(student, "id")
                    item_name_student = ET.SubElement(student, "name")
                    item_id_student.text = str(val.id)
                    item_name_student.text = val.name

            mydata = ET.tostring(root, encoding="unicode")
            write_file.write(mydata)
