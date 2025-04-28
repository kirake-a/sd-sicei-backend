from dataclasses import dataclass

@dataclass
class Grade:
    id: int
    student_id: str
    subject_id: str
    value: float