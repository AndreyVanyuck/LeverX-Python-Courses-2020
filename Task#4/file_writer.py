import json
import xml.etree.ElementTree as ET


class Writer():
    def write(self, data, file_name):
        raise NotImplementedError


class JSONWriter(Writer):
    def write(self, data, file_name):
        with open(file_name, "w") as write_file:
            json.dump(data, write_file)
    

class XMLWriter(Writer):
    def write(self, data, file_name):
        with open(file_name, "w") as write_file:
            root = ET.Element("root")
            for val in data:
                room = ET.SubElement(root, 'Room')
                item_name_room = ET.SubElement(room, 'name')
                item_name_room.text = val[0]
                item_val = ET.SubElement(room, "val")
                item_val.text = str(val[1])
            mydata = ET.tostring(root, encoding="unicode")
            write_file.write(mydata)
