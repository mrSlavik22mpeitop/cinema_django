from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import PersonCreate
from .filters import PersonFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_person(request):
    context = {}
    users_filtered = PersonFilter(request.GET, queryset=User.objects.all())
    context['users_filtered'] = users_filtered
    paginated_filtered_users = Paginator(users_filtered.qs, 4)
    page_number = request.GET.get('page')
    users_page_obj = paginated_filtered_users.get_page(page_number)
    context['users_page_obj'] = users_page_obj
    return render(request, 'person.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_person(request):
    form = PersonCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_person')
    return render(request, 'person_form.html', {'form': form, 'title': "Добавить пользователя"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_person(request, id):
    person = User.objects.get(id=id)
    form = PersonCreate(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('index_person')
    return render(request, 'person_form.html', {'form': form, 'title': "Изменить пользователя"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_person(request, id):
    person = User.objects.get(id=id)
    if request.method == 'POST':
        person.delete()
        return redirect('index_person')
    return render(request, 'person_delete.html', {'person': person})

