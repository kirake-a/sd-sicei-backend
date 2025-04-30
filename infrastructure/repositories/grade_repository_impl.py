from sqlalchemy.orm import Session

from typing import List

from domain.entities.grade import Grade
from domain.repositories.grade_repository import GradeRepository

from infrastructure.db.models import GradeModel
from infrastructure.mappers.grade_mappers import map_grade_entity_to_model, map_grade_model_to_entity

class GradeRepositoryImpl(GradeRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, grade: Grade) -> Grade:
        grade_model = map_grade_entity_to_model(grade)
        self.db.add(grade_model)
        self.db.commit()
        self.db.refresh(grade_model)

        return Grade(
            id=grade_model.id,
            student_id=grade_model.student_id,
            subject_id=grade_model.subject_id,
            value=grade_model.value
        )
    
    def get_by_id(self, grade_id: int) -> Grade | None:
        grade_model = self.db.query(GradeModel).filter(GradeModel.id == grade_id).first()

        if not grade_model:
            return None
        
        return map_grade_model_to_entity(grade_model)

    def get_all(self) -> List[Grade]:
        students_model = self.db.query(GradeModel).all()
        return [map_grade_model_to_entity(grade_model) for grade_model in students_model]

    def update(self, grade: Grade) -> Grade | None:
        grade_model = self.db.query(GradeModel).filter(GradeModel.id == grade.id).first()

        if not grade_model:
            return None
        
        if grade.value is not None:
            grade_model.value = grade.value

        self.db.commit()
        self.db.refresh(grade_model)

        return Grade(
            id=grade_model.id,
            student_id=grade_model.student_id,
            subject_id=grade_model.subject_id,
            value=grade_model.value
        )

    def delete(self, grade_id: int) -> bool:
        grade_model = self.db.query(GradeModel).filter(GradeModel.id == grade_id).first()

        if not grade_model:
            return False
        
        self.db.delete(grade_model)
        self.db.commit()

        return True

    def exists(self, grade_id: int) -> bool:
        student_model = self.db.query(GradeModel).filter(GradeModel.id == grade_id).first()
        return student_model is not None
    
    def get_by_student_id(self, student_id: str) -> List[Grade] | None:
        grade_models = self.db.query(GradeModel).filter(GradeModel.student_id == student_id).all()

        if not grade_models:
            return None
        
        return [map_grade_model_to_entity(grade_model) for grade_model in grade_models]
    
    def get_by_subject_id(self, subject_id) -> List[Grade] | None:
        grade_models = self.db.query(GradeModel).filter(GradeModel.subject_id == subject_id).all()

        if not grade_models:
            return None
        
        return [map_grade_model_to_entity(grade_model) for grade_model in grade_models]
