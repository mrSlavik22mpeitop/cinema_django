from django.shortcuts import render, redirect
from .models import Seat
from .forms import SeatCreate
from .filters import SeatFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_seat(request):
    context = {}
    seats_filtered = SeatFilter(request.GET, queryset=Seat.objects.all())
    context['seats_filtered'] = seats_filtered

    paginated_filtered_seats = Paginator(seats_filtered.qs, 20)
    page_number = request.GET.get('page')
    seats_page_obj = paginated_filtered_seats.get_page(page_number)
    context['seats_page_obj'] = seats_page_obj

    return render(request, 'seat.html', context=context)


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_seat(request):
    form = SeatCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_seat')
    return render(request, 'seat_form.html', {'form': form, 'title': "Добавить место"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_seat(request, id):
    seat = Seat.objects.get(id=id)
    form = SeatCreate(request.POST or None, instance=seat)
    if form.is_valid():
        form.save()
        return redirect('index_seat')
    return render(request, 'seat_form.html', {'form': form, 'title': "Изменить место"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_seat(request, id):
    seat = Seat.objects.get(id=id)
    if request.method == 'POST':
        seat.delete()
        return redirect('index_seat')
    return render(request, 'seat_delete.html', {'seat': seat})
