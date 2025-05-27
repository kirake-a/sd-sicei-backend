from typing import Tuple, List

from domain.entities.grade import GradeToShowStudent, GradeToShowSubject
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from domain.repositories.grade_repository import GradeRepository
from domain.repositories.student_repository import StudentRepository

class GetReportUseCase:
    def __init__(
        self,
        grade_repository: GradeRepository,
        student_repository: StudentRepository
    ):
        self.grade_repository = grade_repository
        self.student_repository = student_repository

    def execute_by_student_id(self, student_id: str) -> Tuple[List[GradeToShowStudent], float]:
        grades_obtained = self.grade_repository.get_student_grades_to_show(student_id)
        student_average = self.student_repository.get_average_by_student_id(student_id)

        if not grades_obtained or student_average is None:
            raise ResourceNotFoundException(f"Cannot fount data for student with ID '{student_id}'")
        
        return grades_obtained, student_average
    
    def execute_by_subject_id(self, subject_id: str) -> Tuple[List[GradeToShowSubject], float]:
        grades_obtained = self.grade_repository.get_subject_grades_to_show(subject_id)

        if not grades_obtained:
            raise ResourceNotFoundException(f"Cannot found data for subject with ID '{subject_id}'")
        
        value_counter: int = 0
        average: float = 0.0
        for grade in grades_obtained:
            value_counter += grade.value

        average = value_counter / len(grades_obtained)

        return grades_obtained, average
        
