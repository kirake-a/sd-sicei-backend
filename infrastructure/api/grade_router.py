from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from infrastructure.db.database import get_db
from infrastructure.repositories.grade_repository_impl import GradeRepositoryImpl
from infrastructure.repositories.student_repository_impl import StudentRepositoryImpl
from infrastructure.repositories.subject_repository_impl import SubjectRepositoryImpl
from infrastructure.mappers.grade_mappers import map_create_grade_dto_to_entity

from application.schemas.grades_schema import CreateGradeDTO, GradeResponseDTO
from application.use_cases.grades.create_grade import CreateGradeUseCase

from domain.exceptions.not_enough_arguments_exception import NotEnoughArgumentsException
from domain.exceptions.cannot_create_exception import CannotCreateException
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from domain.utils.constants import UNEXPECTED_ERROR

router = APIRouter(prefix="/grades", tags=["Grades"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GradeResponseDTO)
def create_grade(
    grade_data: CreateGradeDTO,
    db: Session = Depends(get_db)
) -> GradeResponseDTO:
    """
    Create a new grade.
    """
    try:
        repo = GradeRepositoryImpl(db)
        student_repo = StudentRepositoryImpl(db)
        subject_repo = SubjectRepositoryImpl(db)
        use_case = CreateGradeUseCase(repo, student_repo, subject_repo)
        grade = use_case.execute(
            map_create_grade_dto_to_entity(grade_data)
        )
        return grade
    except NotEnoughArgumentsException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except CannotCreateException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )
