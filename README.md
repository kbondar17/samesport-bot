# Telegram Bot for SameSport
Чат-бот-помощник для актуализации базы данных о спортивных секциях в проекте SameSport

## Технологии
### Python
version: 3.9 or higher
### Прочее
Смотри samesport-bot/requirements.txt

## Virtual environment через poetry
Назначение - Python packaging and dependency management 
    - pip install poetry
    - poetry shell

## Настроить бота
    1. В корневом каталоге создать файл .env (в качестве примера смотри samesport-bot/.venv_defult)
    2. Добавить в файл логин и пароль от базы данных.
    3. Добавить в файл токен телеграм-бота.

## БД
Назначение - тестирование бота без взаимодействия с production database

### Создать
python -m bot.db create
### Удалить
python -m bot.db reset

## Запустить бота
    python -m bot
