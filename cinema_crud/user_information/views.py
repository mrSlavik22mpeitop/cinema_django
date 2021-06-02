from django.views.generic.base import View
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingCreate
from .filters import BookingFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from movie.models import Movie
from screening.models import Screening
from branch_shots.models import BranchShots
from news.models import News
from django.shortcuts import render, get_object_or_404
from seat.models import Seat
from .booking_services import create_seat_layout, make_booking



@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_fixation(request):
    context = {}
    fixations_filtered = BookingFilter(request.GET, queryset=Booking.objects.all())
    context['fixations_filtered'] = fixations_filtered

    paginated_filtered_fixations = Paginator(fixations_filtered.qs, 10)
    page_number = request.GET.get('page')
    fixations_page_obj = paginated_filtered_fixations.get_page(page_number)
    context['fixations_page_obj'] = fixations_page_obj

    return render(request, 'fixation.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_fixation(request):
    form = BookingCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_fixation')
    return render(request, 'fixation_form.html', {'form': form, 'title': "Закрепить место"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_fixation(request, id):
    fixation = Booking.objects.get(id=id)
    form = BookingCreate(request.POST or None, instance=fixation)
    if form.is_valid():
        form.save()
        return redirect('index_fixation')
    return render(request, 'fixation_form.html', {'form': form, 'title': "Изменить закрепление"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_fixation(request, id):
    fixation = Booking.objects.get(id=id)
    if request.method == 'POST':
        fixation.delete()
        return redirect('index_fixation')
    return render(request, 'fixation_delete.html', {'fixation': fixation})



def index_mpei(request):
    return render(request, 'about_the_cinema.html')


def user_account(request):

    corrent_user = request.user
    corrent_user_anime = corrent_user.id
    print(corrent_user_anime)
    anime = Booking.objects.raw('''
                    select  user_information_booking.id, screening_id, seat_id
                    from user_information_booking
                    where user_id = %s
    ''', [corrent_user_anime])
    return render(request, 'user_account.html', {'anime': anime})

class MoviesView(View):
    def get(self, request):
        user_movies = Movie.objects.all()
        return render(request, 'output_movie.html', {"movies_imsp": user_movies})


class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, 'movie_detail.html', {"movie": movie})



class MovieScreening(View):
    def get(self, request):
        user_screenings = Screening.objects.all()
        return render(request, 'output_screening.html', {"user_screenings": user_screenings})


class MovieDetailScreening(View):
    def get(self, request, pk):
        screening = Screening.objects.get(id=pk)
        screening_description = screening.branch_mpei.description
        return render(request, 'screening_detail.html', {"screening": screening,
                                                         "screening_description": screening_description
                                                         })

class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, 'output_news.html', {"news": news})



def book_seat(request, screening_id):

    info = ''
    booked = None

    if request.method == 'POST':
        selected_seat_id = request.POST.__getitem__('selected_seat')
        selected_seat = Seat.objects.get(id=selected_seat_id)

        booked = make_booking(selected_seat, request, screening_id)
        if booked:
            info = f'Место успешно забронировано'
        else:
            info = f'Извините, место недоступно'

    screening = get_object_or_404(Screening, pk=screening_id)
    print(screening)
    seats = Seat.objects.filter(screening_id=screening).order_by('seat_mpei')
    print("A:", seats)

    seat_columns = 6
    seat_layout = create_seat_layout(seats, seat_columns)

    return render(request, 'book_seat.html', {
        'seat_layout': seat_layout,
        'booked': booked,
        'info': info})

