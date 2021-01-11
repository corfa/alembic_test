from sqlalchemy import Column, VARCHAR

from db.models import BaseModel


class DBTest_model(BaseModel):

    __tablename__ = 'test_model'

    owner = Column(VARCHAR(50))
    color = Column(VARCHAR(50))
