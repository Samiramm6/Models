from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('news/<int:pk>', views.get_exact_pr),
    path('newsCategory/<int:pk>', views.get_exact_category),
    path('search', views.search_news),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view)
]



