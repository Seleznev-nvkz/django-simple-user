# Overview

Very simple user model for Django >= 1.5 with only email and password fields without permissions. Uses email for authentication.

## Installation

1. Through Github:
```sh
pip install -e git://github.com/Seleznev-nvkz/django-simple-user#egg=custom_auth
```
2. Or:
```sh
python setup.py install
```
3. Add ```'custom_auth'``` into the ```INSTALLED_APPS``` list.
4. Set your ```AUTH_USER_MODEL``` setting to use ```AbstractSimpleUser```:
```sh
AUTH_USER_MODEL = 'simple_auth.AbstractSimpleUser'
```
5. Run ```manage.py syncdb``` to create tables in database.

## Usage

For referencing to the User model you should using ```get_user_model()``` as explained in the [Django documentation](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#referencing-the-user-model). For example:
```sh
from django.contrib.auth import get_user_model

user = get_user_model().objects.get(email="example@example.com")
```
When you define a foreign key or many-to-many relations to the User model, you should specify the custom model using the ```AUTH_USER_MODEL``` setting. For example:
```sh
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
```

### Extending AbstractSimpleUser model

You can extend your model from AbstractSimpleUser. For example:
```sh
from simple_auth.models import AbstractSimpleUser

class MyUser(AbstractSimpleUser):
    username = models.CharField(max_length=64)
```
And you should change the ```AUTH_USER_MODEL``` setting to your new class:
```sh
AUTH_USER_MODEL = 'my_app.MyUser'
```
