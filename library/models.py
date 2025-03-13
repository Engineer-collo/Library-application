from sqlalchemy import ForeignKey, Integer, String, Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker,relationship


Base = declarative_base()

#Records model
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer(), primary_key=True)
    borrow_date =Column(String(), nullable=False)
    return_date =Column(String(), nullable=True)
    #Relationship
    user_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer(), ForeignKey("books.id"), nullable=False)
    user = relationship("User", back_populates="records")
    book = relationship("Book" ,back_populates="records")

    def __repr__(self):
        return f"<Records(id={self.id}, user_id={self.user_id}, book_id={self.book_id}, borrow_date={self.borrow_date}, return_date={self.return_date})>"


#user model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    phone = Column(String(), nullable=False)
    #Relationships
    records = relationship("Record", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')>"



#Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), unique=True, nullable=False)
    author = Column(String(), nullable=False)
    isbn = Column(String(), unique=True, nullable=False)
    copies_available = Column(Integer())
    #Relationship
    records = relationship("Record", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', copies_available='{self.copies_available}')>"



#Librarian model
class Librarian(Base):
    __tablename__ = "librarians"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    phone = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Librarian(id={self.id}, name='{self.name}', email='{self.email}')>"




#create library database
engine = create_engine("sqlite:///library.db")
#persisting the schema
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session =Session()



