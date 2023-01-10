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
from random import shuffle

_16_teams_league_list = []

# a


class Groups:
    def __init__(self, group_teams):
        self.group_teams = group_teams
        self.group_games = [[c[0], c[1]] for c in combinations(self.group_teams, 2)]
        self.group_points = [0] * len(self.group_teams)

    def result(self):
        # Assume user input format: score_1,score_2
        for match in self.group_games:
            match_result = input('Enter match result of ' + match[0] + ' vs ' + match[1] + ': ')
            score1, score2 = match_result.split(',')
            match += [int(score1), int(score2)]  # Now group_games = [ [team1, team2, score1, score2], ..]

    def selection(self):
        global _16_teams_league_list
        for match in self.group_games:
            team_1, team_2, score_1, score_2 = match
            if score_1 > score_2:
                self.group_points[self.group_teams.index(team_1)] += 3
            elif score_1 < score_2:
                self.group_points[self.group_teams.index(team_2)] += 3
            else:
                self.group_points[self.group_teams.index(team_1)] += 1
                self.group_points[self.group_teams.index(team_2)] += 1

        teams = sorted(self.group_teams, key=lambda x: self.group_points[x], reverse=True)
        _16_teams_league_list += teams[:2]

# b


League = {}
for i in range(32):
    # Assume format: team_name,team_strength
    line = input('Enter team and its strength:')
    team_name, team_strength = line.split(',')
    League[team_name] = int(team_strength)

sorted_teams = sorted(League, key=lambda x: League[x], reverse=True)

# c

classification = [sorted_teams[i:i+8] for i in range(0, 32, 8)]
groups = []
for i in range(8):
    selected_teams = []
    for j in range(4):
        shuffle(classification[j])
        selected_teams.append(classification[j].pop(0))  # Take a team and remove it
    groups.append(Groups(selected_teams))

# d

for group in groups:
    group.result()  # use class function to get result for each group game

# e
for group in groups:
    group.selection()
print(_16_teams_league_list)
