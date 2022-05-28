from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('', views.home, name="home"),
    path('movie/<str:pk>/', views.movie, name="movie"),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
