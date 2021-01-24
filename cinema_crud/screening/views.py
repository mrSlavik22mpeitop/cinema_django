from django.shortcuts import render, redirect
from .models import Screening
from .forms import ScreeningCreate
from django.http import HttpResponse

#DataFlair
def index_screening(request):
    screenings = Screening.objects.all()
    return render(request, 'screening.html', {'screenings': screenings})

def upload_screening(request):
    form = ScreeningCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_screening')
    return render(request, 'screening_form.html', {'form': form, 'title': "Добавить сеанс"})

def update_screening(request, id):
    screening = Screening.objects.get(id=id)
    form = ScreeningCreate(request.POST or None, instance=screening)
    if form.is_valid():
        form.save()
        return redirect('index_screening')
    return render(request, 'screening_form.html', {'form': form, 'title': "Изменить сеанс"})

def delete_movie(request, id):
    screening = Screening.objects.get(id=id)
    if request.method == 'POST':
        screening.delete()
        return redirect('index_screening')
    return render(request, 'screening_delete.html', {'screening': screening})
