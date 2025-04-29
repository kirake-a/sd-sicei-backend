from typing import List

from domain.repositories.grade_repository import GradeRepository
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

from application.schemas.grades_schema import GradeResponseDTO

class GetGradeUseCase:
    def __init__(self, repository: GradeRepository):
        self.repository = repository

    def execute_by_id(self, grade_id: int) -> GradeResponseDTO:
        grade_obtained = self.repository.get_by_id(grade_id)

        if not grade_obtained:
            raise ResourceNotFoundException("Grade cannot be found by id")
        
        return GradeResponseDTO.model_validate(grade_obtained)
    
    def execute_all(self) -> List[GradeResponseDTO]:
        grades_obtained = self.repository.get_all()

        if not grades_obtained:
            raise ResourceNotFoundException("No grades found")
        
        return [GradeResponseDTO.model_validate(grade) for grade in grades_obtained]