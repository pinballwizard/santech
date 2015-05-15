import urllib.request
from django.utils.encoding import iri_to_uri
import json
from django.db import models
from ckeditor.fields import RichTextField

class Worker(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    birth_day = models.DateField("День рождения")
    email = models.EmailField("Почта")
    photo = models.ImageField("Фотография", upload_to='worker')
    phone = models.CharField("Телефон", max_length=100)

    class Meta():
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return " ".join((self.name, self.last_name))


class Blog(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    pub_date = models.DateField("Время публикации")
    text = RichTextField("Текст", max_length=20000)

    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name


class Review(models.Model):
    GRADE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    owner = models.CharField("Клиент", max_length=50, unique=True)
    header = models.CharField("Заголовок", max_length=20)
    text = models.CharField("Отзыв", max_length=500)
    grade = models.IntegerField("Оценка", choices=GRADE_CHOICES, default=5)

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Project(models.Model):
    name = models.CharField("Название проекта", max_length=100)
    face_image = models.ImageField("Заставка", upload_to='project')

    class Meta():
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField("Картинка", upload_to='project')
    text = models.CharField("Комментарий", max_length=500, blank=True)

    class Meta():
        verbose_name = "Фотография проекта"
        verbose_name_plural = "Фотографии проекта"


class Service(models.Model):
    image = models.ImageField("Изображение", upload_to='service')
    header = models.CharField("Заголовок", max_length=20, unique=True)
    text = RichTextField("Описание", blank=True)

    class Meta():
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.header


class Partner(models.Model):
    name = models.CharField("Название", max_length=20, unique=True)
    logo = models.ImageField("Логотип", upload_to='partner')
    url = models.URLField("Ссылка на сайт")

    class Meta():
        verbose_name = "Партнер"
        verbose_name_plural = "Партнера"

    def __str__(self):
        return self.name


class Office(models.Model):
    MAP_CHOICES = (
        ('yandex#map', 'Схема'),
        ('yandex#satellite', 'Спутник'),
        ('yandex#hybrid', 'Гибрид'),
        ('yandex#publicMap', 'Народная'),
        ('yandex#publicMapHybrid', 'Народная+Гибрид'),
    )

    name = models.CharField("Название компании", max_length=100)
    address = models.CharField("Контактный адресс", max_length=100)
    email = models.EmailField("Контактная почта", max_length=50, blank=True)
    phone1 = models.CharField("Телефон Офис", max_length=15, blank=True)
    phone2 = models.CharField("Телефон Тех.поддержки", max_length=15, blank=True)
    latitude = models.CharField("Широта", max_length=10)
    longitude = models.CharField("Долгота", max_length=10)
    maptype = models.CharField("Тип карты", max_length=30, choices=MAP_CHOICES, default='yandex#map')

    class Meta():
        verbose_name = "Офисы"
        verbose_name_plural = "Офис"

    def coordinate(self):
        return [self.longitude, self.latitude]

    def geocode(self):
        url_str = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode=%s' % self.address
        req = urllib.request.Request(iri_to_uri(url_str))
        with urllib.request.urlopen(req) as f:
            json_data = f.read().decode('utf-8')
        obj = json.loads(json_data)
        c = obj["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        coordinate = c.split()
        self.latitude = coordinate[0]
        self.longitude = coordinate[1]


class SocialWidget(models.Model):
    SOCIAL_CHOICES = (
        ('vk', 'Вконтакте'),
        ('ok', 'Одноклассники'),
        ('fb', 'Facebook'),
        ('tw', 'Twitter'),
        ('li', 'LinkedIn'),
        ('yt', 'YouTube'),
        ('in', 'Instagram'),
    )
    name = models.CharField("Название", max_length=2, choices=SOCIAL_CHOICES)
    url = models.URLField("Ссылка", blank=True)

    class Meta():
        verbose_name = "Социальный виджет"
        verbose_name_plural = "Социальные виджеты"

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField("Название", max_length=30)
    price = models.IntegerField("Цена")
    sale = models.BooleanField("Акция", help_text="Указать отображение на главной странице")

    class Meta():
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return self.name


class Mail(models.Model):
    sender = models.CharField("Отправитель", max_length=30)
    email = models.EmailField("Email", max_length=30)
    subject = models.CharField("Тема", max_length=50)
    message = models.TextField("Сообщение", max_length=500)

    class Meta():
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    def __str__(self):
        return " ".join((self.sender, self.subject))