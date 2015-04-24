from django.shortcuts import render
from django import forms
from base.models import *
from django.core import mail

class MailForm(forms.ModelForm):
    color = {}
    def clean(self):
        if self.cleaned_data.get('sender'):
            self.color['sender'] = 'has-success'
        else:
            self.color['sender'] = 'has-error'

        if self.cleaned_data.get('email'):
            self.color['email'] = 'has-success'
        else:
            self.color['email'] = 'has-error'

        if self.cleaned_data.get('subject'):
            self.color['subject'] = 'has-success'
        else:
            self.color['subject'] = 'has-error'

        if self.cleaned_data.get('message'):
            self.color['message'] = 'has-success'
        else:
            self.color['message'] = 'has-error'


    class Meta:
        model = Mail
        fields = ['sender', 'email', 'subject', 'message']
        localized_fields = ('__all__',)
        widgets = {
            'sender': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'type': 'text',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваш Email',
                'type': 'email',
                'class': 'form-control',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Введите тему',
                'type': 'text',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Введите сообщение',
                'type':'text',
                'class': 'form-control',
                'rows': 5,
            }),
        }



def home(request):
    data = {
        'carousel_images': CarouselImage.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/home.html', data)


def blog(request):
    data = {
        'blog': Blog.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/blog.html', data)


def company(request):
    data = {
        'partners': Partner.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
        # 'about_company': Blog.objects.get(mark="about_company"),
    }
    return render(request, 'base/company.html', data)


def contacts(request):
    # office = Office.objects.get(pk=1)
    # office_mail = office.email
    # server_mail = 'ooo.service-partner@yandex.ru'
    # data = {
    #     'office': office,
    #     'widgets': SocialWidget.objects.all(),
    #     'form': MailForm(),
    #     'thank': False,
    #     'color': {},
    # }
    # if request.method == 'POST':
    #     form = MailForm(request.POST)
    #     form.full_clean()
    #     data['color'] = form.color
    #     if form.is_valid():
    #         sender = form.cleaned_data['sender']
    #         email = form.cleaned_data['email']
    #         subj = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         s = ":".join([sender, email, subj])
    #         mail.send_mail(s, message, server_mail, [office_mail], fail_silently=False)
    #         data['form'] = form
    #         data['thank'] = True
    #         form.save()
    #     else:
    #         data['form'] = form
    return render(request, 'base/contacts.html')


def pricing(request):
    data = {
        'prices': Price.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/pricing.html', data)


def reviews(request):
    data = {
        'reviews': Review.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/reviews.html', data)


def services(request):
    data = {
        'services': Service.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/services.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
        'widgets': SocialWidget.objects.all(),
        # 'office': Office.objects.get(pk=1),
    }
    return render(request, 'base/workers.html', data)