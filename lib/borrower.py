from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Borrower(Base):
    __tablename__ = 'borrowers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship('Book')

    def __repr__(self):
        return f"<Borrower(id={self.id}, name='{self.name}')>"
