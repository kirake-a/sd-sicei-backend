from abc import ABC, abstractmethod

from typing import List

from domain.entities.student import Student

class StudentRepository(ABC):
    @abstractmethod
    def create(self, student: Student) -> Student:
        """To create a new student record."""
        pass

    @abstractmethod
    def get_by_id(self, student_id: str) -> Student | None:
        """To retrieve a student record by its ID."""
        pass
    
    @abstractmethod
    def get_by_semester(self, students_semester: int) ->List[Student]:
        """To retrieve all students record by its semester."""
        pass

    @abstractmethod
    def get_all(self) -> List[Student]:
        """To retrieve all student records."""
        pass

    @abstractmethod
    def update(self, student: Student) -> Student:
        """To update an existing student record."""
        pass

    @abstractmethod
    def delete(self, student_id: str) -> bool:
        """To delete a student record by its ID."""
        pass

    @abstractmethod
    def exists(self, student_id: str) -> bool:
        """To check if a student record exists by its ID."""
        pass