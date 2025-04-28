import uuid

from domain.entities.subject import Subject
from domain.repositories.subject_repository import SubjectRepository
from domain.exceptions.cannot_create_exception import CannotCreateException
from domain.exceptions.resource_already_exists_exception import ResourceAlreadyExistsException

from application.schemas.subject_schema import SubjectResponseDTO

class CreateSubjectUseCase:
    def __init__(self, repository: SubjectRepository):
        self.repository = repository

    def execute(self, subject_data: Subject) -> SubjectResponseDTO:
        subject_data.id = self.generate_subject_id()

        created_subject = self.repository.create(subject_data)

        if not created_subject:
            raise CannotCreateException("Cannot create subject successfully")
        
        return SubjectResponseDTO.model_validate(created_subject)
        
    def generate_subject_id(self) -> str:
        new_id = str(uuid.uuid4())

        if self.repository.exists(new_id):
            return self.generate_subject_id()
        
        return new_id