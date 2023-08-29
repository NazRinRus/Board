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
*Модель Ads - объявление:*
В ТЗ указано, что каждое объявление имеет отношение к одной из перечисленных категорий. В связи с чем не имеет смысла
создавать отдельную таблицу, в поле **position** будет передано символьное значение одной из категорий.
Категории будут содержаться в списке кортежей - **[('символьное обозначение','название категории'), ...]**

Согласно ТЗ, в проекте достаточно применить стандартную модель User, связав с моделью Ads по полю author_ads

    author_ads = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default='TK')
    text_ads = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)

*Модель Post - пост, содержащий отклик на объявление:*
В ТЗ указано, что автор объявления может принять отклик, после чего автору поста отклика отсылается сообщение по почте.
Отклик реализовывается в модели Post по полю respond типа boolean

    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    text_post = models.TextField()
    post_at_ad = models.ForeignKey(Ads, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    respond = models.BooleanField(default=False)

# Как реализовать WYSIWYG? django-ckeditor?
Установка пакета django-ckeditor:
1) pip install django-ckeditor; 
2) добавить ckeditor в INSTALLED_APPS; 
3) pip install psycopg2-binary --force-reinstall --no-cache-dir; видимо для postgresql
4) python3 manage.py collectstatic;

**В свободное время подумать как подчистить систему от django-skeditor**
# Проще использовать django_ckeditor_5

Подробная инструкция:
https://pypi.org/project/django-ckeditor-5/

# Представления и шаблоны

![Схема представлений.jpg](..%2F..%2F..%2F%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D1%81%D1%82%D0%BE%D0%BB%2F%D0%A4%D0%BE%D1%82%D0%BE%20%D0%BF%D0%BE%20%D0%B4%D0%BE%D1%80%D0%BE%D1%85%D0%BE%D0%B2%D1%8B%D0%BC%20%D0%B4%D0%B0%D1%87%D0%B0%D0%BC%205%2F%D0%A1%D1%85%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9.jpg)
