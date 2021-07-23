from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        'name': 'MD Shahin Mia Robin',
        'list1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def aboutUs(request):
    return HttpResponse("This about us page")


def services(request):
    return HttpResponse("This services page")
