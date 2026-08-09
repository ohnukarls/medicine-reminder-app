from typing import Any, Optional
import logging

from sqlalchemy.orm import Session

from app.models import Medication, User


class MedicationServiceError(Exception):
    pass


class UserNotFoundError(MedicationServiceError):
    pass


class InvalidMedicationNameError(MedicationServiceError):
    pass


class DuplicateMedicationError(MedicationServiceError):
    pass


class MedicationService:
    def __init__(self, db: Session, logger: Optional[logging.Logger] = None):
        self.db = db
        self.logger = logger or logging.getLogger(__name__)

    def _validate_name(self, name: str) -> str:
        if not isinstance(name, str):
            raise InvalidMedicationNameError('Medication name must be a string.')

        normalized_name = name.strip()
        if not normalized_name:
            raise InvalidMedicationNameError('Medication name must not be empty.')

        return normalized_name

    def _get_user(self, user_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFoundError(f'User with id {user_id} does not exist.')
        return user

    def _ensure_unique_name(self, user_id: int, name: str) -> None:
        existing = (
            self.db.query(Medication)
            .filter(Medication.user_id == user_id, Medication.name == name)
            .first()
        )
        if existing:
            raise DuplicateMedicationError(
                f'Medication "{name}" already exists for user {user_id}.'
            )

    def create_medication(self, user_id: int, name: str, **kwargs: Any) -> Medication:
        validated_name = self._validate_name(name)
        user = self._get_user(user_id)
        self._ensure_unique_name(user.id, validated_name)

        medication = Medication(user_id=user.id, name=validated_name, **kwargs)
        self.db.add(medication)
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise MedicationServiceError(f'Error occurred while creating medication: {e}')
        
        self.db.refresh(medication)

        self.logger.info('Created medication "%s" for user %s', validated_name, user.id)
        return medication
