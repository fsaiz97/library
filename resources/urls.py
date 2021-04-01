from django.urls import path
from . import views

# from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('resource_api/', views.apiOverview, name='api'),
    path('resource-list/', views.resourceList, name='resource-list'),
    path('resource-detail/<str:pk>/', views.resourceDetail, name='resource-detail'),
    path('resource-create/', views.resourceCreate, name='resource-create'),
    path('resource-update/<str:pk>/', views.resourceUpdate, name='resource-update'),
    path('location-list/', views.locationList, name='location-list'),
    path('location-detail/<str:pk>/', views.locationDetail, name='location-detail'),
    path('location-create/', views.locationCreate, name='location-create'),
    path('location-update/<str:pk>/', views.locationUpdate, name='location-update'),
    path('subject-list/', views.subjectList, name='subject-list'),
    path('subject-detail/<str:pk>/', views.subjectDetail, name='subject-detail'),
    path('subject-create/', views.subjectCreate, name='subject-create'),
    path('subject-update/<str:pk>/', views.subjectUpdate, name='subject-update'),
]
