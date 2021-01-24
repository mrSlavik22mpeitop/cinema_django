from django.shortcuts import render, redirect
from .models import Branch
from .forms import BranchCreate


#DataFlair
def index_branch(request):
    branchs = Branch.objects.all()
    return render(request, 'branch.html', {'branchs': branchs})

def upload_branch(request):
    form = BranchCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_branch')
    return render(request, 'movie_form.html', {'form': form, 'title': "Добавить кинозал"})

def update_branch(request, id):
    branch = Branch.objects.get(id=id)
    form = BranchCreate(request.POST or None, instance=branch)
    if form.is_valid():
        form.save()
        return redirect('index_branch')
    return render(request, 'branch_form.html', {'form': form, 'title': "Изменить кинозал"})

def delete_branch(request, id):
    branch = Branch.objects.get(id=id)
    if request.method == 'POST':
        branch.delete()
        return redirect('index_branch')
    return render(request, 'branch_delete.html', {'branch': branch})
