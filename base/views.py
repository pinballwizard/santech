from django.shortcuts import render
from django import forms
from base.models import *
from django.core import mail
from random import sample

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['sender', 'email', 'subject', 'message']
        widgets = {
            'sender': forms.TextInput(attrs={
                'placeholder': 'Ваше Имя',
                'type': 'text',
                'class': 'form-control',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш Email',
                'type': 'email',
                'class': 'form-control',
                'required': True,
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Введите тему',
                'type': 'text',
                'class': 'form-control',
                'required': True,

            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Введите сообщение',
                'type': 'text',
                'class': 'form-control',
                'required': True,
                'rows': 5,
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['owner', 'header', 'text', 'grade']
        widgets = {
            'owner': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'type': 'text',
                'class': 'form-control',
                'required': True,
            }),
            'header': forms.TextInput(attrs={
                'placeholder': 'Заголовок',
                'type': 'text',
                'class': 'form-control',
                'required': True,
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Введите Отзыв',
                'type':'text',
                'class': 'form-control',
                'required': True,
                'rows': 5,
            }),
        }


def home(request):
    data = {
        'carousel_images': CarouselImage.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
        'blogs': Blog.objects.order_by('pub_date')[:3],
        'services': sample(list(Service.objects.all()), 3)
    }
    return render(request, 'base/home.html', data)


def blog(request):
    data = {
        'blogs': Blog.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
        'blog_count': range(1, round(Blog.objects.count()/1)+1, 1),
    }
    return render(request, 'base/blog.html', data)


def company(request):
    data = {
        'partners': Partner.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
        # 'about_company': Blog.objects.get(name="about_company"),
    }
    return render(request, 'base/company.html', data)


def contacts(request):
    office = Office.objects.get(pk=1)
    office_mail = office.email
    server_mail = 'ooo.service-partner@yandex.ru'
    data = {
        'office': office,
        'widgets': SocialWidget.objects.all(),
        'form': MailForm(),
        'thank': False,
    }
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subj = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            s = ":".join([sender, email, subj])
            mail.send_mail(s, message, server_mail, [office_mail], fail_silently=False)
            data['form'] = form
            data['thank'] = True
            form.save()
        else:
            data['form'] = form
    return render(request, 'base/contacts.html', data)


def pricing(request):
    data = {
        'prices': Price.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/pricing.html', data)


def reviews(request):
    data = {
        'reviews': Review.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
        'reviewForm': ReviewForm(),
        'thanks': False,
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            data['thanks'] = True
        else:
            data['reviewForm'] = form
    return render(request, 'base/reviews.html', data)


def services(request):
    data = {
        'services': Service.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/services.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
        'widgets': SocialWidget.objects.all(),
        'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/workers.html', data)