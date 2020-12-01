from dataclasses import dataclass, field


@dataclass
class Room:
    id: int
    name: str


@dataclass
class Student:
    id: int
    name: str


@dataclass
class StudentRoom:
    room: Room
    students: list = field(default_factory=list)
