from domain.repositories.grade_repository import GradeRepository
from domain.entities.grade import Grade
from domain.exceptions.cannot_update_resource_exception import CannotUpdateResourceException
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

class UpdateGradeUseCase:
    def __init__(self, repository: GradeRepository):
        self.repository = repository

    def execute(self, grade_data: Grade) -> Grade:
        if not self.repository.exists(grade_data.id):
            raise ResourceNotFoundException("Grade cannot be found by id")

        updated_grade = self.repository.update(grade_data)
        
        if not updated_grade:
           raise CannotUpdateResourceException("Grade cannot be updated")
        
        return updated_grade
