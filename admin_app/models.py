from datetime import datetime

from sqlalchemy.orm import relationship

from db import Base
from pydantic import EmailStr, HttpUrl


class User(Base):
    __table__ = Base.metadata.tables['users']

    def __repr__(self):
        return f"email: {self.email} | username: {self.username} | position: {self.position}"

#
# class Article(Base):
#     __table__ = Base.metadata.tables['articles']
#
#     def __repr__(self):
#         return f"name: {self.articleName} | "
#
#
# class University(Base):
#     __table__ = Base.metadata.tables['universities']
#     universitydetails_ref = relationship("UniversityDetails")
#
#     def __repr__(self):
#         return f"name: {self.name} | genderLimitation: {self.genderLimitation}| campusType: {self.campusType} " \
#                f"gradLevel: {self.gradLevel}"
#
#
# class UniversityDetails(Base):
#     __table__ = Base.metadata.tables['universitydetails']
#
#     def __repr__(self):
#         return f"{self.text}"
#
#
# class UniversityInfoField(Base):
#     __table__ = Base.metadata.tables['universityinfofields']
#     university_ref = relationship("University")
#
#     def __repr__(self):
#         return f"{self.text}"
#
#
#
#