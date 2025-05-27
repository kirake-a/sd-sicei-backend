from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Query
)

from typing import List

from sqlalchemy.orm import Session

from infrastructure.db.database import get_db
from infrastructure.schemas.report_schema import StudentWithAverageResponseDTO
from infrastructure.repositories.subject_repository_impl import SubjectRepositoryImpl
from infrastructure.repositories.student_repository_impl import StudentRepositoryImpl
from infrastructure.repositories.grade_repository_impl import GradeRepositoryImpl
from infrastructure.schemas.report_schema import ReportStudentsResponseDTO, ReportSubjectsResponseDTO

from application.use_cases.reports.get_report import GetReportUseCase

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/students/{student_id}/grades", status_code=status.HTTP_200_OK)
async def get_student_subjects_grades(
    student_id: str,
    db: Session = Depends(get_db)
):
    """
    Get grades with average for a specific student by their ID.
    """
    try:
        student_repo = StudentRepositoryImpl(db)
        grade_repo = GradeRepositoryImpl(db)
        use_case = GetReportUseCase(
            student_repository=student_repo,
            grade_repository=grade_repo
        )
        grades, average = use_case.execute_by_student_id(student_id)
        return ReportStudentsResponseDTO(
            subjects=grades,
            average=average
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error initializing use case: {str(e)}"
        )

@router.get("/subjects/{subject_id}/grades", status_code=status.HTTP_200_OK)
async def get_subject_students_grades(
    subject_id: str,
    db: Session = Depends(get_db)
):
    """
    Get students with grades for a specific subject by its ID.
    """
    try:
        student_repo = StudentRepositoryImpl(db)
        grade_repo = GradeRepositoryImpl(db)
        use_case = GetReportUseCase(
            student_repository=student_repo,
            grade_repository=grade_repo
        )
        students, average = use_case.execute_by_subject_id(subject_id)
        return ReportSubjectsResponseDTO(
            students=students,
            average=average
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error initializing use case: {str(e)}"
        )