from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import timedelta, datetime
from datetime import date as realDate
import time
import uuid 
from django.urls import reverse

from notes.forms import NoteForm
from .models import Note, IdeaTag, NotePrivacy, Reader
# Create your views here.





def index(request):
    errors = {}
    print("Request user : ", request.user)
    user= request.user

    if not user.is_authenticated:
        user_first = ''
    else:
        if len(user.first_name) > 1:
            user_first = user.first_name[0]
        else:
            user_first = f"{user}"[0]
    # Date Selector
    week = []
    d = realDate.today()
    for x in range(-3, 4):
        week.append(d + timedelta(days=x))
    # Tags
    tags = IdeaTag.objects.all()
    try:
        tag_param = request.GET['tag']
        # print("Tag Param: ", request.GET['tag'])
    except Exception as e:
        tag_param = None
        # print("Error: ", e)
    
    if tag_param:
        try:
            tag_param = f"#{tag_param}"
            tag_param = IdeaTag.objects.get(name=tag_param)
        except Exception as e:
            print("No tag: ", e)
            tag_param = None
    
    
    # Fetch notes based n user's network
    # If request user is autheicted
    if not request.user.is_authenticated:
        notes = Note.objects.filter(privacy_level__gte= 4)
        return render(request, 'notes/all-notes.html', {'week': week, 'notes': notes, 'tags': tags, 'errors': errors})


    # Get auth'd user reader profile
    try:
        reader_profile = Reader.objects.get(user=request.user)
    except Exception as e:
        # Couldn't get reader profile
        print(e)
        reader_profile = None
    if reader_profile == None:
        print(f"{request.user} is auth bu no reader profile assuming the" )
        if request.user.is_staff:
            notes = Note.objects.all()
        
    else:
        reader = reader_profile
        print("This Reader: ", reader)
        
        subscription = reader.subscription_level
        print("Subscription: ", subscription)
        print("Leve: ", subscription.level, "ID", subscription.id)

        notes = Note.objects.filter(privacy_level__level__gte=subscription.level)
        




    print("Result length: ", len(notes))
    #errors['invalid_idea_format'] = "Invalid idea format"

    print(errors)

    return render(request, 'notes/all-notes.html', {'week': week, "user_first": user_first, 'notes': notes, 'tags': tags, 'errors': errors})

def NewNote(request):
    '''
    On GET: This view returns the entry form page on get
    On POST: calls the validate_entry(entry), if valid, calls parse_entry(entry) then save entry.

    '''
    if request.method == "POST":
        # Get authenticated user
        user = request.user


        # Get submited entry text
        print("Form: ", request.POST)
        d = dict(request.POST)
        print("Dict form: ", d)
        title = d['title'][0].title()
        print("Title: ", title)
        text = d['text'][0]
        print("Text: ", text)
        tags = d['tags']
        print("Tags: ", tags)
        privacy_level = d['privacy_level'][0]   # int(d['privacy_level'][0])+1
        print("Privacy Level: ", privacy_level)


        # # # Create new note instance
        try:
            pl = NotePrivacy.objects.get(level=privacy_level)
            new_note = Note.objects.create(title=title, text=text, privacy_level=pl)
            new_note.tags.set(tags)

        except Exception as e:
            print("Error: ", e)
            return HttpResponseRedirect(reverse("notes:index"))

        # # # Save new entry instance
        # new_note.save()

        # Redirect back home
        return HttpResponseRedirect(reverse("notes:index"))
    
    write_form_note = NoteForm()
    return render(request, 'notes/write.html', {'form': write_form_note})

def NewIdea(request):
    if request.method == "POST":

        idea_name = request.POST['idea_name']
        errors ={}
        errors['invalid_idea_format'] = "Invalid idea format"
        if len(idea_name) < 2:
            return HttpResponseRedirect(reverse("notes:index", 
                                                args=(), kwargs=()
                                        ))
        try:
            IdeaTag.objects.get_or_create(name=idea_name)
        except Exception as e:
            return HttpResponse("Error creating tag")


        return HttpResponseRedirect(reverse("notes:index"))

def NoteDate(request, date):
    print("Date: ", date)
    try:
        tag_param = request.GET['tag']
        print("Tag Param: ", request.GET['tag'])
    except Exception as e:
        tag = None
        print("Error: ", e)


    # Date Selector  content_params path
    week = []
    d = realDate.today()
    for x in range(-3, 4):
        week.append(d + timedelta(days=x))

    notes = Note.objects.filter(written_at__date=date)   
    notes_tags = list()
    # notes_tags = set(notes_tags)
    # notes_tags = list(notes_tags)

    if tag == None:
        for x in notes:
            for i in x.tags.values():
                notes_tags.append({
                                'id': dict(i)['id'],
                                'name': dict(i)['name']
                            })

    return render(request, 'notes/notes-date.html', 
                  {
                    'week': week, 
                    "day_notes": notes,
                    "tags": notes_tags
                })

def IdeaNotes(request, slug):
    try:
        idea = IdeaTag.objects.get(slug=slug)
    except:
        idea = IdeaTag.objects.none()
    
    # Get auth'd user reader profile
    try:
        reader_profile = Reader.objects.get(user=request.user)
    except Exception as e:
        # Couldn't get reader profile
        print(e)
        reader_profile = None
    if reader_profile == None:
        print(f"{request.user} is auth bu no reader profile assuming the" )
        if request.user.is_staff:
            notes = Note.objects.all()
        else:
            idea_notes = idea.my_notes()
            notes = idea_notes.objects.filter(privacy_level__level__gte=5)    
    else:
        reader = reader_profile
        print("This Reader: ", reader)
        
        subscription = reader.subscription_level
        print("Subscription: ", subscription)
        print("Level: ", subscription.level, "ID", subscription.id)
        idea_notes = idea.my_notes()
        notes = idea_notes.objects.filter(privacy_level__level__gte=subscription.level)
        

    
    count = idea.my_notes().count()
    return render(request, 'notes/idea-notes.html', {'idea': idea, 'idea_notes': notes, 'idea_notes_count': count})

def NoteView(request, slug):
    try:
        note = Note.objects.get(slug=slug)
    except:
        note = None
    
    return render(request, "notes/note.html", {"note": note})

def Search(request):
    query = request.GET['query'].lower()
    print("Search Query: ", query)
    note_results = []
    notes = Note.objects.all()
    for note in notes:
        if query.lower() in note.text.lower():
            note_results.append(note)

    print(note_results)

    idea_results = []
    ideas = IdeaTag.objects.all()
    for idea in ideas:
        if query.lower() in idea.name.lower():
            idea_results.append(idea)

    print(idea_results)

    return render(request, "notes/search.html", {

        "note_results": note_results,
        "idea_results": idea_results,
        "results_length": len(note_results) + len(idea_results)

        })

def networks(request):

    networks = NotePrivacy.objects.all()
    
    return render(request, "notes/monitize/join-network.html", {"networks": networks})

def network(request, level):
    networks = NotePrivacy.objects.all()
    try:
        network = NotePrivacy.objects.get(level=level)
    except:
        network = None
    
    if network:
        return render(request, "notes/monitize/network.html", {"network": network, "networks": networks})


def subscribe(request):

    if request.method == "POST":
        pass
    
    pass