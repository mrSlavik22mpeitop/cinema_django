from django.shortcuts import render, redirect
from .models import BranchShots
from .forms import BranchShotsCreate
from .filters import BranchShotsFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_branch_shots(request):
    context = {}
    branch_shots_filtered = BranchShotsFilter(request.GET, queryset=BranchShots.objects.all())
    context['branch_shots_filtered'] = branch_shots_filtered

    paginated_filtered_branch_shots = Paginator(branch_shots_filtered.qs, 4)
    page_number = request.GET.get('page')
    branch_shots_page_obj = paginated_filtered_branch_shots.get_page(page_number)
    context['branch_shots_page_obj'] = branch_shots_page_obj

    return render(request, 'branch_shots.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_branch_shots(request):
    form = BranchShotsCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_branch_shots')
    return render(request, 'branch_shots_form.html', {'form': form, 'title': "Добавить кадр"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_branch_shots(request, id):
    branch_shots = BranchShots.objects.get(id=id)
    form = BranchShotsCreate(request.POST or None, instance=branch_shots)
    if form.is_valid():
        form.save()
        return redirect('index_branch_shots')
    return render(request, 'branch_shots_form.html', {'form': form, 'title': "Изменить кадр"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_branch_shots(request, id):
    branch_shots = BranchShots.objects.get(id=id)
    if request.method == 'POST':
        branch_shots.delete()
        return redirect('index_branch_shots')
    return render(request, 'branch_shots_delete.html', {'branch_shots': branch_shots})
