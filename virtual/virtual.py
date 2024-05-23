import itertools
import random


print("Virtual football")

# Train ---- REINFORCEMENT LEARNING
# for round in range(380)         --- assuming no of rounds per season = 380
#   Set round (round) fixtures
#   Set odds for fixtures under(1,X,2, O/U(0.5,1.5,2.5,3.5,4.5,5.5))
#   Predict outcomes
#   Set actual outcomes



# Play ---- REINFORCEMENT LEARNING
# for round in range(380)         --- assuming no of rounds per season = 380
#   Set(input) round (round) fixtures
#   Set(input) odds for fixtures under(1,X,2, O/U(0.5,1.5,2.5,3.5,4.5,5.5))
#   Predict outcomes
#   Set actual outcomes


class FootballLeague():
    def __init__(self, teams=[
                            'ARS', 'AST', 'BHA', 'BOU',  
                            'BRE', 'BUR', 'CHE', 'CRY', 
                            'EVE', 'FOR', 'FUL', 'LIV', 
                            'LUT', 'MCI', 'MUN', 'NEW', 
                            'SHU', 'TOT', 'WHU', 'WOL'
                        ]
        ):
        """
        Initialize the football league.
        Each league has:
            - teams: a list of team names
            - standings: a list of lists to keep track of each team's standings in each round
            - matches_played: a list to keep track of matches played
            - fixtures: a list to keep track of fixture list for each round
        """
        self.teams = teams
        self.standings = [[] for _ in range(len(teams))]
        self.matches_played = []
        self.fixtures = []

    def setup_fixture(self):
        """
        Generate the fixture list for the league.
        """
        # Generate all possible combinations of teams for matches
        matches = list(itertools.combinations(self.teams, 2))
        print(len(matches))
        for m in matches:
            print(m)
            print()

        # Make empty round list in fixtures
        print(round((len(self.teams)/2)))
        for r in range(round(len(matches)/round((len(self.teams)/2)))):
            self.fixtures.append([])
        
        print(self.fixtures)
        print(len(self.fixtures))
        # Randomly shuffle the matches to create randomness in the fixture list
        random.shuffle(matches)

        # Group matches into rounds
        num_rounds = len(self.teams) - 1  # Number of rounds needed to ensure each team plays against every other team once
        matches_per_round = len(matches) // num_rounds  # Number of matches per round
        rounds = [matches[i:i+matches_per_round] for i in range(0, len(matches), matches_per_round)]

        # Create fixtures for each round by alternating home and away matches
        for i, round_matches in enumerate(rounds):
            round_fixtures = []
            for match in round_matches:
                home_team, away_team = match
                if i % 2 == 0:
                    round_fixtures.append((home_team, away_team))
                else:
                    round_fixtures.append((away_team, home_team))
            self.fixtures.append(round_fixtures)

    def play_match(self, home_team, away_team):
        """
        Simulate a match between two teams.
        """
        home_goals = random.randint(0, 5)  # Simulate random goals for the home team
        away_goals = random.randint(0, 5)  # Simulate random goals for the away team

        # Update standings based on match result
        if home_goals > away_goals:
            self.standings[self.teams.index(home_team)].append({3: home_team})
            self.standings[self.teams.index(away_team)].append({0: away_team})
        elif home_goals < away_goals:
            self.standings[self.teams.index(home_team)].append({0: home_team})
            self.standings[self.teams.index(away_team)].append({3: away_team})
        else:
            self.standings[self.teams.index(home_team)].append({1: home_team})
            self.standings[self.teams.index(away_team)].append({1: away_team})
        
        # Record the match in matches_played
        self.matches_played.append((home_team, away_team, home_goals, away_goals))

        # Return scores dictionary
        scores = {
            home_team: home_goals,
            away_team: away_goals
        }
        return scores

    def generate_odds(self):
        """
        Generate odds for each match.
        """
        odds = {}
        for round_fixtures in self.fixtures:
            for fixture in round_fixtures:
                home_team, away_team = fixture
                home_win_odds = random.uniform(1.0, 3.0)  # Random home win odds between 1.0 and 3.0
                draw_odds = random.uniform(2.0, 4.0)  # Random draw odds between 2.0 and 4⬤