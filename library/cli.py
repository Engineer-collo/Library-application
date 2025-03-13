
#fetching data from the database
from query import (
    exit_program,
    list_all_users,
    list_all_books,
    find_user_by_id,
    Search_book_by_id,
    list_all_librarians,
    find_librarian_by_id,
    query_library_records
)

#Adding data to the database
from seed import (
    create_user,
    create_book,
    create_librarian,
    borrow_a_book,
    return_borrowed_book
)

#deleting data from the database
from drop import(
    delete_librarian,
    delete_user,
    delete_book
    
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_users()
        elif choice == "2":
            list_all_books()
        elif choice == "3":
            create_user()
        elif choice == "4":
            create_book()
        elif choice == "5":
            find_user_by_id()
        elif choice == "6":
            Search_book_by_id()
        elif choice == "7":
            create_librarian()
        elif choice == "8":
            list_all_librarians()
        elif choice == "9":
            delete_librarian()
        elif choice == "10":
            find_librarian_by_id()
        elif choice == "11":
            delete_user()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            borrow_a_book()
        elif choice == "14":
            return_borrowed_book()
        elif choice == "15":
            query_library_records()
        
def menu():
    print("Welcome! Please select an option.")
    print("0. Exit program")
    print("1. List all library users")
    print("2. List all library books")
    print("3. Add library user")
    print("4. Add book to the library")
    print("5. Search user by id")
    print("6. Search book by id")
    print("7. Add librarian")
    print("8. List all librarians")
    print("9. Delete librarian")
    print("10. Search librarian by id")
    print("11. Delete user")
    print("12. Delete book")
    print("13. Create a library borrow record")
    print("14. Clear library pending borrow record")
    print("15. List library users with pending book record")

if __name__ == "__main__":
    main()
