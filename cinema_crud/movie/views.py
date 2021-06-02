from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieCreate
from .filters import MovieFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_movie(request):
    context = {}
    movies_filtered = MovieFilter(request.GET, queryset=Movie.objects.all())
    context['movies_filtered'] = movies_filtered

    paginated_filtered_movies = Paginator(movies_filtered.qs, 4)
    page_number = request.GET.get('page')
    movies_page_obj = paginated_filtered_movies.get_page(page_number)
    context['movies_page_obj'] = movies_page_obj
    return render(request, 'movie.html', context=context)



@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_movie(request):
    form = MovieCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_movie')
    return render(request, 'movie_form.html', {'form': form, 'title': "Добавить фильм"})


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_movie(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieCreate(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index_movie')
    return render(request, 'movie_form.html', {'form': form, 'title': "Изменить фильм"})


@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index_movie')
    return render(request, 'movie_delete.html', {'movie': movie})
