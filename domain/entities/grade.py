from dataclasses import dataclass

@dataclass
class Grade:
    id: int | None
    student_id: str
    subject_id: str
    value: float