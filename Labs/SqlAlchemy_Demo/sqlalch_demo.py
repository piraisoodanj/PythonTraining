#CRUD operation using oops (communication b/w tables and query)
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#define the database
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
SessionLocal =sessionmaker(bind=engine)


#Define a simple ORM Model
class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,autoincrement=True)
    name =Column(String,nullable=False)
    age= Column(Integer,nullable=False)


#create the database and tables
Base.metadata.create_all(engine)

#create a new session
session = SessionLocal()


#create 
# new_user=User(name='Raj',age=91)
# session.add(new_user)
# session.commit()

#Read
users = session.query(User).all()
print("All users")
for user in users:
    print(user.id,user.name,user.age)

#Update
user_to_update = session.query(User).filter_by(name='Gayathri').first()
if(user_to_update):
    user_to_update.age=56
    session.commit()


#Delete
user_to_delete=session.query(User).filter_by(name='Raj').first()
if(user_to_delete):
    session.delete(user_to_delete)
    session.commit()

    

session.close()
