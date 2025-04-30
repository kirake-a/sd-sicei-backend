from sqlalchemy.orm import Session

from typing import List

from domain.entities.subject import Subject
from domain.repositories.subject_repository import SubjectRepository

from infrastructure.db.models import SubjectModel
from infrastructure.mappers.subject_mappers import map_subject_entity_to_model, map_subject_model_to_entity

class SubjectRepositoryImpl(SubjectRepository):
    """Implementation of the SubjectRepository interface using SQLAlchemy."""
    
    def __init__(self, db: Session):
        self.db = db

    def create(self, subject: Subject) -> Subject:
        subject_model = map_subject_entity_to_model(subject)
        self.db.add(subject_model)
        self.db.commit()
        self.db.refresh(subject_model)

        return Subject(
            id=subject_model.id,
            name=subject_model.name,
            description=subject_model.description,
            credits=subject_model.credits,
            semester=subject_model.semester
        )
    
    def get_by_id(self, subject_id: str) -> Subject | None:
        subject_model = self.db.query(SubjectModel).filter(SubjectModel.id == subject_id).first()

        if not subject_model:
            return None
        
        return map_subject_model_to_entity(subject_model)

    def get_all(self) -> List[Subject]:
        subjects_model = self.db.query(SubjectModel).all()
        return [map_subject_model_to_entity(subject_model) for subject_model in subjects_model]

    def update(self, subject: Subject) -> Subject | None:
        subject_model = self.db.query(SubjectModel).filter(SubjectModel.id == subject.id).first()
            
        if not subject_model:
            return None
        
        if subject.name is not None:
            subject_model.name = subject.name
        if subject.description is not None:
            subject_model.description = subject.description
        if subject.credits is not None:
            subject_model.credits = subject.credits
        if subject.semester is not None:
            subject_model.semester = subject.semester

        self.db.commit()
        self.db.refresh(subject_model)

        return Subject(
            id=subject_model.id,
            name=subject_model.name,
            description=subject_model.description,
            credits=subject_model.credits,
            semester=subject_model.semester
        )

    def delete(self, subject_id: str) -> bool:
        subject_model = self.db.query(SubjectModel).filter(SubjectModel.id == subject_id).first()

        if not subject_model:
            return False
        
        self.db.delete(subject_model)
        self.db.commit()

        return True

    def exists(self, subject_id: str) -> bool:
        subject_obtained = self.db.query(SubjectModel).filter(SubjectModel.id == subject_id).first()
        return subject_obtained is not None