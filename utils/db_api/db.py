import datetime
from sqlalchemy import create_engine, Integer, String, Column, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from data.config import USER_POSTGRES, PASSWORD_POSTGRES, HOST_POSTGRES, BASE_POSTGRES


engine = create_engine(f"postgresql+psycopg2://{USER_POSTGRES}:{PASSWORD_POSTGRES}@"
                       f"{HOST_POSTGRES}/{BASE_POSTGRES}")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Books(Base):
    """
    Клас описывает табоицу хранения данных в БД
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    author = Column(String(100), default='')
    year = Column(Integer, nullable=False)
    language = Column(String(75))
    translation = Column(String(50))
    date = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    active = Column(Boolean, default=False, nullable=False)
    url = Column(String, default='')
    local_path = Column(String, default='')
    telegram_file_id = Column(String(150), default='', nullable=False)
    local_path_pic = Column(String, default='', nullable=False)

    def __repr__(self):
        return f"<Books(name={self.name}, " \
               f"year={self.date}, " \
               f"id={self.id}, " \
               f"active={self.active}>"


def get_book_id(book_id: int):
    """
    Функция возвращает книгу найденную по id
    """""
    book = session.query(Books).get(book_id)
    return book


def add_new_book(dict_data: dict):
    """
    Функция создает новую запись с книгой
    """
    new_book = Books(
        name=dict_data.get('name'),
        author=dict_data.get('author'),
        year=dict_data.get('year'),
        language=dict_data.get('language'),
        translation=dict_data.get('translation'),
        local_path=dict_data.get('local_path'),
        telegram_file_id=dict_data.get('telegram_file_id'),
        local_path_pic=dict_data.get('local_path_pic')
    )
    session.add(new_book)
    session.commit()


Base.metadata.create_all(engine)




