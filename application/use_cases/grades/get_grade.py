from typing import List

from domain.repositories.grade_repository import GradeRepository
from domain.entities.grade import Grade
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

class GetGradeUseCase:
    def __init__(self, repository: GradeRepository):
        self.repository = repository

    def execute_by_id(self, grade_id: int) -> Grade:
        grade_obtained = self.repository.get_by_id(grade_id)

        if not grade_obtained:
            raise ResourceNotFoundException("Grade cannot be found by id")
        
        return grade_obtained
    
    def execute_all(self) -> List[Grade]:
        grades_obtained = self.repository.get_all()

        if not grades_obtained:
            raise ResourceNotFoundException("No grades found")
        
        return grades_obtained
    
    def execute_by_student_id(self, student_id: str) -> List[Grade]:
        grades_obtained = self.repository.get_by_student_id(student_id)
        # TO CONSIDER
        if not grades_obtained:
            raise ResourceNotFoundException(f"No grades found for student with ID '{student_id}'")
        
        return grades_obtained
    
    def execute_by_subject_id(self, subject_id: str) -> List[Grade]:
        grades_obtained = self.repository.get_by_subject_id(subject_id)
        # TO CONSIDER
        if not grades_obtained:
            raise ResourceNotFoundException(f"No grades found for subject with ID '{subject_id}'")
        
        return grades_obtained