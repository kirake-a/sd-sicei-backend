from dataclasses import dataclass

@dataclass
class Student:
    id: str | None
    name: str
    lastname: str
    email: str
    semester: int
    average: float = 0.0