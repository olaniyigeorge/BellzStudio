from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import timedelta, datetime
from datetime import date as realDate
import time

from django.urls import reverse

from notes.forms import NoteForm
from .models import Note, IdeaTag
# Create your views here.





def index(request):
    # Date Selector
    week = []
    d = realDate.today()
    for x in range(-3, 4):
        week.append(d + timedelta(days=x))

    # Tags
    tags = IdeaTag.objects.all()

    # Notes
    notes = Note.objects.all()


    return render(request, 'notes/all-notes.html', {'week': week, 'notes': notes, 'tags': tags})

def NewNote(request):
    '''
    On GET: This view returns the entry form page on get
    On POST: calls the validate_entry(entry), if valid, calls parse_entry(entry) then save entry.

    '''
    if request.method == "POST":
        # Get authenticated user
        user = request.user


        # Get submited entry text
        ti = request.POST['entry_text']
        entry_text = request.POST['entry_text']
        entry_text = request.POST['entry_text']


        


        # Create new entry instance
        new_entry = Note.objects.create(text=entry_text)

        # Save new entry instance
        new_entry.save()

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
    print("Request: ", request)

    # Date Selector
    week = []
    d = realDate.today()
    for x in range(-3, 4):
        week.append(d + timedelta(days=x))

    notes = Note.objects.filter(written_at__date=date)   
    notes_tags = list()
    # notes_tags = set(notes_tags)
    # notes_tags = list(notes_tags)

    print("\n------------\n")
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


