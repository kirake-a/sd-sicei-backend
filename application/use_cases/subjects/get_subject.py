from domain.repositories.subject_repository import SubjectRepository
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException

from application.schemas.subject_schema import SubjectResponseDTO

class GetSubjectUseCase:
    def __init__(self, repository: SubjectRepository):
        self.respository = repository

    def execute_by_id(self, subject_id: str) -> SubjectResponseDTO:
        subject_obtained = self.respository.get_by_id(subject_id)

        if not subject_obtained:
            raise ResourceNotFoundException("Subject cannot be found by id")
        
        return SubjectResponseDTO.model_validate(subject_obtained)
    
    def execute_all(self) -> list[SubjectResponseDTO]:
        subjects_obtained = self.respository.get_all()

        if not subjects_obtained:
            raise ResourceNotFoundException("No subjects found")
        
        return [SubjectResponseDTO.model_validate(subject) for subject in subjects_obtained]
