from django.shortcuts import render, redirect
from .models import Screening
from .forms import ScreeningCreate
from .filters import ScreeningFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_screening(request):
    context = {}
    screenings_filtered = ScreeningFilter(request.GET, queryset=Screening.objects.all())
    context['screenings_filtered'] = screenings_filtered

    paginated_filtered_screenings = Paginator(screenings_filtered.qs, 4)
    page_number = request.GET.get('page')
    screenings_page_obj = paginated_filtered_screenings.get_page(page_number)
    context['screenings_page_obj'] = screenings_page_obj

    return render(request, 'screening.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_screening(request):
    form = ScreeningCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_screening')
    return render(request, 'screening_form.html', {'form': form, 'title': "Добавить сеанс"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_screening(request, id):
    screening = Screening.objects.get(id=id)
    form = ScreeningCreate(request.POST or None, instance=screening)
    if form.is_valid():
        form.save()
        return redirect('index_screening')
    return render(request, 'screening_form.html', {'form': form, 'title': "Изменить сеанс"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_screening(request, id):
    screening = Screening.objects.get(id=id)
    if request.method == 'POST':
        screening.delete()
        return redirect('index_screening')
    return render(request, 'screening_delete.html', {'screening': screening})
