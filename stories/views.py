import os
import uu
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
import markdown

from BellzStudio.settings import BASE_DIR

from django.urls import reverse
from .inspo import demo_craty_inspirations
from .models import Election, Party, Story, Voter, Vote
from notes.models import IdeaTag


from django.core.files.storage import default_storage

def index(request):
    user = request.user

    stories = Story.objects.all()
    return render(
                    request, 
                    "stories/dev-stories.html", 
                    {
                        "user": user, 
                        "stories": stories
                    }
                )

def story(request, id):
    print("Story id: ", id)
    story = Story.objects.get(id=id)
    print(story)
    mdentry =  story.content.url #util.get_entry(title)
    
    try:
        # f = f"{BASE_DIR}{story.content.url}"

        f = default_storage.open(f"{BASE_DIR}{story.content.url}")
        print("F: ", f)
        #f = default_storage.open(story.content.url)
        c = f.read().decode("utf-8")
        md = markdown.Markdown(extensions=["fenced_code"])
        cc=  markdown.markdown(c)
        cc = md.convert(story.content)
        print("CC: ", cc)
        print("C: ", c)
    except Exception as e:
        print("File not found: ", e)
    
    print(f"Content: ", mdentry)
    converted_content = markdown.markdown(mdentry)
    print(f"Converted entry: ", c)
    return render(request, "stories/story.html", {"story": story, "content": cc})


def DemoCratyIndex(request):
    inspo = demo_craty_inspirations
    democraty_idea = IdeaTag.objects.get(name="#DemoCraty")
    return render(request, "stories/dc_index.html", {'insp': inspo, "DemoCraty": democraty_idea})

def DemoCratyDemo(request):
    elections = Election.objects.all()

    return render(request, "stories/dc_home.html", {'elections': elections})

def ElectionDetails(request, id):
    user = request.user
    message = ""
    reg= False
    voted = False

    try:
        election = Election.objects.get(id=id)
    except:
        election = Election.objects.none()

    election_date = datetime.datetime.strptime("2024-04-24", "%Y-%m-%d").date()
    now = datetime.date.today()

    print("Now: ", now)
    print("Election date: ", election.date)

    print()
    print("Diff: ", (election.date - now).days)
    if user.is_authenticated:
        try:
            voter, created = Voter.objects.get_or_create(person=user)
            reg = voter.election_registrations.filter(pk=election.id).exists()
            print("Reg: ", reg)
        except Exception as e:
            print("Exception: ", e)
            voter = None
            message = "This user can't be a voter"
    else:
        voter = None
        message = "You have to sign in to participate in the electoral processes"

    print("Voter: ",  voter)
    # Check if user has registered for this election
    try:
        pass # print("Reg:", reg)
    except:
        pass

    
    # Check if user has voted
    if voter:
        try:
            voted = Vote.objects.filter(voter=voter, election=election).exists()
            print("This user has voted: ", voted)
        except Exception as e:
            print("Voted Exception: ", e)
            voted = False

    # Get votes in this election
    results = {}    
    votes = Vote.objects.filter(election=id).count
    for party in election.parties.values():
        results[f"{party['name']}_result"] = Vote.objects.filter(election=id, party=party['id']).count

    return render(request, "stories/election_details.html", 
                    {
                    'election': election, 
                    'time_diff': (election.date - now).days,
                    'user': request.user,
                    'voter': voter,
                    'message': message,
                    "vote": True,
                    'user_is_registered': reg, 
                    "voted": voted,
                    "votes": votes,
                    "results": results

                } 
                )

def ElectionRegistration(request, id):
    
    if request.method == "POST":
        voter_id = request.POST['voter']
        
        try: 
            voter = Voter.objects.get(id=voter_id)
            election = Election.objects.get(id=id)
        except Exception as e:
            print("Error: ", e)

        # Add user to registered voters --- Redirect to reg page if more actions need to be done
        try:
            election.registered_voters.add(voter_id)
        except Exception as e:
            print("Registration error: ", e)

        return HttpResponseRedirect(
                reverse(
                        "stories:election_details",args=(id,)
                        )
        )


    else:
        return HttpResponseRedirect(
                reverse(
                        "stories:election_details",args=(id,)
                        )
        )


def VoteView(request, id):
    if request.method == "POST":
        try:
            selected_party = request.POST['party_choice']
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse(
                        "stories:election_details",args=(id,)
                        )))
        print("User: ", request.user)
        try:
            voter = Voter.objects.get(person=request.user)
        except Exception as e:
            print("Error: ", e)
            return HttpResponseRedirect(
                reverse(
                        "stories:election_details",args=(id,)
                        )
        )
        party = Party.objects.get(id=selected_party)
        election = Election.objects.get(pk=id)
        print("Voter: ", voter)
        print("Selected Party ID: ", selected_party)
        print("choice_id: ", party)
        print("Election id: ", election)

        # Create Vote instance with VOTER, PARTY AND ELECTION attrs
        v= Vote(voter=voter, party=party, election=election)
        v.save()
        return HttpResponseRedirect(
                reverse(
                        "stories:election_details",args=(id,)
                        )
        )
    
    else:
        return HttpResponseRedirect(
                reverse(
                        "stories:election_details",args=(id,)
                        )
        )


