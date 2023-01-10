"""
league process is The FIFA world cup supposed to go through many phases. One of them is the world cup group league
which is explained in the following lines.
According to FIFA classification a collection of 32 teams will contribute the league.
Each team is assigned an evaluation level, and the teams are sorted in ascending order due to that level.
They will then be distributed into 8 groups. Each group is composed of 4 teams. Each group will play 6 games.
Accounts of teams will count up three points in case of winning, one point in case of draw, and zero in case of loosing.
Accordingly, two teams of each group will qualify for the 16_teams league (16). Write Python code to do the following:
a) Create a Python class "Groups" that contain the following attributes and functions:
- A list "group_teams" of the teams in a group.
- A list "group_games" of games that will be played by the groups teams with the results of the games associated
to the game.
- A list "group_points" of points collected by teams in a group.
- A function "results" to read the results of each game from the keyboard and store them in the suitable list.
- A function "selection" to sort teams in a group and select the two qualified teams and store them in a global list
"16_teams_league_list".
b) Read the names of the 32 teams with associated levels in python dictionary "League", sort them accordingly.
c) Create a list of objects "groups" of type "Groups" Then randomly distribute the first 8 teams to 8 object groups in
the list. Afterwards, distribute the second 8 teams the same way, and so on.
d) Read the results of the games from the keyboard and store them in their suitable places.
e) Select the qualified teams, store them into "16_teams_league" list and print them.
"""
from itertools import combinations
import random


class Groups:
    def __init__(self, group_teams):
        self.group_teams = group_teams
        self.group_games = []
        self.group_points = {}
        for team in group_teams:
            self.group_points[team] = 0

    def results(self):
        # Read the results of each game from the keyboard and store them in the suitable list

        # for generating matches you can use combinations instead
        # self.group_games = [[c[0], c[1]] for c in combinations(self.group_teams, 2)]

        for i in range(4):
            for j in range(i+1, 4):
                # Generate a random result for the game between the two teams
                team1, team2 = self.group_teams[i], self.group_teams[j]
                score1, score2 = random.randint(0, 7), random.randint(0, 7)
                
                if score1 > score2:
                    self.group_points[team1] += 3
                    
                elif score2 > score1:
                    self.group_points[team2] += 3
                    
                else:
                    self.group_points[team1] += 1
                    self.group_points[team2] += 1

    def selection(self):
        # Sort the teams in the group by their points
        self.group_teams.sort(key=lambda x: self.group_points[x], reverse=True)
        # Select the top two teams as the qualified teams
        qualified_teams = self.group_teams[:2]
        # Store the qualified teams in the global list "16_teams_league_list"16
        _16_teams_league_list.extend(qualified_teams)


# Read the names of the 32 teams with associated levels in python dictionary "League"
League = {}

for i in range(32):
    team = "Team " + str(i+1)
    rate = random.randint(1, 100)
    League[team] = rate

# Sort the teams in ascending order of their levels
sorted_teams = sorted(League, key=League.get)
# Create a list of objects "groups" of type "Groups"
groups = []
Classification = []
for i in range(4):
    # Distribution of teams into 4 groups based on their levels
    group = random.sample(sorted_teams[i * 8:(i + 1) * 8], 8)
    Classification.append(group)


for i in range(8):
    # Randomly select the teams for the group
    group_teams = []
    for j in range(4):
        team = random.choice(Classification[j])
        group_teams.append(team)
        Classification[j].remove(team)
    group = Groups(group_teams)
    groups.append(group)


# Read the results of the games and store them in their suitable places
for group in groups:
    group.results()

# Create the global list "16_teams_league_list" to store the qualified teams16
_16_teams_league_list = []

# Select the qualified teams and store them in the "16_teams_league_list"
for group in groups:
    group.selection()

# Print the qualified teams
print(_16_teams_league_list)
