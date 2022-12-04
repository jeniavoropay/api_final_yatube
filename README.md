# **API для YaTube**
## **Описание**
API для взаимодействия с проектом **YaTube**(https://github.com/jeniavoropay/hw05_final).
### Автор
Евгения Воропай
## **Как запустить проект**
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/jeniavoropay/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
## **Примеры запросов к API**
```
GET /api/v1/posts/
```
**Пример ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
POST /api/v1/posts/
```
**Пример запроса**
```
{
    "text": "string",
    "image": "string",
    "group": 0
} 
```
**Пример ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PUT /api/v1/posts/{id}/
```
**Пример запроса**
```
{
    "text": "newstring",
    "image": "string",
    "group": 0
}
```
**Пример ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "newstring",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
PATCH /api/v1/posts/{id}/
```
**Request sample**
```
{
    "text": "updstring"
}
```
**Response sample**
```
{
    "id": 0,
    "author": "string",
    "text": "updstring",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
---
```
DELETE /api/v1/posts/{id}/
```
---
```
GET /api/v1/posts/{post_id}/comments/
```
**Пример ответа**
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```
---
```
POST /api/v1/posts/{post_id}/comments/
```
**Пример запроса**
```
{
    "text": "string"
}
```
**Пример ответа**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
---
```
POST /api/v1/jwt/create/
```
**Пример запроса**
```
{
    "username": "string",
    "password": "string"
}
```
**Пример ответа**
```
{
    "refresh": "string",
    "access": "string"
}
```
