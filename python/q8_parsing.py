# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

best_team = None
min_diff = None
with open("/Users/christieli/Desktop/pre-work/dsp/python/football.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    team = row["Team"]
    goals = int(row["Goals"])
    goals_allowed = int(row["Goals Allowed"])
    diff = abs(goals - goals_allowed)
    if min_diff is None or diff < min_diff:
      min_diff = diff
      best_team = team

print best_team
