                                   LIBRARY MANAGEMENT SYSTEM
                                   
#Introduction
A simple CLI-based Library Management System built with Python, SQLAlchemy, and SQLite. This system allows users to borrow books, librarians to manage records, and maintain a structured book inventory.

#Features of the system
User Management: Register and manage library users.
Book Management: Add, update, and delete book records.
Librarian Role: Manage borrowing records and oversee operations.
Records Tracking: Maintain borrowing and return history.

#Technologies Used
Python
SQLAlchemy
SQLite

#Installations
1.Clone the repository
    -git clone https://github.com/your-username/Library-application.git
    -cd Library-application

2.Create a project's virtual environment
    pipenv install - creation
    pipenv shell - activation

3.Install dependencies
    pipenv install sqlalchemy - for models structure and application operation
    pipenv install alembic - for migrations

4.Database setup

#project's domain model structure 
 Below is link url showing the projects domain model.   

![Project Image](library/images/Untitled-2025-03-13-1939.excalidraw.png)


#This is the structure of the project,s directories
├── library                    the enclosing directory
│   ├── alembic.ini
│   ├── cli.py                 -all the CLI functionality is here
│   ├── drop.py                -all the delete functionality is here
│   ├── images                 -Storage for my README.md pictures
│   │   └── Untitled-2025-03-13-1939.excalidraw.png     -domain model's picture
│   ├── models.py               -all my project's models are located here
│   ├── __pycache__
│   │   ├── drop.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── query.cpython-38.pyc
│   │   └── seed.cpython-38.pyc
│   ├── query.py                    -all the query functionality is located here
│   └── seed.py                     -all the seeding functionality is located here
├── library.db                      -this is the library management system's database
└── README.md                       -this is the project's README.md file
