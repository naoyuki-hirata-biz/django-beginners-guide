# A Complete Beginner's Guide to Django 4.2

[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.2-brightgreen.svg)](https://djangoproject.com)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-5.3-brightgreen.svg)](https://djangoproject.com)

Code samples from the Django tutorial series.

![Django Boards Screenshot](https://github.com/naoyuki-hirata-biz/django42-beginners-guide/assets/1642937/9b4ef9d0-0582-404c-b4a9-c0654b44600d)


## Table of Contents

* [Part 1 - Getting Started](https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html)
* [Part 2 - Fundamentals](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
* [Part 3 - Advanced Concepts](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)
* [Part 4 - Authentication](https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html)
* [Part 5 - ORM](https://simpleisbetterthancomplex.com/series/2017/10/02/a-complete-beginners-guide-to-django-part-5.html)
* [Part 6 - Class-Based Views](https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html)
* [Part 7 - Deployment](https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html)

For the complete tutorial series index [click here](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/).


## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/naoyuki-hirata-biz/django42-beginners-guide.git
cd django42-beginners-guide
```
```bash
docker compose build
docker compose up
```

```bash
docker compose exec python bash
python -m venv django42
source django42/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```

Create the database:

```bash
mysql -h mysql -u root
create database myproject;
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/django-beginners-guide/blob/master/LICENSE).

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)

The tutorials, documentations, comics are licensed under the
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
