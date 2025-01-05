# Workers
# Приложение для отслеживания сотрудников и состава бригад
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

## Что дает: 
Информацию о составе бригад и о конкретных мастерах
#
http://localhost:8000/workers/ - выдает полный список мастеров.
#
http://localhost:8000/workers/worker/<int:pk>/ - выдает информацию по конкретному сотруднику.
#
http://localhost:8000/workers/brigade/<int:brigade_number>/workerslist/ - запрашивает из БД список сотрудников из конкретной бригады.

## Технологии:
- python 3.11
- SQL
- django 5.1.4
- PostgreSQL
- DRF
  
## Инструкция по развертыванию:

- Установить зависимости из файла requirements.txt в виртуальное окружение
- Использовать файл env_sample для отражения настроек

### Автор проекта:
https://github.com/NikaKoipish
