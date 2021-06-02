from django.shortcuts import render, redirect
from .models import News
from .forms import NewsCreate
from .filters import NewsFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def index_news(request):
    context = {}
    news_filtered = NewsFilter(request.GET, queryset=News.objects.all())
    context['news_filtered'] = news_filtered

    paginated_filtered_news = Paginator(news_filtered.qs, 4)
    page_number = request.GET.get('page')
    news_page_obj = paginated_filtered_news.get_page(page_number)
    context['news_page_obj'] = news_page_obj

    return render(request, 'news.html', context=context)

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def upload_news(request):
    form = NewsCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_news')
    return render(request, 'news_form.html', {'form': form, 'title': "Добавить новость"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def update_news(request, id):
    news = News.objects.get(id=id)
    form = NewsCreate(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('index_news')
    return render(request, 'news_form.html', {'form': form, 'title': "Изменить новость"})

@user_passes_test(lambda u: u.is_superuser, login_url='/admin_login/login/')
def delete_news(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        news.delete()
        return redirect('index_news')
    return render(request, 'news_delete.html', {'news': news})
