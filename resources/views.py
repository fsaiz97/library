from django.shortcuts import render, redirect
from .models import Resource, Location, Subject
from .forms import ResourceCreate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import resourceSerializer, locationSerializer, subjectSerializer


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


@api_view(['GET'])
def resourceList(request):
    tasks = Resource.objects.all().order_by('-id')
    serializer = resourceSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def resourceDetail(request, pk):
    resource = Resource.objects.get(id=pk)
    serializer = resourceSerializer(resource, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def resourceCreate(request):
    serializer = resourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def resourceUpdate(request, pk):
    resource = Resource.objects.get(id=pk)
    serializer = resourceSerializer(instance=resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


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


@api_view(['GET'])
def locationList(request):
    locations = Location.objects.all().order_by('-id')
    serializer = locationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def locationDetail(request, pk):
    location = Location.objects.get(id=pk)
    serializer = locationSerializer(location, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def locationCreate(request):
    serializer = locationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def locationUpdate(request, pk):
    location = Location.objects.get(id=pk)
    serializer = locationSerializer(instance=location, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# subject

@api_view(['GET'])
def subjectList(request):
    subjects = Subject.objects.all().order_by('-id')
    serializer = subjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def subjectDetail(request, pk):
    subject = Subject.objects.get(id=pk)
    serializer = subjectSerializer(subject, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def subjectCreate(request):
    serializer = subjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def subjectUpdate(request, pk):
    subject = Subject.objects.get(id=pk)
    serializer = subjectSerializer(instance=subject, data=request.data)
    if serializer.is_valid():
        serializer.save()
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
        resource_sel = Resource.objects.get(id=resource_id)
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
        resource_sel = Resource.objects.get(id=resource_id)
    except Resource.DoesNotExist:
        return redirect('index')
    resource_sel.delete()
    return redirect('index')
