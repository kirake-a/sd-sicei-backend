from domain.repositories.student_repository import StudentRepository
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from domain.entities.student import Student

class GetStudentUseCase:
    def __init__(self, student_repository: StudentRepository):
        self.repository = student_repository

    def execute_by_id(self, student_id: str) -> Student:
        student_obtained = self.repository.get_by_id(student_id)

        if not student_obtained:
            raise ResourceNotFoundException("Student cannot be found by id")
        
        return student_obtained
    
    def execute_all(self) -> list[Student]:
        students_obtained = self.repository.get_all()

        if not students_obtained:
            raise ResourceNotFoundException("No students found")
        
        return students_obtained