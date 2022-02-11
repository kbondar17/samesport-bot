import logging


from typer import Typer

from db.session import create_db, db_session, reset_db
from db.models import Section

app = Typer()
logger = logging.getLogger(__name__)


@app.command()
def reset():
    reset_db()
    logger.debug('Удалили базу!')


@app.command()
def create():
    create_db()

    logger.debug('Создали базку!')

    new_section = Section(name='Баскетбол для людей с нарушением слуха',
                          description='Занятия проходят в ФОК "На Таганке" в формате игры 3х3 или стритбола. Руководителем секции разработан специальный комплекс упражнений, который способствует развитию уже имеющихся у баскетболистов навыков, а также позволяет научиться выполнять более сложные элементы игры. Спортсмены принимают участие в различных городских турнирах и спартакиадах. Возраст занимающихся - от 16 лет и старше. Если вы не смогли дозвониться до секции по указанному телефону или у вас возникли другие проблемы с записью на занятия. сообщите нам! Информация о секции актуальна на октябрь, 2018 год.',
                          timetable='Понеделььник и среда в 18:00',
                          sport_type='Баскетбол')

    db_session.add(new_section)
    db_session.commit()

    logger.debug('Добавили в БД тестовую секцию!')


if __name__ == '__main__':
    app()
