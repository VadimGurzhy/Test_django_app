# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VadimGurzhy/Test_django_app.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```


```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
* создать суперпользователя
```shell
python manage.py createsuperuser
```
* создать меню и его элементы через административную панель.

Запустить сервер разработки
```shell
python manage.py runserver
```
