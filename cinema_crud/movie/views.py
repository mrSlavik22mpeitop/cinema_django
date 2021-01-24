from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieCreate
from django.http import HttpResponse

#DataFlair
def index_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movies})

def upload_movie(request):
    form = MovieCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_movie')
    return render(request, 'movie_form.html', {'form': form, 'title': "Добавить фильм"})

def update_movie(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieCreate(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index_movie')
    return render(request, 'movie_form.html', {'form': form, 'title': "Изменить фильм"})

def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index_movie')
    return render(request, 'movie_delete.html', {'movie': movie})
