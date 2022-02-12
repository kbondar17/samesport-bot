# Telegram Bot for SameSport

## Virtual environment через poetry
    - pip install poetry
    - poetry shell

## Настроить бота
    1. В корневом каталоге создать файл .env
    2. Добавить в файл логин и пароль от базы данных.
    3. Добавить в файл токен телеграм-бота.

## БД
### Создать
python -m bot.db create
### Удалить
python -m bot.db reset

## Запустить бота
    python -m bot
