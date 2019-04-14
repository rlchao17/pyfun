"""
When two swim teams compete against each other, teams score points 
based on the swimmer placement in each event.  For our scenario, 
Team A is swimming against Team B.  Your job is to calculate the 
placement and team points for each team in the 50 Yard Freestyle 
event and the 100 yard Freestyle, then display the results and 
points for each team. There can be anywhere from 1 to 6 swimmers in an 
event. A team can have a maximum of 3 swimmers in an event. 
There will be no ties in any race.

Teams Points:
6 points – 1st Place
4 points – 2nd Place
3 Points – 3rd Place
2 Points – 4th Place
1 Points – 5th Place

Input
List of 1 - 6 times for the 50 yard freestyle and the 100 yard freestyle. 
The suffix will designate the team.

free50Yards  = ["23.47 A", "27.53 B", "28.31 A", "42.59 A ", "22.29 B", "22.18 B"]
free100Yards = ["56.39 B", "53.17 A", "49.01 A", "50.23 B ", "52.16 B"]

Output
Each event finish order with the placing.
Team A and Team B total points.

50 Yard Freestyle:  1 22.18, 2 22.29, 3 23.47, 4 27.53, 5 28.31, 6 42.59,
100 Yard Freestyle: 1 49.01, 2 50.23, 3 52.16, 4 53.17, 5 56.39,
Team A, 12 points
Team B, 20 points 

"""

free50Yards  = ["23.47 A", "27.53 B", "28.31 A", "42.59 A ", "22.29 B", "22.18 B"]
free100Yards = ["56.39 B", "53.17 A", "49.01 A", "50.23 B ", "52.16 B"]

place_point = [6,4,3,2,1]

# do a manual bubble sort ,sort by this instead the whole value 
def bubbie_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1,n):
            if float(l[i].split(' ')[0]) > float(l[j].split(' ')[0]):
                l[j],l[i] = l[i],l[j]
    return l

TeamA = 0
TeamB = 0

grades  =  [ "100 A", "99 P", "100", "* 85", "* 100", "72", "60 A", "83" ] 

print('\n50 Yard Freestyle:  ') 
for i,v in enumerate(bubbie_sort(free50Yards)):
    print '{} {},'.format(i+1, v.split(' ')[0]), 
    if  v.split(' ')[1] == 'A' and i < 5:        
        TeamA += place_point[i]
    elif v.split(' ')[1] == 'B' and i < 5: 
        TeamB += place_point[i]

print ('\n100 Yard Freestyle: ')    
for i,v in enumerate(bubbie_sort(free100Yards)):
    print '{} {},'.format(i+1, v.split(' ')[0]),  
    if  v.split(' ')[1] == 'A' and i < 5:        
        TeamA += place_point[i]
    elif v.split(' ')[1] == 'B' and i < 5: 
        TeamB += place_point[i]
    
print('\nTeamA, {} Points'.format(TeamA))   
print('TeamB, {} Points'.format(TeamB))
    
