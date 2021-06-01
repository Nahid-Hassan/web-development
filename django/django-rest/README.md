# Django Rest Framework

## Table of Contents

- [Django Rest Framework](#django-rest-framework)
  - [Table of Contents](#table-of-contents)
    - [Introduction](#introduction)
    - [Setup Django Project](#setup-django-project)
    - [Serializer Introduction](#serializer-introduction)
    - [Creating a Serializer class](#creating-a-serializer-class)
    - [Using ModelSerializers](#using-modelserializers)

### Introduction

Django REST API's acts as a translator between two computers/devices/machines over the network or web.

**Features**:

- Authentication Policy's.
- Serialization (Support both ORM and non ORM data source).
- Good documentation.

### Setup Django Project

First **Install** Django, Django Rest Framework

```console
nahid@infoForest:~$ pip3 install django
nahid@infoForest:~$ pip3 install djangorestframework
nahid@infoForest:~$ pip3 install markdown
nahid@infoForest:~$ pip3 install django-filter
```

**Setup Project**

```bash
# create project
nahid@infoForest:~$ django-admin startproject MyProject
nahid@infoForest:~$ cd MyProject
# make migrate
nahid@infoForest:~$ python manage.py migrate
# run server
nahid@infoForest:~$ python manage.py runserver
# create app
nahid@infoForest:~$ python manage.py startapp api_basic
```

After doing above all, create **superuser**.

```bash
# create superuser
nahid@infoForest:~$ python manage.py createsuperuser
Username: nahid
Email Address: nahid.cseru@gmail.com
Password: ****
# ....
Superuser created successfully.
```

Runserver and `login` django admin panel or site administration.

```bash
# runserver
nahid@infoForest:~$ python manage.py runserver
# open browser and run this url: localhost:port
nahid@infoForest:~$ google-chrome http://127.0.0.1:8000/
```

### Serializer Introduction

**Basic Prerequisites**:

Need to basic understanding of django **models**, **views** and **urls**.

Now understand the basics of **serializer**. Serializer is the another concept in DRF. It is an important concept.

... Before sending data to clients we need serialize it to **json**. An API is end result as always **json**, and an **API** can communicate with multiple technologies which takes json as **input**.

**Note**: DRF => Django Rest Framework.

Now first we need to install `rest_framework` and `api_basic` apps in django project `settings.py` file.

`MyProject/settings.py`

```py
# ............
INSTALLED_APPS = [
    # ..........
    'rest_framework',
    'api_basic.apps.ApiBasicConfig',
]
# ............
```

Create **Article** model class.

`api_basic/model.py`

```py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Now we need do `makemigrations` and `migrate`.

```bash
# run makemigrations
nahid@infoForest:~$ python manage.py makemigrations
# now migrate
nahid@infoForest:~$ python manage.py migrate
```

**Register** Article model in django **admin** site.

```py
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

**Runserver**:

```py
# runserver
nahid@infoForest:~$ python manage.py runserver
```

### Creating a Serializer class

The first thing we need to get started on our `Web API` is to provide a way of serializing and deserializing the snippet instances into representation such as `json`. We can do this by declaring serializers that work very similar to Django forms. Create a file in the `api_basic` directory named `serializers.py` and add the following. 

```py
class ArticleSerializer(serializers.Serializer):
    # you will need all of your fields that you have.
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    # to work with serializers we need to defines this two methods.
    def create(self, validated_data):
        return Article.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
```

Now working with **Serializers**.

```bash
# shell
nahid@infoForest:~$ python manage.py shell
# import modules
In [1]: from api_basic.serializers import ArticleSerializer                                                                                      

In [2]: from api_basic.models import Article                                                                                                     

In [3]: from rest_framework.renderers import JSONRenderer 
   ...: from rest_framework.parsers import JSONParser                                                                               

# create Article
In [4]: article = Article(title='Serializer Test', author='Md. Nahid Hassan', email='nahid.cseru@gmail.com')                                     

# save article
In [5]: article.save()               

In [6]: article = Article(title='REST API Test', author='Md. Nahid Hassan', email='nahid.cseru@gmail.com')                                       
                                                                                                       
In [7]: article.save()               

# serialize article instance
In [8]: serializer = ArticleSerializer(article)                                                                                                  

# serializer.data return json data
In [9]: serializer.data                                                                                                                          
Out[9]: {'title': 'REST API Test', 'author': 'Md. Nahid Hassan', 'email': 'nahid.cseru@gmail.com', 'date': '2021-06-01T15:29:38.647363Z'}

In [10]: content = JSONRenderer().render(serializer.data)                                                                                        

# preview content data
In [11]: content                                                                                                                                 
Out[11]: b'{"title":"REST API Test","author":"Md. Nahid Hassan","email":"nahid.cseru@gmail.com","date":"2021-06-01T15:29:38.647363Z"}'

```

**Deserializing Data**: Deserialization is similar. First we parse a stream into Python native datatypes...

```py
In [12]: import io                                                                                                                               

In [13]: stream = io.BytesIO(content)      
In [15]: data = JSONParser().parse(stream)                                                                                                       
```

...then we restore those native datatypes into a fully populated object instance.

```py
In [16]: serializer = ArticleSerializer(data=data)                                                                                               

In [17]: serializer.is_valid()                                                                                                                   
Out[17]: True

In [18]: serializer.validated_data                                                                                                               
Out[18]: 
OrderedDict([('title', 'REST API Test'),
             ('author', 'Md. Nahid Hassan'),
             ('email', 'nahid.cseru@gmail.com'),
             ('date',
              datetime.datetime(2021, 6, 1, 15, 29, 38, 647363, tzinfo=<UTC>))])
```

We can also serialize `querysets` instead of model instances. To do so we simply add a `many=True` flag to the serializer arguments.

```py
In [21]: serializer = ArticleSerializer(Article.objects.all(), many=True)                                                                        

In [22]: serializer.data                                                                                                                         
Out[22]: [OrderedDict([('title', 'Article Title'), ('author', 'Nahid'), ('email', 'nahid.cseru@gmail.com'), ('date', '2021-06-01T06:33:37.445176Z')]), OrderedDict([('title', 'Article Title1'), ('author', 'Nahid'), ('email', 'nahid.cseru@gmail.com'), ('date', '2021-06-01T06:34:37.098949Z')]), OrderedDict([('title', 'Serializer Test'), ('author', 'Md. Nahid Hassan'), ('email', 'nahid.cseru@gmail.com'), ('date', '2021-06-01T15:29:17.523293Z')]), OrderedDict([('title', 'REST API Test'), ('author', 'Md. Nahid Hassan'), ('email', 'nahid.cseru@gmail.com'), ('date', '2021-06-01T15:29:38.647363Z')])]

```

### Using ModelSerializers