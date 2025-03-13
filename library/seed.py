from models import Base,session,Book,Librarian,Record,User,engine
from datetime import date


    
def create_user():
    name = input("Enter username:")
    email = input("Enter user email:")
    phone = input("Enter user phone number:")
    
    user = User(
        name=name,
        email=email,
        phone=phone
        )

    session.add(user)
    session.commit()
    print("User added successfully.")
    print("    ")



def create_book():
    title = input("Enter book title:")
    author = input("Enter book author:")
    isbn = input("Enter book ISBN number:")
    copies_available = input("Enter number of copies available:")

    
    book = Book(
        title=title,
        author=author,
        isbn=isbn,
        copies_available=copies_available
        )

    session.add(book)
    session.commit()
    print("Book added successfully.")
    print("    ")


def create_librarian():
    name = input("Enter librarian name:")
    email = input("Enter librarian email:")
    phone = input("Enter librarian phone number:")

    librarian = Librarian(
        name=name,
        email=email,
        phone=phone
    )

    session.add(librarian)
    session.commit()
    print("Librarian added successfully.")
    print("    ")


#create records.
def borrow_a_book():
    book_being_borrowed = input("Enter book title being borrowed:")
    is_book_available = session.query(Book).filter_by(title=book_being_borrowed).first()
    if is_book_available.copies_available > 0:
        borrower_name = input("Enter name of the user borrowing a book:")
        user = session.query(User).filter_by(name=borrower_name).first()
        if user:
            userId=user.id
            book = session.query(Book).filter_by(title=book_being_borrowed).first()
            if book:
              bookId=book.id
              record = Record(
                  borrow_date =date.today(),
                  return_date = None,
                  user_id = userId,
                  book_id = bookId
              )
              bk = session.query(Book).filter_by(id=bookId).first()
              calculation = int(bk.copies_available) - 1
              bk.copies_available = calculation

              session.add(record)
              session.commit()
            print("Record added successfully")
    else:
        print(f"All available copies of {book_being_borrowed} have been borrowed")




#return borrowed book.
def return_borrowed_book():
    name_of_borrower = input("Enter a name of user returning a book:")
    user = session.query(User).filter_by(name=name_of_borrower).first()
    userId = user.id
    book_in_record = session.query(Record).filter_by(user_id=userId).first()
    book_in_record.return_date = date.today()
    session.query(Book).filter_by(id=userId)
    bk = session.query(Book).filter_by(id=userId).first()
    calculation = int(bk.copies_available) + 1
    bk.copies_available = calculation
    session.commit()
    print(f"Congratulations, book returned Successfully.")

