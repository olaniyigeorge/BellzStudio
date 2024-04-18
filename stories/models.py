from django.db import models
import datetime 
from django.utils import timezone
import uuid
from main.models import User



#  ------------ DemoCraty ------------

class Voter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.OneToOneField(User, on_delete=models.CASCADE, related_name='voter_identity')

    def __str__(self):
        return f"{self.person.email}"

class Party(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10, default="PARTY")
    ideology = models.CharField(max_length=550)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.acronym}"



class Election(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    date = models.DateField()
    parties = models.ManyToManyField(Party, blank=True, related_name='elections_participated_in')
    registered_voters = models.ManyToManyField(Voter, blank=True, related_name='election_registrations')

    def registered_voters_no(self):

        return self.registered_voters.count()
    # def conduct_election(self):
    #     if self.validate_election_date():
    #         self.register_voters()
    #     else:
    #         print("Election date is not valid.")

    # def validate_election_date(self):
    #     current_date = timezone.now().date()
    #     if self.date < (current_date - timedelta(weeks=2)):
    #         return True
    #     else:
    #         return False

    # def register_voters(self):
    #     for party in self.parties.all():
    #         for voter in party.voters.all():
    #             if voter.registered:
    #                 self.voting_results.add(voter)
    #             else:
    #                 print(f"{voter.name} is not registered to vote in {self.name}.")

    def vote(self, voter, party):
        if party in self.parties.all() and voter.registered:
            if voter not in self.voting_results.all():
                self.voting_results.add(voter)
                voter.vote(self, party)
            else:
                print(f"{voter.name} has already voted in {self.name}.")
        else:
            print(f"{voter.name} is not eligible to vote in {self.name}.")

    def __str__(self):
        return self.name



class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='voter_votes')
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='election_votes')
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='party_votes')


    time_casted = models.DateTimeField(auto_now_add=True)

