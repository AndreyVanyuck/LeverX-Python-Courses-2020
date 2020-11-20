class Room:
    def __init__(self, id: int, name: str):
       self.id = id
       self.name = name
       
class Student:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class StudentRoom():
    def __init__(self, room: Room):
        self.room = room
        self.students = []
