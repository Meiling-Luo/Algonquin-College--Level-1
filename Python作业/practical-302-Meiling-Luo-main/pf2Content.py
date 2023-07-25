wc22 = {
    "A":["Ecuador","Netherlands","Qatar","Senegal"],
    "B":["England","Iran","USA","Wales"],
    "C":["Argentina","Mexico","Poland","Saudi Arabia"],
    "D":["Australia","Denmark","France","Tunisia"],
    "E":["Costa Rica","Germany","Japan","Spain"],
    "F":["Belgium","Cnada","Croatia","Morocco"],
    "G":["Brazil","Cameroon","Serbia","Switzerland"],
    "H":["Ghana","Portugal","Korea Republic","Uruguay"],
}

#Format of the list
#[Number of matches played, Number of Wins, Number of Draws, Number of Losses, Number of goals scored, Number of goals conceded, Goal Difference, Number of points]
#In short
#[MP,W,D,L,GF,GA,GD=GF-GA,Pts]
gameResults = {
    "Ecuador":[0,0,0,0,0,0,0,0],
    "Netherlands":[0,0,0,0,0,0,0,0],
    "Qatar":[0,0,0,0,0,0,0,0],
    "Senegal":[0,0,0,0,0,0,0,0],
    "England":[0,0,0,0,0,0,0,0],
    "Iran":[0,0,0,0,0,0,0,0],
    "USA":[0,0,0,0,0,0,0,0],
    "Wales":[0,0,0,0,0,0,0,0],
    "Argentina":[0,0,0,0,0,0,0,0],
    "Mexico":[0,0,0,0,0,0,0,0],
    "Poland":[0,0,0,0,0,0,0,0],
    "Saudi Arabia":[0,0,0,0,0,0,0,0],
    "Australia":[0,0,0,0,0,0,0,0],
    "Denmark":[0,0,0,0,0,0,0,0],
    "France":[0,0,0,0,0,0,0,0],
    "Tunisia":[0,0,0,0,0,0,0,0],
    "Costa Rica":[0,0,0,0,0,0,0,0],
    "Germany":[0,0,0,0,0,0,0,0],
    "Japan":[0,0,0,0,0,0,0,0],
    "Spain":[0,0,0,0,0,0,0,0],
    "Belgium":[0,0,0,0,0,0,0,0],
    "Canada":[0,0,0,0,0,0,0,0],
    "Croatia":[0,0,0,0,0,0,0,0],
    "Morocco":[0,0,0,0,0,0,0,0],
    "Brazil":[0,0,0,0,0,0,0,0],
    "Cameroon":[0,0,0,0,0,0,0,0],
    "Serbia":[0,0,0,0,0,0,0,0],
    "Switzerland":[0,0,0,0,0,0,0,0],
    "Ghana":[0,0,0,0,0,0,0,0],
    "Portugal":[0,0,0,0,0,0,0,0],
    "Korea Republic":[0,0,0,0,0,0,0,0],
    "Uruguay":[0,0,0,0,0,0,0,0],
}

#What is a python statement that prints Morocco on the screen (use the dictionary wc22)
print(wc22['F'][3])

#What is a python statement that prints the number of points of Denmark (use the dictionary gameResults)
print(gameResults['Denmark'][7])

#What is a python statement that prints the number of losses of Qatar (use the dictionary wc22)
print(gameResults['Qatar'][3])

#What is a python statement that prints the Goal difference for Uruguay (use the dictionary gameResults)
print(gameResults['Uruguay'][6])


#What is a python statement that fixes the typo in group F, replacing Cnada with Canada (use the dictionary wc22)
wc22["F"][1] = "Canada"



#Write the code of the function printGroup
#This function creates and returns a string which is the  html table that displays the group name and each member of the group name
#if name is not a valid group, an error message is displayed
#
#Example string returned if name="A":<table><tr><th>Group A</th></tr><tr><td>Ecuador</td></tr><tr><td>Netherlands</td></tr><tr><td>Qatar</td></tr><tr><td>Senegal</td></tr></table>

def printGroup(name):
    if name not in wc22:
        return "Group name not exist"
    group = wc22[name]
    result = "<table><tr><th>Group {}</th></tr>".format(name)
    for country in group:
        result += "<tr><td>{}</td></tr>".format(country)
    result += "</table>"

    return result

#Write the code of the function testprintGroup
#This function tests the function printGroup:
# - prompts the user for a group name
# - calls the function to create the html string
# - Saves the string into a file name.html where name is the group name: A to G
# - function starts again until the user presses "N"
def testprintGroup():
    while True:
        try:
            group = input('Input a Group Name From A-G, N to exit')
            if group.upper() == "N":
                break
            elif group.upper() in wc22:
                html_string = printGroup(group)
                f = open("{}.html".format(group), "w")
                f.write(html_string)
                f.close()
            else:
                raise ValueError("Invalid input")

        except:
            print('Please enter a valid group name')


#Write the code of the function saveGame
#
#Note that knowing the function signature, you may start doing the next function and come back to this one later
#
#This function receives the result of the game as a string with the following format
#Group, Country1: GoalsScored, Country2: GoalsScored
#Example:
#A, Qatar:0, Ecuador:2"
# the function parses the input (hint: use split)
# then updates the dictionary dResult
#[Number of matches played, Number of Wins, Number of Draws, Number of Losses, Number of goals scored, Number of goals conceded, Goal Difference, Number of points]
#
#As an example if gameResult is "A, Qatar:0, Ecuador:2"
#For Qatar:
#   Game Played is incremented by 1
#   Goal against is incremented by 2
#   Loss is incremented by 1
#
#For Ecuador:
#   Game Played is incremented by 1
#   Goal For is incremented by 2
#   Win is incremented by 1
#   Points is incremented by 3


#convert gameResult to a list using split
#Extract the first country name and number of goals scored using split
# Extract the second country name and number of goals scored using split
def saveGame(gameResult,dResult):
    lstGameResult = gameResult.split(",")
    country1 = listGameResult[1].split(':')[0]
    country2 = gameResultList[2].split(':')[0]
    countryScore1 = lstGameResult[1].split(':')[1]
    countryScore2 = listGameResult[2].split(':')[1]


    # then updates the dictionary dResult
    # [Number of matches played, Number of Wins, Number of Draws, Number of Losses, Number of goals scored, Number of goals conceded, Goal Difference, Number of points]
    # [Mp,W,D,L,GF,GA,GD,Pts]
    #if second country wins
    #update dResult with appropriate values:
    #first country: l+=1 GF+=s1 GA+=s2  MP+=1 GD+=s1-s2
    #second country: w+=1 GF+=s2 GA+=s1 MP+=1 GD+=s1-s2 pts+=3


    #if first country wins
    #update dResult with appropriate values:
    #first country: W +=1 GF+=s1 GA+=s2 Pts+=3 Mp+=1 GD+=s1-s2
    #second country: L+=1 GF+=s2 GA+=s1 Mp+=1 GD+=s1-s2

 

    #if draw
    #update dResult with appropriate values:
    #first country d+=1 GF+=s1 GA+=s2  MP+=1 GD+=s1-s2 pts+=1
    #second country: d+=1 GF+=s2 GA+=s1 MP+=1 GD+=s1-s2 pts+=1




#Write the code of the function readFileResults
#This function receives the file with game results
#It then populates the dictionary dR
#This function makes use of the saveGame function created previously
def readFileResults(fName, dR):
    with open(fName, "r") as f:
        for line in f:
            saveGame(line, dR)

        return

#Write the code of the function printgameResults
#This function prints on the screen a html table row that contains
#the current results of the country str
#In order the table row displays:
#Match played | Wins | Losses | Draws | Goals For | Goals Against | Goals differential | Points
#
#Example output on screen
#<tr><td>1/td><td>1/td><td>0/td><td>0/td><td>1/td><td>0/td><td>1/td><td>3/td></tr>
def printgameResults(str, dR):
    results = dR[str]
    row = "<tr><td>{}</td><td>"
    return row
#Write the code of the function printResults
#This function prints on screen a html table that displays the results
#of all the countries in the group.
#It makes calls to the function printgameResults

def printResults(group,dR,dG):
    lstCountry = dG[group]
    table = "<table><tr><th> Group {}</th></tr>".format(group)
    for team in lstCountry:
        table += printResults(team, dR)
    table += "</table>"
    return table

#This code should work without any modification
printGroup("B")
readFile("results.txt",gameResults)
printgameResults("Tunisia",gameResults["Tunisia"])
printResults("B",gameResults,wc22)



