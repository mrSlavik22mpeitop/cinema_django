from django.shortcuts import render, redirect
from .models import Branch
from .forms import BranchCreate
from .filters import BranchFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_branch(request):
    context = {}
    branchs_filtered = BranchFilter(request.GET, queryset=Branch.objects.all())
    context['branchs_filtered'] = branchs_filtered

    paginated_filtered_branchs = Paginator(branchs_filtered.qs, 4)
    page_number = request.GET.get('page')
    branchs_page_obj = paginated_filtered_branchs.get_page(page_number)
    context['branchs_page_obj'] = branchs_page_obj

    return render(request, 'branch.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_branch(request):
    form = BranchCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_branch')
    return render(request, 'branch_form.html', {'form': form, 'title': "Добавить кинозал"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_branch(request, id):
    branch = Branch.objects.get(id=id)
    form = BranchCreate(request.POST or None, instance=branch)
    if form.is_valid():
        form.save()
        return redirect('index_branch')
    return render(request, 'branch_form.html', {'form': form, 'title': "Изменить кинозал"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_branch(request, id):
    branch = Branch.objects.get(id=id)
    if request.method == 'POST':
        branch.delete()
        return redirect('index_branch')
    return render(request, 'branch_delete.html', {'branch': branch})

#DataFlair