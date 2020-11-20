import json
import xml.etree.ElementTree as ET
from CustomEncoder import CustomEncoder


class FileWriter:
    @staticmethod
    def write_as_json(studentRooms: list):
        with open("studentRooms.json", "w") as write_file:
            json.dump(studentRooms, write_file, cls=CustomEncoder)
    
    @staticmethod
    def write_as_xml(studentRooms: list):
        with open("studentRooms.xml", "w") as write_file:
            root = ET.Element("root")
            for studentRoom in studentRooms:
                item = ET.SubElement(root, 'StudentRoom')

                room = ET.SubElement(item, 'Room')
                item_id_room = ET.SubElement(room, 'id')
                item_name_room = ET.SubElement(room, 'name')
                item_id_room.text = str(studentRoom.room.id)
                item_name_room.text = studentRoom.room.name
                
                students = ET.SubElement(item, 'Students')
                for val in studentRoom.students:
                    student = ET.SubElement(students, 'Student')
                    item_id_student = ET.SubElement(student, 'id')
                    item_name_student = ET.SubElement(student, 'name')
                    item_id_student.text = str(val.id)
                    item_name_student.text = val.name

            mydata = ET.tostring(root, encoding="unicode")
            write_file.write(mydata)