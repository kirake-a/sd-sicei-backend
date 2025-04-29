from abc import ABC, abstractmethod
from domain.entities.grade import Grade
from typing import List

class GradeRepository(ABC):
    @abstractmethod
    def create(self, grade: Grade) -> Grade:
        """
        To create a new grade in the repository.
        """
        pass

    @abstractmethod
    def get_by_id(self, grade_id: int) -> Grade:
        """
        To get a grade by its ID from the repository.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Grade]:
        """
        To get all grades from the repository.
        """
        pass

    @abstractmethod
    def update(self, grade: Grade) -> Grade:
        """
        To update an existing grade in the repository.
        """
        pass

    @abstractmethod
    def delete(self, grade_id: int) -> bool:
        """
        To delete a grade by its ID from the repository.
        """
        pass

    @abstractmethod
    def exists(self, grade_id: int) -> bool:
        """
        To check if a grade exists in the repository.
        """
        pass