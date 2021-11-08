# SF_Final_project_backend
## Backend выпускного проект курса "Веб-разработчик на Python" от онлайн-школы SkillFactory - веб-сайт для внутренних опросов HR Tech

## Frontend проекта в GitHub
```
https://github.com/YuriyShashurin/SF_Final_project_frontend.git
```

### Stack backend проекта:

* Python 3.8
* Django 3.2 + PostgreSql 13

### FullStack проект развернут на публичном IP по адресу 

* Сайт проекта http://178.154.200.34
* API проекта http://178.154.200.34/api/v1/
* Документация проекта http://178.154.200.34/docs/

### Как развернуть проект локально

#### 1. Cклонировать данный репозиторий

```
git clone https://github.com/YuriyShashurin/SF_Final_project_backend.git
```

#### 2. Перейти в папку проекта

```
cd SF_Final_project_backend
```

#### 2. Создать виртуальное окружение и активировать его (вводим команды в командной строке из папки проекта)

```
* python -m venv venv
* venv/Scripts/activate.bat
```

#### 3. Устанавливаем зависимости проекта (вводим команду в командной строке из папки проекта)

```
pip install -r requirements.txt
```
#### 4. Создаем файл .env в папке проекта и добавляем актуальные для вас значения переменных ниже

```

SECRET_KEY= ENTER_YOUR_SECRET_KEY
DB_NAME='ENTER_YOUR_DB_NAME'
DB_PASSWORD='enter_your_password'
DB_HOST='localhost'
DEBUG=on
```

#### 5. Делаем миграции для создания таблиц в базе данных (вводим команду в командной строке из папки проекта)

```
python manage.py migrate
```

#### 6. Заполним модели базы данных изначальными данными - опционально (вводим команду в командной строке из папки проекта)

```
django-admin loaddata db.json
```

#### 7. Создаем суперюзера  (вводим команду в командной строке из папки проекта)

```
python manage.py createsuperuser
Далее, следовать интрукциям
```

#### 8. Запускаем проекта на dev-сервере Django и открываем его  (вводим команду в командной строке из папки проекта)

```
python manage.py runserver
http://127.0.0.1:8000/api/v1
```


### Как развернуть проект через Docker

#### 1. Выполнить шаги 1,2,4 из вышеописанного мануала

#### 2. Выполнить в консоли 
```
docker-compose up
```
#### 3. Зайти в консоль в Docker контейнера и выполнить команды миграции и загрузки фикстуры
```
docker exec -it enter_name_of_your_container bash
Команды: 
* python manage.py migrate
* django-admin loaddata db.json
* python manage.py createsuperuser
* python manage.py collectstatic
```

#### 4. Открыть проект по ссылке
```
http://127.0.0.1:8000/api/v1
```
