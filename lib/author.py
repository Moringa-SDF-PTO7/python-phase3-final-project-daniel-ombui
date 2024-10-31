from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Junction table for many-to-many relationship between Authors and Books
author_books = Table(
    'author_books',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
)

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship('Book', secondary=author_books, back_populates='authors')

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"
