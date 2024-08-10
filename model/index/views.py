from django.shortcuts import render
from .models import NewsCategory, News
from .forms import RegisterForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User




# Create your views here.
def home_page(request):
    # получаем данные из бд
    news = News.objects.all()
    newsCategory = NewsCategory.objects.all()

    # передаем данные на фронт
    context = {'news': news,
               'newsCategory': newsCategory,
               }
    return render(request, 'home.html', context)


def get_exact_pr(request, pk):
    exact_product = News.objects.get(id=pk)

    context = {'news': exact_product}
    return render(request, 'news.html', context)

def get_exact_category(request, pr):
    exact_category = NewsCategory.objects.get(id=pr)
    news = News.objects.filter(pr_category=exact_category)

    context = {'news': news}
    return render(request, 'category.html', context)

def search_news(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')

        try:
            exact_news = News.objects.get(pr_name__icontains=get_news)
            return redirect(f'news/{exact_news.id}')
        except:
            print('не нашел')
            return redirect('/')


class Register(View):
    template_name = 'registration/register.html'


    def get(self, request):
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.clean_password2()
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, password=password2, email=email)
            user.save()
            login(request, user)
            return redirect('/')
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')

