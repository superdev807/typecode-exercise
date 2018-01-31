# Blog editing application

Exercise project for Type/Code

## Requirements Specification

Write backend api that manages blogs.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).

```sh
$ cd backend

$ pipenv install

$ pipenv shell

$ python manage.py migrate

$ python manage.py loaddata blogs/fixtures/blogs_blogs.json

$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Built With

* [Django-rest-framework](http://www.django-rest-framework.org/) - The web
  framework used for building RESTful api
