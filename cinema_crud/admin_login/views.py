from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import AdminForm

def admin_login(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active and user.is_superuser:
                    login(request, user)
                    return render(request, 'main.html')
                else:
                    return HttpResponse('Нет прав у пользователя')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = AdminForm()
    return render(request, 'admin_login.html', {'form': form})
