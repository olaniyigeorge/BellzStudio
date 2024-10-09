from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import timedelta, datetime
from datetime import date as realDate
import time
import uuid 
from django.urls import reverse
from requests import Response
from notes.serializers import IdeaTagSerializer
from notes.paginations import StandardResultsSetPagination
from notes.serializers import NoteSerializer

from notes.forms import NoteForm
from .models import Note, IdeaTag
# Create your views here.

from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer



def index(request):
    # Date Selector
    week = []
    d = realDate.today()
    for x in range(-3, 4):
        week.append(d + timedelta(days=x))

    try:
        tag_param = request.GET['tag']
        print("Tag Param: ", request.GET['tag'])
    except Exception as e:
        tag_param = None
        print("Error: ", e)
    
    if tag_param:
        try:
            tag_param = f"#{tag_param}"
            tag_param = IdeaTag.objects.get(name=tag_param)
        except Exception as e:
            print("No tag: ", e)
            tag_param = None
    
    # Notes
    if tag_param == None:
        notes = Note.objects.all()
    else:
        notes = tag_param.my_notes
    
    

    # Tags
    tags = IdeaTag.objects.all()


    print("Notes: ", notes)

    return render(request, 'notes/all-notes.html', {'week': week, 'notes': notes, 'tags': tags})

class Notes(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = Note.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
                # Date Selector
        week = []
        d = realDate.today()
        for x in range(-3, 4):
            week.append(d + timedelta(days=x))

        tags = IdeaTag.objects.all()
        posts = Note.objects.all()

        return Response({'week': week, 'notes': posts, 'tags': tags}, template_name='notes/all-notes.html')



def NewNote(request):
    '''
    On GET: This view returns the entry form page on get
    On POST: calls the validate_entry(entry), if valid, calls parse_entry(entry) then save entry.

    '''
    if request.method == "POST":
        # Get authenticated user
        user = request.user


        # Get submited entry text
        title = request.POST['title']
        text = request.POST['text']
        tags = request.POST['tags']

        print("title: ", title)
        print("text: ", text)
        print("tags: ", tags)
    
        tags_list = tags.split(',')

        tags_uuid = [uuid.UUID(tag.strip()) for tag in tags_list]
        
        
        print("Tags list: ", len(tags_uuid))
        # # # Create new note instance
        try:
            new_note = Note.objects.create(title=title, text=text)
            new_note.tags.set(tags_uuid)
        except Exception as e:
            print("Error: ", e)
            return HttpResponseRedirect(reverse("notes:index"))

        # # # Save new entry instance
        # new_note.save()

        # Redirect back home
        return HttpResponseRedirect(reverse("notes:index"))

        '''
        submitted_form = AddEntryForm(request.POST)

        if submitted_form.is_valid():
            # Get authenticated user
            user = request.user

            # Create and save entry
            entry_text = submitted_form.cleaned_data["entry_text"]

            # Create entry. Not specifiying the date with make the date datetime.datetime.now() so far t
            new_entry = Entry.objects.create(author=user, text=entry_text)

            # Redirect back to home
        else:
            # If form sn't valid, redirect back to the create entry page and 
            # prepopulate the form with the invalid entry
            return HttpResponseRedirect(reverse("journal:create_entry"))
        
        pass
        '''
    
    write_form_note = NoteForm()
    return render(request, 'notes/write.html', {'form': write_form_note})

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

def IdeaNotes(request, id):
    try:
        idea = IdeaTag.objects.get(id=id)
    except:
        idea = IdeaTag.objects.none()
    
    idea_notes = idea.my_notes()
    return render(request, 'notes/idea-notes.html', {'idea': idea, 'idea_notes': idea_notes})


#    API ---------
class ApiV1Home(generics.ListAPIView):
    queryset = Note.objects.all().order_by("written_at")
    serializer_class = NoteSerializer
    permission_classes = []
    pagination_class = StandardResultsSetPagination
    search_fields = ['title']
