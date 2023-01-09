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
    #Distribution of teams into 4 groups based on their levels
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

