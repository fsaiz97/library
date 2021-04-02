from django.shortcuts import render, redirect
from .models import *
from users.models import *
from django.contrib.auth.models import User
from .forms import ResourceCreate
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


# subject

@api_view(['GET'])
def subjectList(request):
    subjects = Subject.objects.all().order_by('-subject_name')
    if not subjects:
        return Response("No subjects found", status=404)
    serializer = subjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def subjectCreate(request):
    serializer = subjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Subject creation failed", status=400)


@api_view(['DELETE'])
def subjectDelete(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response("Subject not found", status=404)

    subject.delete()
    response = "%s was deleted" % pk
    return Response(response)


# character

@api_view(['GET'])
def characterList(request):
    characters = Character.objects.all().order_by('-character_name')
    if not characters:
        return Response("No characters found", status=404)
    serializer = characterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def characterCreate(request):
    serializer = characterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Character creation failed", status=400)


@api_view(['DELETE'])
def characterDelete(request, pk):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response("Character not found", status=404)

    character.delete()
    response = "%s was deleted" % pk
    return Response(response)


# place

@api_view(['GET'])
def placeList(request):
    places = Place.objects.all().order_by('-place_name')
    if not places:
        return Response("No places found", status=404)
    serializer = placeSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def placeCreate(request):
    serializer = placeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Place creation failed", status=400)


@api_view(['DELETE'])
def placeDelete(request, pk):
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response("Place not found", status=404)

    place.delete()
    response = "%s was deleted" % pk
    return Response(response)


#location

@api_view(['GET'])
def locationList(request):
    locations = Location.objects.all().order_by('-name')
    if not locations:
        return Response("No locations found", status=404)
    serializer = locationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def locationCreate(request):
    serializer = locationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Location creation failed", status=400)


@api_view(['DELETE'])
def locationDelete(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response("Location not found", status=404)

    location.delete()
    response = "%s was deleted" % pk
    return Response(response)



# resource

@api_view(['GET'])
def resourceList(request):
    resources = Resource.objects.all().order_by('-key')
    if not resources:
        return Response("No places found", status=404)
    serializer = resourceSerializer(resources, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def resourceDetail(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = resourceSerializer(resource, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def resourceCreate(request):
    serializer = resourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Book not created", status=400)


@api_view(['POST'])
def resourceUpdate(request, pk):
    resource = Resource.objects.get(pk=pk)
    serializer = resourceSerializer(instance=resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Book not updated", status=400)


@api_view(['DELETE'])
def resourceDelete(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response("Book not found", status=404)

    resource.delete()
    response = "%s was deleted" % pk
    return Response(response)


# loans

@api_view(['GET'])
def getUserLoans(request, name):
    user = User.objects.get(username=name)
    loanList = user.profile.loans.through.objects.all()
    if not loanList:
        return Response("No loans found", status=404)
    serializer = loanReadableSerializer(loanList, many=True)
    return Response(serializer.data)

# DataFlair
def index(request):
    shelf = Resource.objects.all()
    return render(request, 'resources/library.html', {'shelf': shelf})


def upload(request):
    upload_resource = ResourceCreate()
    if request.method == 'POST':
        upload_resource = ResourceCreate(request.POST, request.FILES)
        if upload_resource.is_valid():
            upload_resource.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'resources/upload_form.html', {'upload_form': upload_resource})


def update_resource(request, resource_id):
    resource_id = int(resource_id)
    try:
        resource_sel = Resource.objects.get(pk=resource_id)
    except Resource.DoesNotExist:
        return redirect('index')
    resource_form = ResourceCreate(request.POST or None, instance=resource_sel)
    if resource_form.is_valid():
        resource_form.save()
        return redirect('index')
    return render(request, 'resources/upload_form.html', {'upload_form': resource_form})


def delete_resource(request, resource_id):
    resource_id = int(resource_id)
    try:
        resource_sel = Resource.objects.get(pk=resource_id)
    except Resource.DoesNotExist:
        return redirect('index')
    resource_sel.delete()
    return redirect('index')
