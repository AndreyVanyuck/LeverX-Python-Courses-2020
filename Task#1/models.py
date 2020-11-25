from dataclasses import dataclass


@dataclass
class Room:
    id : int
    name : str


@dataclass   
class Student:
    id : int
    name: str


@dataclass
class StudentRoom():
    room : Room
    students : list