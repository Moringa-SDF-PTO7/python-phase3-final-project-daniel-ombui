from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    available = Column(Integer, default=1)  # 1 if available, 0 if not available

    authors = relationship('Author', secondary='author_books', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', available={self.available})>"
