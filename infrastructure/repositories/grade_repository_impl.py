from sqlalchemy.orm import Session

from domain.entities.grade import Grade
from domain.repositories.grade_repository import GradeRepository

from infrastructure.db.models import GradeModel
from infrastructure.mappers.grade_mappers import map_grade_entity_to_model

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
    
    def get_by_id(self, grade_id: int) -> Grade:
        pass

    def get_all(self) -> list[Grade]:
        pass

    def update(self, grade: Grade) -> Grade:
        pass

    def delete(self, grade_id: int) -> None:
        pass

    def exists(self, grade_id: int) -> bool:
        pass