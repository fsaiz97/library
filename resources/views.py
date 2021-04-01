from django.shortcuts import render, redirect
from .models import Resource
from .forms import ResourceCreate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import resourceSerializer


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
def ResourceList(request):
    tasks = Resource.objects.all().order_by('-id')
    serializer = resourceSerializer(tasks, many=True)
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
