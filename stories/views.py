from django.shortcuts import render
from datetime import datetime
from .inspo import demo_craty_inspirations
from .models import Election



def index(request):



    return render(request, "stories/index.html", {})



def DemoCratyIndex(request):
    inspos = demo_craty_inspirations
    return render(request, "stories/dc_index.html", {'inspos': inspos})

def DemoCratyDemo(request):
    elections = Election.objects.all()

    return render(request, "stories/dc_home.html", {'elections': elections})


def ElectionDetails(request, id):
    try:
        election = Election.objects.get(id=id)
    except:
        election = Election.objects.none()

    now = datetime.now().date()

    print("Now: ", now)
    print("Election date: ", election.date)

    print()
    print("Diff: ", election.date - now)
    print()

    return render(request, "stories/election_details.html", {'election': election, 'time_diff': election.date - now})






