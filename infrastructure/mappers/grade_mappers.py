from domain.entities.grade import Grade

from application.schemas.grades_schema import CreateGradeDTO, UpdateGradeDTO

from infrastructure.db.models import GradeModel

def map_create_grade_dto_to_entity(grade_dto: CreateGradeDTO) -> Grade:
    """
    Maps a CreateGradeDTO to a Grade entity.
    
    Args:
        grade_dto (CreateGradeDTO): The DTO to map.
        
    Returns:
        Grade: The mapped Grade entity.
    """
    return Grade(
        id=None,
        student_id=grade_dto.student_id,
        subject_id=grade_dto.subject_id,
        value=grade_dto.value
    )

def map_grade_entity_to_model(grade: Grade) -> GradeModel:
    """
    Maps a Grade entity to a GradeModel.
    
    Args:
        grade (Grade): The entity to map.
        
    Returns:
        GradeModel: The mapped model.
    """
    return GradeModel(
        id=grade.id,
        student_id=grade.student_id,
        subject_id=grade.subject_id,
        value=grade.value
    )
