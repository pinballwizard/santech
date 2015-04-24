from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def blog(request):
    return render(request, 'base/blog.html')


def company(request):
    return render(request, 'base/company.html')


def contacts(request):
    return render(request, 'base/contacts.html')


def pricing(request):
    return render(request, 'base/pricing.html')


def reviews(request):
    return render(request, 'base/reviews.html')


def services(request):
    return render(request, 'base/services.html')


def workers(request):
    return render(request, 'base/workers.html')