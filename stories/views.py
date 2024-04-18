from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime

from django.urls import reverse
from .inspo import demo_craty_inspirations
from .models import Election, Party, Voter



def index(request):



    return render(request, "stories/index.html", {})



def DemoCratyIndex(request):
    inspos = demo_craty_inspirations
    return render(request, "stories/dc_index.html", {'inspos': inspos})

def DemoCratyDemo(request):
    elections = Election.objects.all()

    return render(request, "stories/dc_home.html", {'elections': elections})


def ElectionDetails(request, id):
    user = request.user
    message = ""
    reg= False
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
    print()

    return render(request, 
                  "stories/election_details.html", 
                    {
                        'election': election, 
                        'time_diff': (election.date - now).days,
                        'user': request.user,
                        'voter': voter,
                        'message': message,
                        "vote": True,
                        'user_is_registered': reg

                    }    
                )




def ElectionRegistration(request):
    pass


def Vote(request, id):
    if request.method == "POST":
        try:
            selected_party = request.POST['party_choice']
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('poll:home')))
        
        print("Selected Party ID: ", selected_party)
        print("choice_id: ", Party.objects.get(id=selected_party))
        print("Election id: ", Election.objects.get(pk=id))

        # Create Vote instance with VOTER, PARTY AND ELECTION attrs
        
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


