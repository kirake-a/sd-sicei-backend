from domain.repositories.grade_repository import GradeRepository
from domain.entities.grade import Grade
from domain.exceptions.cannot_update_resource_exception import CannotUpdateResourceException
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

from application.schemas.grades_schema import GradeResponseDTO

class UpdateGradeUseCase:
    def __init__(self, repository: GradeRepository):
        self.repository = repository

    def execute(self, grade_data: Grade) -> GradeResponseDTO:
        if not self.repository.exists(grade_data.id):
            raise ResourceNotFoundException("Grade cannot be found by id")

        updated_grade = self.repository.update(grade_data)
        
        if not updated_grade:
           raise CannotUpdateResourceException("Grade cannot be updated")
        
        return GradeResponseDTO.model_validate(updated_grade)
