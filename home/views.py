from django.shortcuts import render, HttpResponse


# Create your views here.
def Home_view(request):
    if request.user.is_authenticated:

        context = {
            'isim': 'Yavuz Bektaş'

        }
    else:
        context = {
            'isim': 'Kullanıcı Tanımlı değil'

        }
    return render(request, 'home.html', context)
