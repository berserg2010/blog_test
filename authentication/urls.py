from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


app_name = 'authentication'


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='admin/login.html',
        extra_context={'site_header': 'Blog'}
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
