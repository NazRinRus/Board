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

# Проще использовать django_ckeditor_5
