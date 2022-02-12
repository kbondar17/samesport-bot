import re

from bot.db.models import User, Section
from bot.db.session import db_session, Base
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
user_password = hashlib.md5(b'users password')

# читаем данные
with con:
    cur = con.cursor()

    # TODO: добавить проверку пароля
    cur.execute("SELECT * FROM wp_users WHERE user_email=%s", user_email)

    id = cur.fetchone()
    print(id)
# TODO: проверить валидность кода


class WordPressDatabase:
    
    # подключаемся к таблицам
    basic_section_info = Base.classes.wp_posts 
    additional_section_info =  Base.classes.wp_postmeta 
    section_terms = Base.classes.wp_terms  # возраст, вид спорта, доступность

    def get_section_info(self, uid=220):

        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()

        if not section_info:
            raise ValueError('нет такой секции')

        # эта инфа изначально в норм виде
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=uid)
        description =  meta_info_query.filter_by(meta_key='section_description').first().meta_value
        schedule = meta_info_query.filter_by(meta_key='section_schedule').first().meta_value
        contacts = meta_info_query.filter_by(meta_key='section_contacts').first().meta_value

        # эту вытягиваем из строки вроде 'a:1:{i:0;s:2:"33";}' и потом идем искать в другой таблице
        age = meta_info_query.filter_by(meta_key='age').first().meta_value
        availability = meta_info_query.filter_by(meta_key='availability').first().meta_value
        section_type = int(meta_info_query.filter_by(meta_key='section_type').first().meta_value)    
        sport = meta_info_query.filter_by(meta_key='section_sport').first().meta_value
         
        # возрастов, и типов секций может не быть, а может быть несколько, проходимся и берем
        if age:
            age = re.findall(string=age, pattern='\"\d{1,2}\"')
            age = [int(e.strip('"') )for e in age]
            age =  [db_session.query(self.section_terms).filter_by(term_id=e).first().name for e in age]

        if availability:
            availability = re.findall(string=availability, pattern='\"\d{1,2}\"')
            availability = [int(e.strip('"')) for e in availability]
            availability =  [db_session.query(self.section_terms).filter_by(term_id=e).first().name for e in availability]
                
        if sport:
            sport = re.findall(string=sport, pattern='\"\d{1,2}\"')
            sport = [int(e.strip('"') )for e in sport]
            sport =  [db_session.query(self.section_terms).filter_by(term_id=e).first().name for e in sport]

        
        section_type = db_session.query(self.section_terms).filter_by(term_id=section_type).first().name

        return {'name': section_info.post_title, 'link': section_info.guid, 
                'description': description, 'schedule': schedule, 'contacts': contacts, 'sport':sport,
                'age': age, 'availability':availability, 'section_type':section_type,
                }    


    def change_name(self, new_name, uid=220):
        
        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()

        if not section_info:
            raise ValueError('нет такой секции')

        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()
        section_info.post_title = new_name
        db_session.commit()

    def change_description(self, description, u_id=1):
        pass

    
#each function is an SQL query
class Database: # старая тестовая БД, скоро удалим

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

    def get_type(self, u_id=1):
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        if not sec:
            raise ValueError('нет такой секции')
        return sec.sport_type

    def change_type(self, new_type, u_id=1):
        sec = db_session.query(Section).filter_by(uid=u_id).first()
        if not sec:
            raise ValueError('нет такой секции')
        sec.sport_type = new_type
        db_session.commit()

        logger.info(f'Поменяли тип секции!')



repo = Database()
