from django.shortcuts import render, redirect
from .models import *
from users.models import *
from django.contrib.auth.models import User
from .forms import ResourceCreate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.decorators import login_required
from .get_works import get_works, save_works
import json
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes


@login_required
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

@login_required
@api_view(['GET'])
def subjectList(request):
    # returns a list of book subjects
    subjects = Subject.objects.all().order_by('-subject_name')
    if not subjects:
        return Response("No subjects found", status=404)
    serializer = subjectSerializer(subjects, many=True) # creates json version of a table's row, all views use similar code
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def subjectCreate(request):
    # creates a book subject
    serializer = subjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Subject creation failed", status=400)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def subjectDelete(request, pk):
    # deletes a book subject
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response("Subject not found", status=404)

    subject.delete()
    response = "%s was deleted" % pk
    return Response(response)


# character

@login_required
@api_view(['GET'])
def characterList(request):
    # returns a list of book characters
    characters = Character.objects.all().order_by('-character_name')
    if not characters:
        return Response("No characters found", status=404)
    serializer = characterSerializer(characters, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def characterCreate(request):
    # creates a book character
    serializer = characterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Character creation failed", status=400)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def characterDelete(request, pk):
    # deletes a book character
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response("Character not found", status=404)

    character.delete()
    response = "%s was deleted" % pk
    return Response(response)


# place

@login_required
@api_view(['GET'])
def placeList(request):
    # returns a list of book settings (e.g. towns, countries, planets, etc...)
    places = Place.objects.all().order_by('-place_name')
    if not places:
        return Response("No places found", status=404)
    serializer = placeSerializer(places, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def placeCreate(request):
    # creates a book place
    serializer = placeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Place creation failed", status=400)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def placeDelete(request, pk):
    # deletes a book place
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response("Place not found", status=404)

    place.delete()
    response = "%s was deleted" % pk
    return Response(response)


#location

@login_required
@api_view(['GET'])
def locationList(request):
    # returns a list of library locations
    locations = Location.objects.all().order_by('-name')
    if not locations:
        return Response("No locations found", status=404)
    serializer = locationSerializer(locations, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def locationCreate(request):
    # creates a library location
    serializer = locationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Location creation failed", status=400)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def locationDelete(request, pk):
    # deletes a library location
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response("Location not found", status=404)

    location.delete()
    response = "%s was deleted" % pk
    return Response(response)


# author

@login_required
@api_view(['GET'])
def authorList(request):
    # returns a list of authors
    authors = Author.objects.all().order_by('-name')
    if not authors:
        return Response("No authors found", status=404)
    serializer = authorSerializer(authors, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def authorCreate(request):
    # creates an author
    serializer = authorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Author creation failed", status=400)

    
@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def authorDelete(request, pk):
    # deletes an author
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response("Author not found", status=404)

    author.delete()
    response = "%s was deleted" % pk
    return Response(response)

# resource

@login_required
@api_view(['GET'])
def resourceList(request):
    # returns a list of books owned by the library
    resources = Resource.objects.all().order_by('-id')
    if not resources:
        return Response("No places found", status=404)
    serializer = resourceSerializer(resources, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def resourceDetail(request, pk):
    # returns all stored information on a particular book
    resource = Resource.objects.get(pk=pk)
    serializer = resourceSerializer(resource, many=False)
    return Response(serializer.data)


@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def resourceCreate(request):
    # creates a new book
    serializer = resourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response("Book not created", status=400)


@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def resourceUpdate(request, pk):
    # update details of a book
    resource = Resource.objects.get(pk=pk)
    serializer = resourceSerializer(instance=resource, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Book not updated", status=400)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def resourceDelete(request, pk):
    # deletes a book
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response("Book not found", status=404)

    resource.delete()
    response = "%s was deleted" % pk
    return Response(response)
'''
@login_required
@api_view(['DELETE'])
def resourceSearchBySubject(request, name):
    # finds all books on a particular subject
    try
    subject = Subject.objects.get(subject_name=name)
    except Subject.DoesNotExist:
        return Response("Subject not found", status=404)
    resources = Resource.objects.filter(subject__in=subjects).order_by('-id')
    if not resources:
        return Response("No books found", status=404)
    serializer = resourceSerializer(resources, many=True)
    return Response(serializer.data)
'''

# loans

@permission_classes([IsAdminUser])
@login_required
@api_view(['GET'])
def getUserLoans(request, name):
    # returns a list of loan records involving a particular user
    if request.user.is_superuser:
        user = User.objects.get(username=name)
        loanList = user.profile.loans.through.objects.all()
        if not loanList:
            return Response("No loans found", status=404)
        serializer = loanReadableSerializer(loanList, many=True)
        return Response(serializer.data)
    else:
        return Response("Admin credentials required", status=401)

@login_required
@api_view(['GET'])
def getMyLoans(request):
    # returns a list of loan records involving the logged on user
    user = request.user
    loanList = user.profile.loans.through.objects.all()
    if not loanList:
        return Response("No loans found", status=404)
    serializer = loanReadableSerializer(loanList, many=True)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def createLoan(request):
    username = request.data["user"]
    user = User.objects.get(username=username)
    title = request.data["resource"]
    book = Resource.objects.get(title=title)
    loan = Loan(account=user.profile, resource=book)
    loan.save()
    serializer = loanReadableSerializer(loan)
    return Response(serializer.data)

@permission_classes([IsAdminUser])
@login_required
@api_view(['DELETE'])
def deleteLoan(request, pk):
    # deletes a loan
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response("Loan not found", status=404)

    loan.delete()
    response = "Loan %s was deleted" % pk
    return Response(response)


# Open Library API


@login_required
@api_view(['GET'])
def getAuthorWorks(request, name):
    # returns a list of an author's works
    output = get_works(name)
    if output == "Not Found":
        return Response("Author "+output, status=404)
    else:
        return Response(output)

@permission_classes([IsAdminUser])
@login_required
@api_view(['POST'])
def saveAuthorWorks(request, name):
    # saves 1 of every work made by an author
    output = get_works(name)
    if output == "Not Found":
        return Response("Author "+output, status=404)
    works_json = json.loads(output)
    result = save_works(works_json)
    if result == -1:
        return Response("Works not saved", status=400)
    else:
        return Response(str(result), status=418)

# DataFlair
def index(request):
    # returns a list of all books, with buttons to edit and delete each book
    shelf = Resource.objects.all()
    return render(request, 'resources/library.html', {'shelf': shelf})

@permission_classes([IsAdminUser])
@login_required
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

@permission_classes([IsAdminUser])
@login_required
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

@permission_classes([IsAdminUser])
@login_required
def delete_resource(request, resource_id):
    resource_id = int(resource_id)
    try:
        resource_sel = Resource.objects.get(pk=resource_id)
    except Resource.DoesNotExist:
        return redirect('index')
    resource_sel.delete()
    return redirect('index')
