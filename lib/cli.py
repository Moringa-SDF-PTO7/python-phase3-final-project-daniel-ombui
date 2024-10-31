from sqlalchemy.orm import sessionmaker
from database import create_tables, Session
from author import Author
from book import Book
from borrower import Borrower

def main():
    
    create_tables()

    session = Session()

    while True:
        print("\nLibrary Management System")
        print("1. Add Author")
        print("2. Add Book")
        print("3. Add Borrower")
        print("4. List Authors")
        print("5. List Books")
        print("6. List Borrowers")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '0':
            break
        elif choice == '1':
            add_author(session)
        elif choice == '2':
            add_book(session)
        elif choice == '3':
            add_borrower(session)
        elif choice == '4':
            list_authors(session)
        elif choice == '5':
            list_books(session)
        elif choice == '6':
            list_borrowers(session)
        else:
            print("Invalid choice! Please try again.")

    session.close()

def add_author(session):
    name = input("Enter author name: ")
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Added Author: {author}")

def add_book(session):
    title = input("Enter book title: ")
    book = Book(title=title)
    session.add(book)
    session.commit()
    print(f"Added Book: {book}")

def add_borrower(session):
    name = input("Enter borrower name: ")
    book_id = input("Enter book ID to borrow: ")
    borrower = Borrower(name=name, book_id=book_id)
    session.add(borrower)
    session.commit()
    print(f"Added Borrower: {borrower}")

def list_authors(session):
    authors = session.query(Author).all()
    print("\nAuthors:")
    for author in authors:
        print(author)

def list_books(session):
    books = session.query(Book).all()
    print("\nBooks:")
    for book in books:
        print(book)

def list_borrowers(session):
    borrowers = session.query(Borrower).all()
    print("\nBorrowers:")
    for borrower in borrowers:
        print(borrower)

if __name__ == "__main__":
    main()
