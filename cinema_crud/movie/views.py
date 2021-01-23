from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieCreate
from django.http import HttpResponse

#DataFlair
def index_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movies})

def upload_movie(request):
    upload = MovieCreate()
    if request.method == 'POST':
        upload = MovieCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index_movie')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'movie_form.html', {'movie_form': upload, 'title': "Добавить новый фильм"})

def update_movie(request, movie_id):
    movie_id = int(movie_id)
    try:
        movie_sel = Movie.objects.get(id = movie_id)
    except Movie.DoesNotExist:
        return redirect('index_movie')
    movie_form = MovieCreate(request.POST or None, instance=movie_sel)
    if movie_form.is_valid():
        movie_form.save()
        return redirect('index_movie')
    return render(request, 'movie-form.html', {'movie-form': movie_form, 'title': "Изменить фильм"})

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index_movie')
    return render(request, 'movie_delete.html', {'movie': movie})
