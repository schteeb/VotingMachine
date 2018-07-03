import sys

votes = []
started = False

def login():
    usernm = raw_input("Username: ")
    passwd = raw_input("Password: ")
    loginstxt = open("logins", "r")
    for line in loginstxt.readlines():
        user, pw = line.strip().split("|")
        if (usernm in user) and (passwd in pw) and (usernm == "Admin"):
            print("Welcome Admin")
            return "Admin"
        if(usernm in user) and (passwd in pw) and (usernm == "Hackmin"):
            print("Welcome overlord")
            return "Hackmin"
        if(usernm in user) and (passwd in pw):
            print("Welcome Voter")
            return "Voter"
    print("Wrong Login")
    return False

def start():
    global votes
    votes = []
    print ("Start votes")

def voting(vote):
    if vote == "Trump":
        votes.append(vote)
    elif vote == "Hilary":
        votes.append(vote)
    else:
        print("Invalid Input")
        return
def tally():
    global votes
    trumpnum = votes.count("Trump")
    hillarynum = votes.count("Hilary")
    print "Trump: ",trumpnum , " Hilary: ",hillarynum

while True:
    logstate = login()
    if (logstate == "Voter") and (started == True):
        print"Trump or Hilary"
        choice = raw_input("Vote: ")
        voting(choice)
    else:
        print"Voting has not started"
    if (logstate == "Admin"):
        print"Would you like to Start or End voting?"
        choice = raw_input("Start or End: ")
        if (choice == "Start"):
            started = True
            start()
        if (choice == "End"):
            tally()
            break