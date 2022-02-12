from bot.db.models import User, Section
from bot.db.session import db_session
from bot.loader import get_logger

logger = get_logger(f'my_log-{__name__}')

# TODO: переделать под sqlalchemy
# подключаем нужные либы
import pymysql
import hashlib

# создаем подключение к БД
con = pymysql.connect('host', 'user', 'зфыыцщкв', 'db')

# Данные пользователя
user_email = 'email пользователя'
# b потому что функция принимает байты
# если хэшируем ввод пользователя, то
# используем .encode() к данным
user_password = hashlib.md5(b'password пользователя')

# читаем данные
with con:
    cur = con.cursor()

    # TODO: добавить проверку пароля
    cur.execute("SELECT * FROM wp_users WHERE user_email=%s", user_email)

    id = cur.fetchone()
    print(id)
# TODO: проверить валидность кода

# each function is an SQL query
class Database:

    def add_user(self, u_id, user_name):
        user = db_session.query(User).filter_by(uid=u_id).count()
        logger.info(f'юзер {u_id} уже есть!')

        if not user:
            user = User(uid=u_id, tg_user_name=user_name)
            db_session.add(user)
            db_session.commit()
            logger.info(f'добавили юзера {u_id} в БД!')

    def change_name(self, name, u_id=1):
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        sec.name = name
        db_session.commit()
        logger.info(f'Поменяли название секции!')

    def change_description(self, description, u_id=1):
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        sec.description = description
        db_session.commit()
        logger.info(f'Поменяли описание секции!')

    def change_timetable(self, timetable, u_id=1):
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        sec.timetable = timetable
        db_session.commit()
        logger.info(f'Поменяли расписание секции!')

    def get_section_info(self, u_id=1) -> Section:
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        if not sec:
            raise ValueError('нет такой секции')
        return sec


repo = Database()
