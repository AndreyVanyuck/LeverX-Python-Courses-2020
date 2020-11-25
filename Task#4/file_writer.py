import json
import xml.etree.ElementTree as ET


class FileWriter:
    @staticmethod
    def write_as_json(data, file_name):
        with open(file_name, "w") as write_file:
            json.dump(data, write_file)
    
    @staticmethod
    def write_as_xml(data, file_name, is_two_argument=False):
        with open(file_name, "w") as write_file:
            root = ET.Element("root")
            for val in data:
                room = ET.SubElement(root, 'Room')
                item_name_room = ET.SubElement(room, 'name')
                item_name_room.text = val[0]
                
                if is_two_argument:
                    item_count = ET.SubElement(room, "count_students")
                    item_count.text = str(val[1])
            mydata = ET.tostring(root, encoding="unicode")
            write_file.write(mydata)