from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]


"""NOTEtoJason
    below is related to How to manage static files (e.g. images, JavaScript, CSS)¶
    Websites generally need to serve additional files such as images, JavaScript, or CSS. 
    In Django, we refer to these files as “static files”. 
    Django provides django.contrib.staticfiles to help you manage them.

    This page describes how you can serve these static files.
    page = https://docs.djangoproject.com/en/dev/howto/static-files/

    This is not suitable for production use! For some common deployment strategies, 
    see How to deploy static files.
    https://docs.djangoproject.com/en/dev/howto/static-files/deployment/
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
