import json
import os


class FileReader:
    def __init__(self, file_name: str):
        if not (os.path.exists(file_name)):
            raise FileNotFoundError('file not found')
        self.file_name = file_name
      
    
    def read(self):
        with open(self.file_name, "r") as read_file:
            return json.load(read_file)  
