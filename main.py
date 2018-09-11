import random
import itertools

class Player:
    def __init__(self, team):
        namelist=["Jamie Seegmiller","Deshawn Ferron","Davis Cranford","Erik Levinson" ,"Richie Mcgown","Elvis Cheng","Edgar Busey"]
        countrylist=["England","Germany","France","Spain"]
        #teamlist = ["Liverpool", "Chelsea","Arsenal"]
        self.name = random.choice(namelist)
        self.team = team
        self.skill = random.randrange(50, 90)
        self.country = random.choice(countrylist)

class Team:
    newid = itertools.count()
    def __init__(self, name):
        self.name = name
        self.player1 = Player(name)
        self.player2 = Player(name)
        self.player3 = Player(name)
        self.player4 = Player(name)
        self.player5 = Player(name)
        self.player6 = Player(name)
        self.player7 = Player(name)
        self.player8 = Player(name)
        self.player9 = Player(name)
        self.player10 = Player(name)
        self.player11 = Player(name)
        self.playerlist = [self.player1.name, self.player2.name, self.player3.name, self.player4.name, self.player5.name, self.player6.name, self.player7.name, self.player8.name, self.player9.name, self.player10.name]

class Game:
    def __init__(self, team1, team2):
        self.team1win = 50
        self.team2win = 50
        self.team1avg = round((team1.player1.skill + team1.player2.skill +team1.player3.skill+team1.player4.skill+team1.player5.skill+team1.player6.skill+team1.player7.skill+team1.player8.skill+team1.player9.skill+team1.player10.skill+team1.player11.skill)/11,0)
        self.team2avg = round((team2.player1.skill + team2.player2.skill +team2.player3.skill+team2.player4.skill+team2.player5.skill+team2.player6.skill+team2.player7.skill+team1.player8.skill+team2.player9.skill+team2.player10.skill+team2.player11.skill)/11, 0)
        if self.team1avg - self.team2avg > 0:
            self.team1win = 50 + (1* (self.team1avg - self.team2avg))
        elif self.team2avg - self.team1avg > 0:
            self.team2win = 50 + (1*(self.team2avg - self.team1avg))
        else:
            self.team1win = 50
            self.team2win = 50
        self.Winner = Game.play(self)
    
    def play(self):
        teamchoice = ["Rangers"]*int(self.team1win) + ["Lions"]*int(self.team2win) + ["Draw"]*10
        outcome = random.choice(teamchoice)
        if outcome == "Draw":
            return "It's a Draw!"
        else:
            return "The "+outcome+" won!"

Rangers = Team("Rangers")
Lions = Team("The Lions")

Game1 = Game(Rangers, Lions)
print("The skill of The Rangers is "+ str(Game1.team1avg))
print("The skill of The Lions is "+str(Game1.team2avg))
#print(Game1.team1win)
#print(Game1.team2win)
print(Game1.Winner)
