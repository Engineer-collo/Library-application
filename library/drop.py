from models import Base,session,Book,Librarian,Record,User,engine


#delete librarian
def delete_librarian():
    librarian_id = int(input("Enter librarian id:"))
    librarian = session.get(Librarian,librarian_id)
    if librarian:
        session.delete(librarian)
        session.commit()
        print("Librarian deleted successfully.")
    else:
        print(f"librarian id {librarian_id} not found.")



#delete user
def delete_user():
    user_id = int(input("Enter user Id:"))
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"{user.name} deleted successfully.")
    else:
        print(f"user id {user_id} not found.")




#delete book
def delete_book():
    book_id = int(input("Enter book id:"))
    book = session.get(Book, book_id)
    if book:
        session.delete(book)
        session.commit()
        print(f"Book id {book_id} deleted successfully")
    else:
        print(f"Book id {book_id} not found")
