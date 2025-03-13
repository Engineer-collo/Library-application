from models import Base,session,Book,Librarian,Record,User,engine

#Exit the program
def exit_program():
    print("Goodbyee!")
    exit()

#List all users available 
def list_all_users():
    #def list_all_users():
    print(              )
    all_users = session.query(User).all()
    print("                 All Library Users")
    for user in all_users:
        print(user)
    print(              )

#search user by name
def find_user_by_id():
    print("       ")
    input_id = input("Enter id: ")
    user = session.query(User).filter_by(id=input_id).first()
    if user:
        print(user)
    else:
        print(f'No user named {input_id} found.')  
        print("       ")

  
#list all books available
def list_all_books():
    print("                 All Library Books")
    all_books = session.query(Book).all()
    for book in all_books:
        print(book)
    print(              )


#seach book by title
def Search_book_by_id():
    input_id = int(input("Enter book id:"))
    book = session.query(Book).filter_by(id=input_id).first()
    if book:
        print(book)
    else:
        print(f'No book titled {input_id} found. ')



#list all librarians
def list_all_librarians():
    print(              )
    all_librarians = session.query(Librarian).all()
    print("                 All Librarians")
    for librarian in all_librarians:
        print(librarian)
    print(              )

def find_librarian_by_id():
    librarian_id = int(input("Enter librarian id:"))
    librarian = session.query(Librarian).filter_by(id=librarian_id).first()
    if librarian:
        print(librarian)
    else:
        print(f"Librarian id {librarian_id} not found")




        

def query_library_records():
    library_records = session.query(Record).all()
    for record in library_records:
        #print(record)
        if record.return_date == None:
            r = record.user_id
            b = record.book_id
            user = session.query(User).filter_by(id=r).first()
            book = session.query(Book).filter_by(id=b).first()
    print(f" Name: {user.name}, Phone: {user.phone}, Book borrowed: {book.title} ")


query_library_records()