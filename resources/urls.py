from django.urls import path
from . import views

# from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]
