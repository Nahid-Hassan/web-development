# Models
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

## The basics:

- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- With all of this, Django gives you an automatically-generated database-access API; see Making queries.

## Field

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
```

Here `first_name`, `last_name` and `instrument` is the `field` of this model.
Each `field` is specified as a `class attribute`.

## Field Option

`max_length` is the field option. Other common field option is
- null -> True/False(Default)
- blank -> True/False(Default)
- choices -> 2-tuple

To use models you need to install this app in django INSTALLED_APPS settings.py file.

```python
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```

```console
$ python manage.py makemigrations
$ python manage migrate
```

Examples Model with choices

```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```

Now run QuerysetAPI

```console
$ python manage.py shell
```