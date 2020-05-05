# Django Opencv

Proje Python 3 kullanılarak yapılacaktır.

**Python Hakkında Hatırlatmalar**
* python
    * Windows kullanıyorsanız cmd ekranında **python**
    * Linux kullanıyorsanız terminal ekranında **python3**
* pip
    * Windows kullanıyorsanız cmd ekranında **pip**
    * Linux kullanıyorsanız terminal ekranında **pip3**

**Örnek Projeyi Çalıştırma**

1. https://github.com/canokay/django_opencv/archive/master.zip adresine gidip dosyayı indirin.
2. Zip'i açın ve içerisindeki django_opencv-master klasörüne girin. 
3. Bulunduğunuz klasörde **manage.py** olduğuna emin olun.
4. Terminal ekranindan
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py createsuperuser`
    * `python manage.py runserver` kodlarını girin.


## 1. Projede Gerekli Python Kütüphaneleri Kurulumu

Projede 

```
Django 2.0.9
opencv-python
matplotlib
numpy
```
kütüphaneleri kullanılacaktır.

Kurmak için projeyi oluşturacağınız bir klasör açın. Klasör içerisine `requirements.txt` dosyası oluşturun.

`requirements.txt` içerisine 

```
Django==2.0.9
opencv-python
matplotlib
numpy
```

bilgilerini girip kapatın. 

Daha sonra proje klasörü içerisinde terminal ekranını (windows cmd, linux terminal vb.) açın. 

```
pip install -r requirements.txt
```

komutunu girin. Böylelikle gerekli olan python scriptleri pip sayesinde indirilecektir.

Eğer linux kullanıyorsanız 

```
pip3 install -r requirements.txt
```
komutunu girmelisiniz.

Windows üzerinden eğer hata alırsanız `Control Panel\System and Security\System` içerisindeki Advanced system settings > Environment Variables > Path  içerisine Python3 kurulu olan dosya yolu ve Python3/Scripts olduğuna emin olun. 

## 2. Django Proje oluşturma

Yukarıdaki kurulumları yaptıktan sonra terminal ekranında 

```
django-admin startproject django_opencv .
```

Yazın ve çalıştırın. Böylelikle bulunduğunuz klasörde 

* django_opencv
* manage.py
* requirements.txt

dosyaları oluşacaktır.

### django_opencv Klasörü

Bu klasör bizim django projemizdir. İçerisindeki python dosyaları

1. __init__.py
2. asgi.py
3. settings.py
4. urls.py
5. wsgi.py

Python dosyaları projemizin çalışmasını sağlayan python dosyalarıdır.

#### settings.py

settings.py dosyası adındanda anlaşıldığı üzere django projemizin settings kısmıdır.


## 3. Django Uygulaması Oluşturma (django_opencv_app )

Terminal ekranında 

```
python manage.py startapp django_opencv_app
```
yazıp çalıştırın.

Bu kod sayesinde şu anda projemizde 

* django_opencv
* django_opencv_app
* manage.py
* requirements.txt

klasörleri oluştu.

Yeni oluşan django_opencv_app klasörü içerisindeki

* migrations
* __init__.py
* admin.py
* apps.py
* models.py
* tests.py
* views.py

dosyalar django uygulamamızın dosyalarıdır.

## 4. django_opencv_app uygulamamızı settings.py kaydetme

Oluşturduğumuz django_opencv_app django uygulamamızın ileride yazacağımız kodların çalışması için django_opencv/settings.py içerisine kaydetmemiz gerekir.

1. django_opencv/settings.py açın

2. `INSTALLED_APPS` içerisine `'django_opencv_app'` ekleyin.

Sonuç olarak

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_opencv_app'
]
```
olmalıdır.

## 5. Django Hakkında Kısa Bilgilendirme

(Bu kısım Django veya herhangi bir web framework'ü bilmeyenler için yazılmıştır. Eğer Django'nun nasıl çalıştığını biliyorsanız geçebilirsiniz.)

Temel olarak bilinmesi gereken 3 başlık vardır. Bunlar **manage.py**, **django_projesi** ve **django uygulamaları** dır.


### manage.py 

Bu dosyanın içerisinde hiçbir değişiklik **yapılmaz**. Bu dosya çalıştığında **django_projemizin** içerisindeki **settings** modülünü çalıştırır.

Şu anda oluşturduğumuz django projesinin içerisindeki manage.py dosyasının içerisine girerseniz: 

```python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_opencv.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

kodlarını göreceksiniz. Bu kod satırları içerisindeki `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_opencv.settings')`  kodu bizim django projemizin içerisindeki `django_opencv/settings.py` dosyasını çalıştırır.

### django_opencv/settings.py 

settings.py dosyamız adındanda anlaşılabileceği üzerine proje ayarlamalarının yapıldığı dosyadır. 

* BASE_DIR = Projenin bulunduğu dosya dizinini getirir.
* SECRET_KEY = Projemizin anahtarıdır. Bu anahtar projeye özeldir. Bu anahtardan başka hiçbir proje bulunmaz. 
* DEBUG = Projenin herhangi bir serverda çalışıp çalışmadığını gösterir. Eğer geliştirme aşamasındaysa True olur.
* `INSTALLED_APPS` içerisindeki modüllerdir. Oluşturulan her django uygulaması buraya eklenir. Eklenmezse proje içerisinde kullanılamaz. 
* ROOT_URLCONF = Projedeki ana dizinde çalışacak url lokasyonu.


Yukarıda anlattığım gibi `settings.py` çalışınca içerisindeki `ROOT_URLCONF` yazan urls dosyası çalışır.

```python
ROOT_URLCONF = 'django_opencv.urls'
```
Bizim projemizde django_opencv/urls.py çalışır.


### django_opencv/urls.py

Proje içerisinde çalışacak url'lerdir. Şu anda gördüğünüz `path('admin/', admin.site.urls)` projeyi çalıştırınca göreceğimiz **localhost:8000/admin** urlsidir.

Buraya oluşturduğumuz django applerinin içerisindeki url leri import ederek çalıştırabiliriz.

## 6. django_opencv_app Kodlama

1. django_opencv_app/view.py dosyasını açın ve içerisini 

```python
from django.shortcuts import render


def IndexView(request):
    return render(request, "index.html")

```

olarak kaydedin.

2. django_opencv/settings.py dosyasını açın ve TEMPLATES'in içerisindeki DIRS'e ['templates'] ekleyin.

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
```

Sonuç yukarıdaki gibi olacaktır.

Bu yaptığımız işlem herhangi bir views.py dosyasında kullanacağımız render fonksiyonunun request olarak alacağı html sayfasının yolunun templates dosyası altında olacağını gösterecektir.

3. templates dosyası oluşturma

Projenin ana dizinine gidin ve templates dosyası oluşturun.

Sonuç olarak

* django_opencv
* django_opencv_app
* templates
* manage.py
* requirements.txt

dosyaları olacaktır.

4. templates/index.html oluşturma.

templates klasörüne gidin ve içerisinde index.html dosyası oluşturun.

Bu dosyanın içine

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

kodlarını girin.

Artık bir view ve içerisinde renderlanacak bir index.html dosyamız var. 

5. django_opencv_app/urls.py dosyası oluşturma

django_opencv_app/view.py içerisinde oluşturduğumuz IndexView'un hangi urlde gözükeceğini projemizde belirmemiz gerekiyor.

Bunun için django_opencv_app/urls.py dosyasını oluşturun ve içerisine



```python
from django.conf.urls import url
from django_opencv_app.views import IndexView


app_name = 'django_opencv_app'

urlpatterns = [
    url(r'^$', IndexView, name='homepage')
]
```

kodlarını girin. 

Böylelikle **django_opencv_app** projesinin ana urlsi girildiğinde **IndexView** çalışacak ve herhangi bir yerde bu url'yi **homepage** ismi ile kullanılabilecektir.

6. django_opencv/urls.py dosyası içerisine django_opencv_app/urls.py include etmek

django projemizin url'si django_opencv/urls.py gidin ve 

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include("django_opencv_app.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

yukarıdaki gibi girin.

Böylelikle proje ilk çalıştığında **django_opencv/urls.py** çalışacak. Anasayfa açıldığında (hiçbir parametre alınmadığında) `url(r'^',  include("django_opencv_app.urls")),` kodu çalışacak ve bu kod `django_opencv_app.urls` içerisindeki urlpatterns gelecek. django_opencv_app.urls içerisindeki urlpatterns içerisinde `url(r'^$', IndexView, name='homepage')` çalışacak ve IndexView ekrana gelecek.

## 7.Projeyi Çalıştırma

Terminal ekranını açın.

```
python manage.py runserver
```

komutunu girin.

Eğer hata almıyorsanız 

```
Django version 2.0.9, using settings 'django_opencv.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.  
```
terminalde yukarıdaki gibi http://127.0.0.1:8000/ veya http://localhost:8000/ görürsünüz. Bu url'yi tarayıcınızda açın. 

Ekranda **Hello World** yazısını göreceksiniz.


## 8. Model Oluşturma

Projemizde Image adında bir tablo kullanıcaz. Bunun oluşturmak için django_opencv_app/models.py dosyasını açın. 

```python
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(null=False, max_length=40)
    modified_image = models.ImageField(upload_to='modified_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

    def save(self):
        self.modified_image.save(self.image.name, self.image, save=False)
        super(Image, self).save()
        
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
```
kodunu girin.

* Bu Image class'ı bir Modeldir.
* İçerisinde 
    * image
    * title
    * modified_image

    alanları vardır. Bu alanlar birer **Field** dır. 
* image = ImageField yani bir resim alanıdır. Veri tabanına resim yolu olarak kaydedilir.
* title = CharField yani en fazla 40 karakterlik yazı kaydedilir (40 karakterden fazla kaydedilmez). 
* modified_image = ImageField dır. **Opencv** kullanarak değiştireceğimiz resim alanıdır.

models.py dosyasını yukarıdaki gibi kodlayıp kaydettikten sonra terminal'e gidin. 

Bir önceki terminal kodumuz 
```
python manage.py runserver
```
çalışıyorsa **Ctrl+c** ile durdurun ve hiçbir yerde çalışmadığına emin olun.

```
python manage.py makemigrations
```

girin. 

```
Migrations for 'django_opencv_app':
django_opencv_app\migrations\0001_initial.py
- Create model Image 
```

Her şey düzgün ise terminalde yukarıdaki gibi cevap gelecektir. 

Her şey düzgün çalışınca aşağıdaki gibi 

```
python manage.py migrate
```

yazıp çalıştırın. 

```
Operations to perform:
Apply all migrations: admin, auth, contenttypes, django_opencv_app, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK
Applying django_opencv_app.0001_initial... OK
Applying sessions.0001_initial... OK        
```

Yukarıdaki gibi sonuç döndüğünde herhangi bir sorun yok demektir.

```
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK

```

Yukarıdaki gibi yazılan kodlar django içerisindeki auth tablolarını oluşturur.

```
Applying django_opencv_app.0001_initial... OK
```

Yukarıdaki kod ise django_opencv_app içerisindeki models.py migrate'i oluştuğunu gösterir.

Şu anda dosyalarımıza baktığımızda


* django_opencv
* django_opencv_app
* templates
* manage.py
* db.sqlite3
* requirements.txt

göreceksiniz.

Buradaki **db.sqlite3** yukarıdaki migrate ederek oluşturduğumuz veri tabanıdır.

### Sqlite Nereden Geliyor?

django_opencv/settings.py içerisindeki **DATABASES**

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

gelir. Default olarak **sqlite3** kullanılır.

Django resmi olarak

* PostgreSQL
* MariaDB
* MySQL
* Oracle
* SQLite

veri tabanlarını destekliyor. Diğerki veri tabanlarını third party yazılımlar kullanarak projeye ekleyebilirsiniz. Biz bu proje için SQLite kullanmaya devam edeceğiz.


## 9. Django Admin Panel'i ve Image Model'ini eklemek

1. Superuser Oluşturma 

Terminal ekranında 

```
python manage.py createsuperuser
```
yazıp çalıştırın. Burada yazıldığı gibi bir superuser oluşturacağız.

```
Superuser created successfully.
```

Mesajını aldığınızda belirttiğiniz kullanıcı kayıt olmuş olacaktır.

2. Image Model Admin panel'e kaydetme

django_opencv_app/admin.py dosyasına gidin.

```py
from django.contrib import admin
from django_opencv_app.models import Image

admin.site.register(Image)

```

Yukarıdaki gibi kaydedin.

3. settings.py İçerisinde media ekleme

Şu anda ImageField olan filed'larımızın **upload** işleminin lokasyonunu belirtmemiz gerekiyor.

Bunun için django_opencv/settings.py dosyasına gidin ve en aşağıya

```py
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

kodlarını ekleyin. 

Böylelikle projeye uploadlanacak olan dosyaların yolunu **media** klasörü altında olacağını göstermiş olduk.


4. Projeyi Çalıştırıp admin sayfasına girmek

Terminal ekranında

```
python manage.py runserver
```
yazıp server'ı çalıştırın.

http://127.0.0.1:8000/admin

urlsine gidin.

Username ve Password `python manage.py createsuperuser` oluşturduğumuz kullanıcı adı ve şifreyi girin.

Her şey düzgün çalıştığında ekranda 

```
DJANGO_OPENCV_APP
Images
```

göreceksiniz.

http://127.0.0.1:8000/admin/django_opencv_app/image/

Yukarıdaki url **django_opencv_app** içerisinde oluşturduğumuz **Image** model'inin liste url'sidir.

http://127.0.0.1:8000/admin/django_opencv_app/image/add/

Yukarıdaki url **django_opencv_app** içerisinde oluşturduğumuz **Image** model'inin kayıt ekleme url'sidir.

Test için herhangi bir kayıt yapabilirsiniz.


Ek bilgi: Django Admin'i İngilizceden Türkçeye dönüştürmek için: django_opencv/settings.py içerisindeki **LANGUAGE_CODE** 'u tr olarak değiştirebilirsiniz.

```py
...
LANGUAGE_CODE = 'tr'
...
```

## 10. Anasayfaya Eklediğimiz Image Objelerini yollama

Projemizin anasayfasında http://127.0.0.1:8000/ şu anda **Hello World** yazıyor. Resimlerin gelmesi için django_opencv_app/views.py içerisini

```py
from django.shortcuts import render
from django_opencv_app.models import Image


def IndexView(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'index.html', context)

```

yukarıdaki gibi kodlayın. 

* `Image.objects.all()` veri tabanındaki image tablosundaki bütün verileri getirir `SELECT * FROM image` SQL sorgusu gibidir. Djangoda SQL sorguları kullanmak yerine ORM sorguları kullanılır.

* context index.html'e gönderdiğimiz veridir.

Şu anda resim tablosundaki verileri index.html template'ine gönderdik.

## 11. Template Yapısı 

templates/layout.html dosyasını oluşturun. Bu dosyanın içerisine aşağıdaki kodları girin.

```html
<!doctype html>
<html lang="en">
  <head>
    <title>{% block headerTitle %} {% endblock headerTitle %}</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
   
    {% block pageHeader %}

    {% endblock pageHeader %}
  
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="#">Django - Opencv</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item active">
                <a class="nav-link" href="#">Home
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">New</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">List</a>
              </li>
            </ul>
          </div>
        </div>
    </nav>
    
    <div class="container">
        <div class="row">
          <div class="col-lg-8 ml-auto mr-auto">
            {% block content %}

            {% endblock content %}
            </div>
        </div>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    
    {% block pageJs %}

    {% endblock pageJs %}

  </body>
</html>

```

index.html içerisini

```html
{% extends "layout.html" %}

{% block headerTitle %}Images {% endblock headerTitle %}

{% block content %}
    <h1>Images</h1>
    <ul>
    <a href="../add/">Add new image</a>
    {% for image in images %}
        <li><img src="{{ image.image.url }}" height=150px /> - <a href="../edit/{{image.id}}">{{ image.title }}</a></li>
    {% empty %}
        <li>No images yet.</li>
    {% endfor %}
    </ul>

{% endblock content %}


```

olarak kodlayın.

Bu yaptığımız işlem 
* layout.html adlı bir dosya oluşturduk.
    * layout.html dosyası içerisine master html layout kodlarını yazdık. Bu kodlar Cdn linkleri, head, body vb...
    * Diğerki sayfalarda kullanacağımız block'ları ekledik (content vb..)
* index.html sayfasında kullanacağımız blokları **headerTitle** ve **content** oluşturduk. Bu block'lar layout.html üzerinde belirttiğimiz blocklar oluyor. 

http://127.0.0.1:8000/ Urlsine geldiğimizde eklenen resimleri görebiliriz.



```html
    {% for image in images %}
        <li><img src="{{ image.image.url }}" height=150px /> - <a href="../edit/{{image.id}}">{{ image.title }}</a></li>
    {% empty %}
        <li>No images yet.</li>
    {% endfor %}
```

Yukarıdaki kod index.html içerisine yolladığımız **images** context'ini **image** olarak kullanmamızı sağlayan koddur. 

* http://127.0.0.1:8000/admin/django_opencv_app/image/add/ urlsine gidin ve test verileri ekleyin.
* http://127.0.0.1:8000/ anasayfaya gittiğinizde girdiğiniz veriler'i göreceksiniz.




## 12. django_opencv_app/forms.py Oluşturma

django_opencv_app/forms.py dosyasını oluşturun.

```py
from django import forms
from django_opencv_app.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image', 'title']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title'}),
        }

```

Yukarıdaki kod django_opencv_app uygulamasının içerisindeki Image model'inin formudur. Bu form kullanıldığında **image** ve **title** fieldları gelecektir. `attrs={'class': 'form-control'}` gelen inputların class değerlerine **form-control** gönderir.


## 13. CreateImageView Oluşturma

Projemizde kullanacağımız resimlerin yükleme formunu yapmak için django_opencv_app/views.py içerisinde aşağıdaki kodu ekleyin.


```py
from django.shortcuts import render, redirect
from django_opencv_app.models import Image
from django_opencv_app.forms import ImageForm

def IndexView(request):
    images = Image.objects.all().order_by("-id")
    context = {
        "images": images
    }
    return render(request, 'index.html', context)




def CreateImageView(request):
    form = ImageForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("django_opencv_app:homepage")

    context = {
        "form":form
    }
    return render(request, "imageadd.html", context)
```

CreateImageView da oluşturduğumuz **ImageForm**'u import ettik ve **imageadd.html** içerisine context olarak gönderdik. 

## 14. imageadd.html Oluştuma

templates/imageadd.html dosyasını oluşturun ve aşağıdaki gibi kodlayın.

```html
{% extends "layout.html" %}

{% block headerTitle %}Image Add {% endblock headerTitle %}

{% block content %}

<h1>Image Add</h1>

<div id="container">
    <form method = "post" enctype="multipart/form-data">
        {% csrf_token %}
        <div id="title">
            {{ form.title }}
        </div>
        <div id="image">
            {{ form.image }}
        </div>
        <button type = "submit" class = "btn btn-danger">Resim Ekle</button>
    </form>
</div>

{% endblock content %}

```

Django üzerinde form oluştururken formların içerisine **{% csrf_token %}** eklenmesi gerekmektedir. ImageForm fieldları olan title ve image yukarıdaki gibi eklenmesi yeterlidir.

## 15.imageadd Url oluşturma

django_opencv_app/urls.py içerisineki urlpatterns a

```py
url(r'^add/', CreateImageView, name='image_add'),
```
ekleyin **CreateImageView** View'u import etmeyi unutmayın.

```py
from django.conf.urls import url
from django_opencv_app.views import IndexView, CreateImageView


app_name = 'django_opencv_app'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^add/', CreateImageView, name='image_add')
]
```

Kodlar yukarıdaki gibi olmalıdır.

## 16. add url'sini çalıştırma


Terminal ekranını açın.

```
python manage.py runserver
```

ile django server'ı çalıştırın.

http://localhost:8000/add/ url'sine gittiğimizde Image form elemanları title ve image field karşınıza çıkacaktır. Test verisi girin.




## 17. ImageEditForm oluşturma

(Projenin Opencv ile düzenleme formu)

Bu projede resim opencv ile düzenlenecek. Düzenleme formunda thresh datası alınacak. 


```py
class ImageEditForm(forms.Form):
    thresh = forms.IntegerField(label='value of treshold', min_value=0, max_value=255)
```

**thresh** datası **IntegerField**'dır ve en fazla 255 girilebilir.


## 18. imageedit.html ve Opencv

(Projemizdeki Opencv View'ı)

django_opencv_app/views.py dosyasını açın.


1. ImageEditForm'u importlayın.

```py
from django_opencv_app.forms import ImageForm, ImageEditForm
```


2. Opencv import

```py
import cv2
```
ile opencv2 modülünü views.py içerisine import edin.

3. `EditCv2ImageView(request, id)`  view'ı aşağıdaki gibi oluşturun.

```py
def EditCv2ImageView(request, id):
    form = ImageEditForm(request.POST or None,request.FILES or None)
    image = Image.objects.get(id=id)
    
    if form.is_valid():
        image = Image.objects.get(id=id)

        # opencv start
        img_main  = cv2.imread(image.image.path, cv2.IMREAD_GRAYSCALE)
        thresh = form.cleaned_data['thresh']

        candidate_img = cv2.threshold(img_main, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(image.modified_image.path, candidate_img)
        # opencv end

        return redirect("django_opencv_app:homepage")

    context = {
        "form" : form,
        "image" : image
    }
    return render(request, "imageedit.html", context)
```

### EditCv2ImageView(request, id)

1. EditCv2ImageView(request, id) buradaki id url parametre olarak göndereceğimiz Image objesi id'sidir.
2. form.is_valid() olduğunda (yani post işlemi gerçekleştiğinde) opencv kodları çalışacaktır.
3. Bu örnekde düzenlenen resim'in siyah ve beyaz olmaktadır.
4. `thresh = form.cleaned_data['thresh']` thresh değişkeninden integer değer gelmektedir. String veya integer değer gelmezse hata verir. En fazla 255 değeri gelir. Bunların kontrolünü **Django** yapmaktadır. 
5. 0-255 arasındaki değer örnek olarak 
```py
...
candidate_img = cv2.threshold(img_main, 150, 255, cv2.THRESH_BINARY)[1]
```
kodu çalıştığında resim siyah beyaz olmaktadır. yukarıdaki örnek 150 verisi form üzerinden gelmektedir.

6. Siyah beyaz olan resim **modified_image** değişkenindedir. Bunun veri tabanına ve resim olarak **media/modified_images** kayıt olması gerekmektedir. Bu yeni resimin kayıt olması için

```py
cv2.imwrite(image.modified_image.path, modified_image)
```
kodu çalışır.

Buradaki `image.modified_image.path` veri tabanındaki image tablosunun içerisindeki **modified_image**'in yoludur. Yeni oluşturulan resim'in yolu burası olur. Yeni resim Opencv tarafından oluşturulur.



## 19.templates/imageedit.html oluşturma

templates/imageedit.html dosyasını oluşturun ve aşağıdaki gibi girin.

```html
{% extends "layout.html" %}

{% block headerTitle %}Images {% endblock headerTitle %}

{% block content %}

<h1>Images</h1>

<div id="container">
<form id="editForm" enctype="multipart/form-data" method="post">
    {% csrf_token %}
    <div id="title">
        {{ image.title }}
    </div>
    <div id="title">
        {{ form.treshold.errors }}
        Black and White Thresh 0-255 =  {{ form.thresh }}
    </div>
    <input id="sendform" type="submit" value="OpenCV Çalıştır">
    <div id="title_before">
        before filters
    </div>
    <div id="image">
        <img src="{{ image.image.url }}"  height="150px"/>
    </div>
    <div id="title_after">
        after filters
    </div>
    <div id="image">
        {% if image.modified_image %}
            <img src="{{ image.modified_image.url }}" height="150px"/>
        {% else %}
            <img src="{{ image.image.url }}" height="150px"/>
        {% endif %}
    </div>

</form>
</div>

{% endblock content %}

```

## 20. EditCv2ImageView url oluşturma

django_opencv_app/urls.py içerisindeki **urlpatterns** 'a 
`url(r'^edit/(?P<id>\d+)$', EditCv2ImageView, name='image_edit'),` ekleyin. Sonuç olarak

```py
from django.conf.urls import url
from django_opencv_app.views import IndexView, CreateImageView, EditCv2ImageView


app_name = 'django_opencv_app'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^add/', CreateImageView, name='image_add'),
    url(r'^edit/(?P<id>\d+)$', EditCv2ImageView, name='image_edit'),
]
```
Yukarıdaki gibi olmalıdır.

`url(r'^edit/(?P<id>\d+)$', EditCv2ImageView, name='image_edit')` bu url **localhost:8000/edit/Image_id** gibi bir url geleceğini gösterir.

Örnek:

localhost:8000/edit/1 gibi.

## 21. edit url'sini çalıştırma


Terminal ekranını açın.

```
python manage.py runserver
```

ile django server'ı çalıştırın.

Anasayfa içerisinden eklediğiniz herhangi bir resim title'ına tıklayın. localhost:8000/edit/:id (localhost:8000/edit/1) gibi bir sayfa açılacaktır.

Textbox'a 0-255 arasında bir değer girin. 

Girdiğiniz değerden sonra **modified_image** siyah beyaz olacaktır.
