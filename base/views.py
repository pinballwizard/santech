from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django import forms
from base.models import *
from django.core import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

popover_text = '''<div class="modal-body">
                        <ol class="text-left">
                            <li>Оставьте заявку</li>
                            <li>Проконсультируйтесь со специалистом</li>
                            <li>Сравните условия и цены</li>
                            <li>Закажите услугу</li>
                        </ol>
                    </div>
                    <div class="modal-footer m-footer">
                        <div class="border">
                            <a href="{% url 'contacts' %}">
                                <button type="button" class="btn yellow-btn">Оставить заявку</button>
                            </a>
                        </div>
                    </div>'''


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

template_dict = {
    'widgets': SocialWidget.objects.all(),
    'office': Office.objects.get(pk=1),
    'reviewForm': ReviewForm(),
    'ptext': popover_text,
    'review_thank': False,
}

def home(request):
    data = {
        'prices': Price.objects.filter(sale=True).order_by('?')[:3],
        'blogs': Blog.objects.order_by('-pub_date')[:3],
        'services': Service.objects.order_by('?')[:3],
    }
    data.update(template_dict)
    return render(request, 'base/home.html', data)


def blog(request):
    blog_list = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blog_list, 10)

    if request.GET.get('blog'):
        blog_article = request.GET.get('blog')
        try:
            blogs = Blog.objects.get(pk=blog_article)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        data = {
            'blogs': blogs,
            'widgets': SocialWidget.objects.all(),
            'office': Office.objects.get(pk=1),
        }
        return redirect('blog_article')
    else:
        page = request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
    data = {
        'blogs': blogs,
    }
    data.update(template_dict)
    return render(request, 'base/blog.html', data)


def blog_article(request, article):
    data = {
        'blog': Blog.objects.get(pk=article),
    }
    data.update(template_dict)
    return render(request, 'base/blog_article.html', data)


def contacts(request):
    office = Office.objects.get(pk=1)
    office_mail = office.email
    server_mail = 'ooo.service-partner@yandex.ru'
    data = {
        'form': MailForm(),

    }
    data.update(template_dict)
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
        'reviewForm': ReviewForm(),
        'ptext': popover_text,
    }
    data.update(template_dict)
    return render(request, 'base/pricing.html', data)


def reviews(request):
    p = []
    projects = Project.objects.all()
    for project1 in projects:
        project1.image = ProjectImage.objects.all().filter(project__name=project1.name)
    data = {
        'reviews': Review.objects.all(),
        'projects': projects,
        # 'projects_images': ProjectImage.objects.select_related().all(),
    }
    data.update(template_dict)
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
    }
    data.update(template_dict)
    return render(request, 'base/services.html', data)


def services_article(request, article):
    data = {
        'service': Service.objects.get(pk=article),
    }
    data.update(template_dict)
    return render(request, 'base/services_article.html', data)


def workers(request):
    data = {
        'workers': Worker.objects.all(),
    }
    data.update(template_dict)
    return render(request, 'base/workers.html', data)