from django.urls import path
from . import views

# from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('subject-list/', views.subjectList, name='subject-list'),
    path('subject-create/', views.subjectCreate, name='subject-create'),
    path('subject-delete/<str:pk>/', views.subjectDelete, name='subject-delete'),
    path('character-list/', views.characterList, name='character-list'),
    path('character-create/', views.characterCreate, name='character-create'),
    path('character-delete/<str:pk>/', views.characterDelete, name='character-delete'),
    path('place-list/', views.placeList, name='place-list'),
    path('place-create/', views.placeCreate, name='place-create'),
    path('place-delete/<str:pk>/', views.placeDelete, name='place-delete'),
    path('location-list/', views.locationList, name='location-list'),
    path('location-create/', views.locationCreate, name='location-create'),
    path('location-delete/<str:pk>/', views.locationDelete, name='location-update'),
    path('author-list/', views.authorList, name='author-list'),
    path('author-create/', views.authorCreate, name='author-create'),
    path('author-delete/<str:pk>/', views.authorDelete, name='author-update'),
    path('resource_api/', views.apiOverview, name='api'),
    path('resource-list/', views.resourceList, name='resource-list'),
    path('resource-detail/<str:pk>/', views.resourceDetail, name='resource-detail'),
    path('resource-create/', views.resourceCreate, name='resource-create'),
    path('resource-update/<str:pk>/', views.resourceUpdate, name='resource-update'),
    path('resource-delete/<str:pk>/', views.resourceDelete, name='resource-delete'),
    path('user-loans/<str:name>/', views.getUserLoans, name='user-loans'),
    path('books-by/<str:name>/', views.getAuthorWorks, name='get-author-works'),
    path('save-books-by/<str:name>/', views.saveAuthorWorks, name='save-author-works'),
]
