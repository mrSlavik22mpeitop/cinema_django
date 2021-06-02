from django.shortcuts import render, redirect
from .models import MovieShots
from .forms import MovieShotsCreate
from .filters import MovieShotsFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_movie_shots(request):
    context = {}
    movie_shots_filtered = MovieShotsFilter(request.GET, queryset=MovieShots.objects.all())
    context['movie_shots_filtered'] = movie_shots_filtered

    paginated_filtered_movie_shots = Paginator(movie_shots_filtered.qs, 4)
    page_number = request.GET.get('page')
    movie_shots_page_obj = paginated_filtered_movie_shots.get_page(page_number)
    context['movie_shots_page_obj'] = movie_shots_page_obj

    return render(request, 'movie_shots.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_movie_shots(request):
    form = MovieShotsCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_movie_shots')
    return render(request, 'movie_shots_form.html', {'form': form, 'title': "Добавить кадр"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_movie_shots(request, id):
    movie_shots = MovieShots.objects.get(id=id)
    form = MovieShotsCreate(request.POST or None, instance=movie_shots)
    if form.is_valid():
        form.save()
        return redirect('index_movie_shots')
    return render(request, 'movie_shots_form.html', {'form': form, 'title': "Изменить кадр"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_movie_shots(request, id):
    movie_shots = MovieShots.objects.get(id=id)
    if request.method == 'POST':
        movie_shots.delete()
        return redirect('index_movie_shots')
    return render(request, 'movie_shots_delete.html', {'movie_shots': movie_shots})
