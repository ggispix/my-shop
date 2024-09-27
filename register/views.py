
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import reverse
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('about_us')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Проверяем, есть ли параметр next для редиректа
                next_url = request.POST.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    # Если next не задан, редиректим на другую страницу, например, 'home'
                    return HttpResponseRedirect(reverse('about_us'))
            else:
                # Ошибка: неверные данные
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            # Форма не валидна
            return render(request, 'login.html', {'form': form})

    else:
        # Для метода GET возвращаем форму входа
        form = AuthenticationForm()
        # Передаём в контекст параметр next, если он есть
        return render(request, 'login.html', {'form': form, 'next': request.GET.get('next')})



def user_logout(request):
    logout(request)
    return redirect('about_us')  # Переход на главную страницу после выхода

