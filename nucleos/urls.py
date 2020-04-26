from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from apps.users.views import HomeView, SignUpView
from apps.clients.views import ClientCreationView
from apps.products.views import ProductCreationView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('register/', SignUpView.as_view(success_url=reverse_lazy('home')),
         name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'), name='logout'),

    path('new/client/', ClientCreationView.as_view(success_url=reverse_lazy('home')),
         name='newclient'),

    path('new/product/', ProductCreationView.as_view(success_url=reverse_lazy('home')),
         name='newproduct'),
]
