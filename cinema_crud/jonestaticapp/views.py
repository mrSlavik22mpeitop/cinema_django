from django.shortcuts import render
from movie.models import Movie
from branch.models import Branch
from screening.models import Screening
from django.contrib.auth.models import User
from seat.models import Seat
from user_information.models import Booking
from news.models import News
from movie_shots.models import MovieShots
from branch_shots.models import BranchShots
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index_john(request):
    branchs = Branch.objects.all()
    movies = Movie.objects.all()
    screenings = Screening.objects.all()
    users = User.objects.all()
    seats = Seat.objects.all()
    fixations = Booking.objects.all()
    news = News.objects.all()
    movie_shots = MovieShots.objects.all()
    branchs_shots = BranchShots.objects.all()
    total_branchs = branchs.count()
    total_movies = movies.count()
    total_screenings = screenings.count()
    total_users = users.count()
    total_seats = seats.count()
    total_fixations = fixations.count()
    total_news = news.count()
    total_movie_shots = movie_shots.count()
    total_branch_shots = branchs_shots.count()
    now_screenings = Screening.objects.raw('''
                              SELECT
                              screening_screening.id, screening_time,
                              date_film,
                              screening_screening.price, title,name
                    FROM screening_screening inner join movie_movie
                    on screening_screening.movie_mpei_id = movie_movie.id
                    inner join branch_branch
                    on screening_screening.branch_mpei_id = branch_branch.id
                    WHERE to_char(date_film, 'YYYY-MM-DD') = to_char(now(), 'YYYY-MM-DD')
                    ORDER BY screening_screening.id;
                    ''')
    paginator = Paginator(now_screenings, 4)
    page = request.GET.get('page', 1)
    mpei_page = paginator.get_page(page)
    is_paginated = mpei_page.has_other_pages()
    if mpei_page.has_previous():
        prev_url = '?page={}'.format(mpei_page.previous_page_number())
    else:
        prev_url = ''

    if mpei_page.has_next():
        next_url = '?page={}'.format(mpei_page.next_page_number())
    else:
        next_url = ''
    try:
        now_screenings = paginator.page(page)
    except PageNotAnInteger:
        now_screenings = paginator.page(1)
    except EmptyPage:
        now_screenings = paginator.page(paginator.num_pages)


    return render(request, 'main.html', {'total_branchs': total_branchs,
                                         'total_movies': total_movies,
                                         'total_screenings': total_screenings,
                                         'total_users': total_users,
                                         'total_seats': total_seats,
                                         'total_fixations': total_fixations,
                                         'total_news': total_news,
                                         'total_movie_shots': total_movie_shots,
                                         'total_branch_shots': total_branch_shots,
                                         'now_screenings': now_screenings,
                                         'is_paginated': is_paginated,
                                         'prev_url': prev_url,
                                         'next_url': next_url
                                        })

