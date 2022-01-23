## Проект «YaMDb»

>Учебный проект в рамках курса __Python-developer__ на платформе __Яндекс.Практикум__

## Описание:

В проекте YaMDb реализован API с помощью Django REST Framework, его задача собирать отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапозоне от одного до десяти (целое число).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Ресурсы API  __YaMDb__ :

* Ресурс auth: аутентификация.
* Ресурс users: пользователи.
* Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
* Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
* Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
* Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
* Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

__Ознакомиться с полным функционалом и примерами можно по адресу__   
__http://127.0.0.1:8000/redoc__  
__( Доступно после запуска проекта )__

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Igoryarets/api_yamdb.git
cd api_yamdb
```

Cоздать и активировать виртуальное окружение (для Windows):

```
python -m venv venv
source venv/Scripts/activate
```

Обновление менеджера пакетов pip

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
``` 



### Разработчики группового проекта

* __Адиль Акылбаев__
E-mail: [Teijodes@yandex.kz](mailto:Teijodes@yandex.kz)

* __Хуршед Бобоев__
E-mail: [khurshed-shavkatzhonovich@yandex.ru](mailto:khurshed-shavkatzhonovich@yandex.ru)

* __Максим Замятин__
E-mail: [mm.zamyatin@gmail.com](mailto:mm.zamyatin@gmail.com)
