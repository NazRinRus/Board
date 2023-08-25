# BOARD project

# 1) Создание виртуального окружения:
python3 -m venv venv_board
# 2) Активировать виртуальное окружение:
source venv_board/bin/activate
# 3) Установка django:
pip3 install django
# 4) Создание проекта Board:
django-admin startproject Board
# 5) Создание приложения abs:
cd Board
python3 manage.py startapp abs
# 6) Создание базы данных postgresql в терминале:
Командная строка postgresql:
**sudo -i -u postgres**

Создать БД:
**createdb board_db**

Консоль суперпользователя:
**psql**

Установить пароль суперпользователя:
**ALTER USER postgres WITH PASSWORD 'мой стандартный пароль';**

Создать нового пользователя:
**CREATE USER nazrinrus WITH PASSWORD 'мой стандартный пароль';**

Дал права суперпользователя новому пользователю:
**ALTER USER nazrinrus WITH SUPERUSER;**

Команды: 
**\q** выход с консоли суперюзера;
**\l** просмотр существующих БД;
**\du** просмотр списка пользователей;
**exit** выход с консоли postgresql/

# 7) Описание моделей:


