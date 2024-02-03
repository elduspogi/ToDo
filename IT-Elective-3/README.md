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

    python manage.py migrate

## Creating Superuser

    python manage.py createsuperuser

## Running the server

    python manage.py runserver

## URLS

    CREATE
    http://localhost:8000/create/
    READ
    http://localhost:8000/todo-list/
    UPDATE
    http://localhost:8000/todo-list/id/
    DELETE
    http://localhost:8000/delete/id/
