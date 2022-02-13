import re
from bot.db.sport_session    import db_session, Base
from bot.loader import get_logger

logger = get_logger(f'my_log-{__name__}')


class WordPressDatabase:
    
    # подключаемся к таблицам
    basic_section_info = Base.classes.wp_posts 
    additional_section_info =  Base.classes.wp_postmeta 
    section_terms = Base.classes.wp_terms  # возраст, вид спорта, доступность

    def get_section_info(self, uid=222):

        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()

        if not section_info:
            raise ValueError('нет такой секции')

        # эта инфа изначально в норм виде
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=uid)
        description =  meta_info_query.filter_by(meta_key='section_description').first().meta_value
        schedule = meta_info_query.filter_by(meta_key='section_schedule').first().meta_value
        contacts = meta_info_query.filter_by(meta_key='section_contacts').first().meta_value
        address = meta_info_query.filter_by(meta_key='section_address_text').first().meta_value


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

        print('инфа о секции ---',locals())

        return {'name': section_info.post_title, 'link': section_info.guid, 'schedule': schedule,
                'description': description, 'schedule': schedule, 'contacts': contacts, 'sport':sport,
                'age': age, 'availability':availability, 'section_type':section_type, 'adress': address
                }    


    def change_name(self, new_name, uid=220):
        
        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()

        if not section_info:
            raise ValueError('нет такой секции')

        section_info = db_session.query(self.basic_section_info).filter_by(ID=uid).first()
        section_info.post_title = new_name
        db_session.commit()
        logger.debug('Поменяли название секции на %s!', new_name)

    def change_description(self, new_description, u_id=220):
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=u_id)
        description = meta_info_query.filter_by(meta_key='section_description').first()
        
        if not description:
            raise ValueError('У секции нет описания!')
        
        description.meta_value = new_description
        db_session.commit()
        logger.debug('Поменяли описание секции на %s!', new_description)


    def change_timtable(self, new_timetable, u_id=220):
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=u_id)
        time_table = meta_info_query.filter_by(meta_key='section_schedule').first()
        
        if not time_table:
            raise ValueError('У секции нет описания!')

        time_table.meta_value = new_timetable
        db_session.commit()
        logger.debug('Поменяли описание секции секции на %s!', new_timetable)

    def change_contacts(self, new_contacts: str, u_id=220):
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=u_id)
        contacts = meta_info_query.filter_by(meta_key='section_contacts').first()

        if not contacts:
            raise ValueError('У секции нет описания!')

        contacts.meta_value = new_contacts
        db_session.commit()
        logger.debug('Поменяли расписание секции секции на %s!', new_contacts)


    def change_adress(self, new_adress: str, u_id=220):
        meta_info_query = db_session.query(self.additional_section_info).filter_by(post_id=u_id)
        address = meta_info_query.filter_by(meta_key='section_address_text').first()
        
        if not address:
            ValueError('у секции нет адреса')

        address.meta_value = new_adress
        db_session.commit()
        logger.debug('Поменяли адресс секции секции на %s!', new_adress)

    # обратная связь от юзера
    def add_user_data(self, uid, number): 
        pass 
    
    def add_user_data_2(self, uid, number):
        pass

    def check_if_authorized(self, uid):
        meta_info_query = db_session.query(self.user_registration).filter_by(user_id=uid)
        registation = meta_info_query.filter_by(meta_key='user_registration').first()
        if registation.user_registration: 
            return True
    
    def set_user_is_authorized(self, uid):
        meta_info_query = db_session.query(self.user_registration).filter_by(user_id=uid)
        registation = meta_info_query.filter_by(meta_key='user_registration').first()
        registation.user_registration = True


wp_repo = WordPressDatabase()