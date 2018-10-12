from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

# def users_index(request):
#     return render(request, 'users/index.html', {'users': users})
