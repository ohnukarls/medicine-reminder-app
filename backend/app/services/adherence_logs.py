from datetime import datetime
import logging

from sqlalchemy.orm import Session

from app.models import Medication, User, AdherenceLog

class AdherenceLogServiceError(Exception):
    pass

class UserNotFoundError(AdherenceLogServiceError):
    pass

class InvalidAdherenceLogError(AdherenceLogServiceError):
    pass

class AdherenceLogService:
    def __init__(self, db: Session, logger: Optional[logging.Logger] = None):
        self.db = db
        self.logger = logger or logging.getLogger(__name__)

    def _get_user(self, user_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFoundError(f'User with id {user_id} does not exist.')
        return user
    
    def _get_medication(self, medication_id: int) -> Medication:
        medication = self.db.query(Medication).filter(Medication.id == medication_id).first()
        if not medication:
            raise InvalidAdherenceLogError(f'Medication with id {medication_id} does not exist.')
        return medication

    def _validate_adherence_log(self, medication_id: int, taken_at: datetime, status: str) -> None:
        valid_statuses = {"taken", "missed", "late"}
        if not isinstance(medication_id, int):
            raise InvalidAdherenceLogError('Medication ID must be an integer.')
        if not isinstance(taken_at, datetime):
            raise InvalidAdherenceLogError('Taken at must be a valid datetime object.')
        if status not in valid_statuses:
            raise InvalidAdherenceLogError('Status must be one of "taken", "missed", or "late".')
        
    def create_adherence_log(self, user_id: int, medication_id: int, taken_at: datetime, status: str, notes: Optional[str] = None) -> AdherenceLog:
        self._validate_adherence_log(medication_id, taken_at, status)        
        user = self._get_user(user_id)
        self._get_medication(medication_id)
        adherence_log = AdherenceLog(user_id=user.id, medication_id=medication_id, taken_at=taken_at, status=status, notes=notes)
        self.db.add(adherence_log)
        try:
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise InvalidAdherenceLogError('Failed to create adherence log.') from e
        self.db.refresh(adherence_log)
        self.logger.info("Created adherence log %s", adherence_log.id)
        return adherence_log
