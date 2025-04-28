from domain.repositories.student_repository import StudentRepository
from domain.entities.student import Student
from domain.exceptions.cannot_update_resource_exception import CannotUpdateResourceException
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

from application.schemas.student_schema import StudentResponseDTO

class UpdateStudentUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, student_data: Student) -> StudentResponseDTO:
        if not self.repository.exists(student_data.id):
            raise ResourceNotFoundException("Student cannot be found by id")

        updated_student = self.repository.update(student_data)
        
        if not updated_student:
           raise CannotUpdateResourceException("Student cannot be updated")
        
        return StudentResponseDTO.model_validate(updated_student)