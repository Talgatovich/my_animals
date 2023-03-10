### My_animals. Тестовое задание для Doubletapp

#### API для ведения учёта питомцев

#### Локальный запуск проекта

Клонировать репозиторий:

```
git clone git@github.com:Talgatovich/my_animals.git
```

### Вариант 1. Через Docker-compose

#### Перейти в папку с Docker-compose.yaml

#### Создать файл .env и добавить туда

```
POSTGRES_HOST=db
POSTGRES_NAME=<Название вашей БД>
POSTGRES_USER=<Логин пользователя БД>
POSTGRES_PASSWORD=<Пароль от БД>
POSTGRES_PORT=5432
```

#### Запустить контейнеры

```
docker-compose up -d
```

#### Собрать статические файлы в STATIC_ROOT

```
docker-compose exec web python manage.py collectstatic --noinput
```

#### Применить миграции

```
docker-compose exec web python manage.py migrate --noinput
```

#### Наполнить базу данных

```
docker-compose exec web python manage.py load_pets
```

#### Создать суперпользователя Django

```
docker-compose exec web python manage.py createsuperuser
```

#### Введите в адресную строку браузера localhost: приложение запущено и работает

#### Для вывода информации о питомцах в консоль

```
docker-compose exec web python3 manage.py show_pets
```

### Вариант 2. Не используя Docker-compose

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Перейти директорию с файлом settings.py

#### Создать файл .env и добавить туда

```
DJANGO_SECRET_KEY=<Приватный ключ Django>
POSTGRES_HOST=localhost
POSTGRES_NAME=<Название вашей БД>
POSTGRES_USER=<Логин пользователя БД>
POSTGRES_PASSWORD=<Пароль от БД>
POSTGRES_PORT=5432
```

Перейти в директорию с файлом manage.py

Выполнить миграции:

```
python3 manage.py migrate
```

#### Собрать статические файлы в STATIC_ROOT

```
python3 manage.py collectstatic --noinput
```

#### Наполнить базу данных

```
python3 manage.py load_pets
```

#### Создать суперпользователя Django

```
python3 manage.py createsuperuser
```

#### Запустить проект

```
python3 manage.py runserver
```

Перейти по адресу <http://127.0.0.1:8000/>

#### Для вывода информации о питомцах в консоль

```
python manage.py show_pets
```

---

#### Данный проект временно доступен по [ссылке](http://80.251.156.48/pets/)

API-KEY для доступа к API

```
l1vCnRU1.7LBYt7qgrnVuHsVdzFLVQ1yW2rMMPG7S
```

Доступ к админке:

```
login - admin
password - admin
```

---

Автор: [Ибятов Раиль](https://github.com/Talgatovich)
