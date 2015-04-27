import urllib.request
from django.utils.encoding import iri_to_uri
import json
from django.db import models


class Worker(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    birth_day = models.DateField("День рождения")
    email = models.EmailField("Почта")
    photo = models.ImageField("Фотография", upload_to='worker')
    phone = models.CharField("Телефон", max_length=100)

    def __str__(self):
        return " ".join((self.name, self.last_name))


class Blog(models.Model):
    name = models.CharField("Название", max_length=20, unique=True)
    pub_date = models.DateField("Время публикации")
    text = models.TextField("Текст", max_length=20000)

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


class CarouselImage(models.Model):
    image = models.ImageField("Картинка", upload_to='carousel')
    text = models.CharField("Подпись", max_length=100, blank=True)
    position = models.IntegerField("Позиция", unique=True, blank=False)

    def __str__(self):
        return self.text


class Service(models.Model):
    image = models.ImageField("Изображение", upload_to='service')
    header = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Описание", max_length=1000)

    def __str__(self):
        return self.header


class Partner(models.Model):
    name = models.CharField("Название", max_length=20, unique=True)
    logo = models.ImageField("Логотип", upload_to='partner')
    url = models.URLField("Ссылка на сайт")

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

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField("Название", max_length=30)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name


class Mail(models.Model):
    sender = models.CharField("Отправитель", max_length=30)
    email = models.EmailField("Email", max_length=30)
    subject = models.CharField("Тема", max_length=50)
    message = models.TextField("Сообщение", max_length=500)

    def __str__(self):
        return " ".join((self.sender, self.subject))