from django.urls import path
from . import views

# from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('api/subject-list/', views.subjectList, name='api-subject-list'),
    path('api/subject-create/', views.subjectCreate, name='api-subject-create'),
    path('api/subject-delete/<str:pk>/', views.subjectDelete, name='api-subject-delete'),
    path('api/character-list/', views.characterList, name='api-character-list'),
    path('api/character-create/', views.characterCreate, name='api-character-create'),
    path('api/character-delete/<str:pk>/', views.characterDelete, name='api-character-delete'),
    path('api/place-list/', views.placeList, name='api-place-list'),
    path('api/place-create/', views.placeCreate, name='api-place-create'),
    path('api/place-delete/<str:pk>/', views.placeDelete, name='api-place-delete'),
    path('api/location-list/', views.locationList, name='api-location-list'),
    path('api/location-create/', views.locationCreate, name='api-location-create'),
    path('api/location-delete/<str:pk>/', views.locationDelete, name='api-location-update'),
    path('api/author-list/', views.authorList, name='api-author-list'),
    path('api/author-create/', views.authorCreate, name='api-author-create'),
    path('api/author-delete/<str:pk>/', views.authorDelete, name='api-author-update'),
    path('api/resource-api/', views.apiOverview, name='api-api'),
    path('api/resource-list/', views.resourceList, name='api-resource-list'),
    path('api/resource-detail/<str:pk>/', views.resourceDetail, name='api-resource-detail'),
    path('api/resource-create/', views.resourceCreate, name='api-resource-create'),
    path('api/resource-update/<str:pk>/', views.resourceUpdate, name='api-resource-update'),
    path('api/resource-delete/<str:pk>/', views.resourceDelete, name='api-resource-delete'),
    path('api/user-loans/<str:name>/', views.getUserLoans, name='api-user-loans'),
    path('api/my-loans/', views.getMyLoans, name='api-my-loans'),
    path('api/create-loan/', views.createLoan, name='api-create-loan'),
    path('api/delete-loan/<str:pk>/', views.deleteLoan, name='api-delete-loan'),
    path('api/books-by/<str:name>/', views.getAuthorWorks, name='api-get-author-works'),
    path('api/save-books-by/<str:name>/', views.saveAuthorWorks, name='api-save-author-works'),
]
