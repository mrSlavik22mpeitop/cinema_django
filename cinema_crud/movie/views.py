from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieCreate


#DataFlair
def index_movie(request):

    movies = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movies})

def upload_movie(request):

    form = MovieCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_movie')
    return render(request, 'movie-form.html', {'form': form})

def update_movie(request, id):

    movie = Movie.objects.get(id=id)
    form = MovieCreate(request.POST or None, instance=movie)
    if form.is_valid():
       form.save()
       return redirect('index_movie')
    return render(request, 'movie-form.html', {'form':form, 'movie':movie})

def delete_movie(request, id):

    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index_movie')
    movie.delete()
    return redirect('index_movie')
