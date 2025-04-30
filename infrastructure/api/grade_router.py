from fastapi import APIRouter, Depends, HTTPException, status

from typing import List

from sqlalchemy.orm import Session

from infrastructure.db.database import get_db
from infrastructure.repositories.grade_repository_impl import GradeRepositoryImpl
from infrastructure.repositories.student_repository_impl import StudentRepositoryImpl
from infrastructure.repositories.subject_repository_impl import SubjectRepositoryImpl
from infrastructure.mappers.grade_mappers import map_create_grade_dto_to_entity, map_update_grade_dto_to_entity

from application.schemas.grades_schema import CreateGradeDTO, UpdateGradeDTO, GradeResponseDTO
from application.use_cases.grades.create_grade import CreateGradeUseCase
from application.use_cases.grades.get_grade import GetGradeUseCase
from application.use_cases.grades.delete_grade import DeleteGradeUseCase
from application.use_cases.grades.update_grade import UpdateGradeUseCase

from domain.exceptions.not_enough_arguments_exception import NotEnoughArgumentsException
from domain.exceptions.cannot_create_exception import CannotCreateException
from domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from domain.exceptions.cannot_update_resource_exception import CannotUpdateResourceException
from domain.exceptions.cannot_delete_resource_exception import CannotDeleteResourceException
from domain.utils.constants import UNEXPECTED_ERROR
from domain.utils.exception_detail_wrapper import exception_detail_wrapper

router = APIRouter(prefix="/grades", tags=["Grades"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GradeResponseDTO)
async def create_grade(
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
        return GradeResponseDTO.model_validate(grade)
    except NotEnoughArgumentsException as e:
        raise exception_detail_wrapper(
            status_code=status.HTTP_400_BAD_REQUEST,
            exception=e,
            error_type="NotEnoughArgumentsException"
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

@router.get("/{grade_id}", status_code=status.HTTP_200_OK, response_model=GradeResponseDTO)
async def get_grade_by_id(
    grade_id: int,
    db: Session = Depends(get_db)
) -> GradeResponseDTO:
    """
    Get a grade by Id
    """
    try:
        repo = GradeRepositoryImpl(db)
        use_case = GetGradeUseCase(repo)
        grade = use_case.execute_by_id(grade_id)
        return GradeResponseDTO.model_validate(grade)
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )
    
@router.get("/student/{student_id}", status_code=status.HTTP_200_OK, response_model=List[GradeResponseDTO])
async def get_grade_by_student_id(
    student_id: str,
    db: Session = Depends(get_db)
) -> List[GradeResponseDTO]:
    try:
        repo = GradeRepositoryImpl(db)
        use_case = GetGradeUseCase(repo)
        grades = use_case.execute_by_student_id(student_id)
        return [GradeResponseDTO.model_validate(grade) for grade in grades]
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:  
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )
    
@router.get("/subject/{subject_id}", status_code=status.HTTP_200_OK, response_model=List[GradeResponseDTO])
async def get_grade_by_subject_id(
    subject_id: str,
    db: Session = Depends(get_db)
) -> List[GradeResponseDTO]:
    try:
        repo = GradeRepositoryImpl(db)
        use_case = GetGradeUseCase(repo)
        grades = use_case.execute_by_subject_id(subject_id)
        return [GradeResponseDTO.model_validate(grade) for grade in grades]
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )

    
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GradeResponseDTO])
async def get_all_grade(
    db: Session = Depends(get_db)
) -> List[GradeResponseDTO]:
    try:
        repo = GradeRepositoryImpl(db)
        use_case = GetGradeUseCase(repo)
        grades = use_case.execute_all()
        return [GradeResponseDTO.model_validate(grade) for grade in grades]
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )

@router.put("/{grade_id}", status_code=status.HTTP_200_OK, response_model=GradeResponseDTO)
async def update_grade(
    grade_id: int,
    grade_data: UpdateGradeDTO,
    db: Session = Depends(get_db)
) -> GradeResponseDTO:
    """
    Update a grade by Id
    """
    try:
        repo = GradeRepositoryImpl(db)
        use_case = UpdateGradeUseCase(repo)
        grade = use_case.execute(
            map_update_grade_dto_to_entity(grade_id, grade_data)
        )
        return GradeResponseDTO.model_validate(grade)
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except CannotUpdateResourceException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )
    
@router.delete("/{grade_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grade(
    grade_id: int,
    db: Session = Depends(get_db)
) -> None:
    """
    Delete a grade by Id
    """
    try:
        repo = GradeRepositoryImpl(db)
        use_case = DeleteGradeUseCase(repo)
        use_case.execute(grade_id)
    except ResourceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except CannotDeleteResourceException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=UNEXPECTED_ERROR + str(e)
        )
