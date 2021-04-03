# import required modules
import requests
from pprint import pprint
import json
import pandas as pd
from olclient.openlibrary import OpenLibrary
from .models import *
import datetime
from dateutil import parser

url_template = 'http://openlibrary.org/authors/{id}/works.json'


# set template url for API call

def get_works(name):
    ol = OpenLibrary()
    author_id = ol.Author.get_olid_by_name(name)

    query_url = url_template.format(id=author_id)  # format API url to include OLID

    resp = requests.get(query_url)  # use requests module to access API
    if resp.ok:
        response = resp.json()  # return json of results if ok
    else:
        return resp.reason  # print reason if not ok

    datalist = response['entries']  # make json data easier to parse through

    num_works = len(datalist)

    author = [name] * num_works  # create list of author name (API call returns 50 results maximum)

    titles = [entry['title'] for entry in datalist]  # create list of titles by parsing through json

    revision = [entry['revision'] for entry in datalist]  # create list of revision number

    key = [entry['key'] for entry in datalist]  # create list of keys

    publish_date = []  # initialise list for publish date (not all entries have one)
    for entry in datalist:
        if 'first_publish_date' in entry.keys():
            publish_date.append(entry['first_publish_date'])  # if publish date exists, append to list
        else:
            publish_date.append(None)  # if publish date does not exist, append 'N/A' to list

    subjects = []  # initialise subject list
    for entry in datalist:
        if 'subjects' in entry.keys():
            subjects.append(entry['subjects'])  # if subjects exist, append to list
        else:
            subjects.append('N/A')  # if subjects do not exist, append 'N/A' to list

    places = []  # initialise places list
    for entry in datalist:
        if 'subject_places' in entry.keys():
            places.append(entry['subject_places'])  # if places exist, append to list
        else:
            places.append('N/A')  # if places do not exist, append 'N/A' to list

    characters = []  # initialise character list
    for entry in datalist:
        if 'subject_people' in entry.keys():
            characters.append(entry['subject_people'])  # if characters exist, append to list
        else:
            characters.append('N/A')  # if characters do not exist, append 'N/A' to list

    data = pd.DataFrame(
        data={"Author": author, "Title": titles, "Revision": revision, "Key": key, "Publish Date": publish_date,
              "Subjects": subjects, "Characters": characters, "Places": places})
    # create pandas dataframe of lists, makes it easy to save as csv file
    '''
    name_list = name.split()
    name = name_list[-1]

    data.to_csv(name+".csv", sep=',', index = False)
    #save author's data as csv file

    with open(name+'.json', 'w') as OUTF:
        json.dump(response, OUTF)
	#create json dump of all returned data
	'''

    output = data.to_json(orient='records')

    return output

def save_works(works_json):
    try:
        author_name = works_json[0]["Author"]
        author, created = Author.objects.get_or_create(name = author_name)
        for work in works_json:
            subjects = [] if work["Subjects"]=="N/A" else [Subject(subject_name=name) for name in work["Subjects"]]
            subjects_new = []
            for subject in subjects:
                if subject not in Subject.objects.filter(subject_name=subject.subject_name):
                    subject.save()
                subjects_new.append(subject)
            characters = [] if work["Characters"]=="N/A" else [Character(character_name=name) for name in work["Characters"]]
            for character in characters:
                if character not in Character.objects.filter(character_name=character.character_name):
                    character.save()
            places = [] if work["Places"]=="N/A" else [Place(place_name=name) for name in work["Places"]]
            for place in places:
                if place not in Place.objects.filter(place_name=place.place_name):
                    place.save()
            date = parser.parse(work["Publish Date"]) if work["Publish Date"] != None else None
            if not Resource.objects.filter(title=work["Title"],author=author,revision=work["Revision"]):
                book = Resource(
                                title=work["Title"],
                                author=author,
                                revision=work["Revision"],
                                publish_date=date,
                                quantity=1,
                                location=None)
                #return book.title, book.author, book.revision, book.publish_date, book.quantity, book.location
                book.save()
                #return "yay"
                ''' # Can't auto add subjects, characters or places at the moment
                for subject in subjects_new:
                    book.subjects.add(subject)
                for character in characters:
                    book.characters.add(character)
                    for place in places:
                        book.places.add(place)
                '''
        return 1
    except:
        return -1