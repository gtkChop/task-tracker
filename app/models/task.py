import datetime
from sqlalchemy import Column, Integer, DateTime, Float, Text, Boolean, String
from sqlalchemy.dialects import postgresql
from app import db
from settings import ProjectNames


class Task(db.Model):

    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    project_name = Column(postgresql.ENUM(ProjectNames, create_type=False), nullable=False)
    issue_number = Column(String(32), nullable=True)
    issue_link = Column(Text, nullable=True)
    summary = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    no_of_hours = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

    def as_dict(self) -> dict:
        columns = [col.key for col in self.__table__.columns if not col.key.startswith("_")]
        data = {k: getattr(self, k) for k in columns}
        data['created_at'] = str(data['created_at'])
        data['last_updated'] = str(data['last_updated'])
        data['date'] = str(data['date'])
        data['project_name'] = data['project_name'].value
        return data
