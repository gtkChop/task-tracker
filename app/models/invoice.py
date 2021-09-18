from sqlalchemy import Column, Integer, DateTime, Float, Text, Boolean, String
import datetime
from app import db

class InvoiceHistory(db.Model):

    id = Column(Integer, primary_key=True)
    from_date =  Column(DateTime, nullable=False)
    to_date =  Column(DateTime, nullable=False)
    total_records = Column(Integer, nullable=False, default=0)
    name = Column(Text, nullable=True)
    _created_at = Column(DateTime, default=datetime.datetime.utcnow)
    _last_updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

    @property
    def created_at(self) -> str:
        return str(self._created_at)

    @property
    def last_updated(self) -> str:
        return str(self._last_updated)

