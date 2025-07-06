
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import authView, home_

app_name = 'login_page'

urlpatterns = [
    path('signup/', authView, name='authView'),
    path('login/', LoginView.as_view(template_name='login_page/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home_, name='home_'),
    path('accounts/', include('django.contrib.auth.urls')),
]
