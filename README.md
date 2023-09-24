# Создание коротких ссылок с помощью сервиса Bitly

Данный проект преобразует обычные ссылки в короткие и показывает сумму кликов по ним.


## Установка

Должен быть установлен python3.
Затем используйте pip (или pip3, если есть конфликт с python2) для установки зависимостей:

`pip install -r requirements.txt`

или

`pip3 install -r requirements.txt`

Рекомендуется использовать venv для изоляции проекта.


## Ключ

Для получения ключа (токена) зарегистрируйтесь на https://app.bitly.com через e-mail для личного пользования (так проще и быстрее). После подтверждения e-mail перейдите по ссылке для создания токена:

https://app.bitly.com/settings/api/

После генерации ключ должен быть сохранён в `.env` файл в директорию проекта в следующем формате:

`BITLY_TOKEN=вместо этого текста вставьте токен`


## Запуск

Находясь в директории проекта, откройте с помощью python3 файл `main.py`:

`python main.py`


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков https://dvmn.org/.