# Django RESTFUL API

A simple ToDo List with CRUD Operations using DJANGO REST FRAMEWORK.

## Requirements

    1. Python
    2. PIP

## Create virtual environment

    path-to-folder\python -m venv .venv

## Activate virtual environment

    path-to-folder\.venv\Scripts\activate

## Installation

    pip install -r requirements.txt

    
    path-to-where-manage.py-is-located\python manage.py makemigrations
    path-to-where-manage.py-is-located\python manage.py migrate

## Creating Superuser

     path-to-where-manage.py-is-located\python manage.py createsuperuser

## Running the server

     path-to-where-manage.py-is-located\python manage.py runserver

## URLS

    CREATE
    http://localhost:8000/create/
    READ
    http://localhost:8000/todo-list/
    UPDATE
    http://localhost:8000/todo-list/id/
    DELETE
    http://localhost:8000/delete/id/
