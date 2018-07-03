import Tkinter as tk
import tkFont as tkfont
from collections import Counter

race1votes = []
race2votes = []
race3votes = []
started = False
usedusers = ["Admin", "Hackmin"]

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, VotingPage, VotingPage2, VotingPage3, AdminPage, Tallypage, Hackmin, Thankspage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login to Vote", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.entry1 = tk.Entry(self)
        self.entry1.insert(0, "Enter Username")
        self.entry1.pack()

        self.entry2 = tk.Entry(self, show="*")
        self.entry2.insert(0, "       ")
        self.entry2.pack()

        button1 = tk.Button(self, text="Login", command=self.login)
        button1.pack()

    def login(self):
        usernm = self.entry1.get()
        passwd = self.entry2.get()
        loginstxt = open("logins", "r")
        for line in loginstxt.readlines():
            user, pw = line.strip().split("|")
            if (usernm in user) and (passwd in pw) and (usernm == "Admin"):
                print("Welcome Admin")
                app.show_frame("AdminPage")
            if (usernm in user) and (passwd in pw) and (usernm == "Hackmin"):
                print("Welcome Hacker")
                app.show_frame("Hackmin")
            if (usernm in user) and (passwd in pw) and (usernm not in usedusers) and (started == True):
                print("Welcome Voter")
                usedusers.append(usernm)
                app.show_frame("VotingPage")
        print("Wrong Login")
        return False

class VotingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Vote for your President:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Trump", command=lambda: self.vote("Trump"))
        button2 = tk.Button(self, text="Hilary", command=lambda: self.vote("Hilary"))
        button3 = tk.Button(self, text="Obama", command=lambda: self.vote("Obama"))
        button4 = tk.Button(self, text="Bush", command=lambda: self.vote("Bush"))
        button5 = tk.Button(self, text="Kanye", command=lambda: self.vote("Kanye"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

    def vote(self, vote):
        race1votes.append(vote)
        print(race1votes)
        app.show_frame("VotingPage2")

class VotingPage2(tk.Frame):
    varList = []
    x = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select vice president(s):", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        var1 = tk.StringVar()
        checkvp1 = tk.Checkbutton(self, text="Emily Hill", variable=var1, onvalue=("Hill"), offvalue="")
        var2 = tk.StringVar()
        checkvp2 = tk.Checkbutton(self, text="Rebecca Mercuri", variable=var2, onvalue="Mercuri", offvalue="")
        var3 = tk.StringVar()
        checkvp3 = tk.Checkbutton(self, text="Barry Burd", variable=var3, onvalue="Burd", offvalue="")

        submitbutton = tk.Button(self, text="submit", command= lambda: self.addvotes())

        checkvp1.pack()
        checkvp2.pack()
        checkvp3.pack()
        submitbutton.pack()
        self.varList.append(var1)
        self.varList.append(var2)
        self.varList.append(var3)

    def addvotes(self):
        for items in self.varList:
            if items.get() !="":
                race2votes.append(items.get())
        print(race2votes)
        app.show_frame("VotingPage3")

class VotingPage3(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Select policy focus:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Education/Health", command=lambda: self.votechoice("Education/Health"))
        button2 = tk.Button(self, text="Richer Rich people", command=lambda: self.votechoice("Richer Rich People"))
        button1.pack()
        button2.pack()

    def votechoice(self, vote):
        race3votes.append(vote)
        print(race3votes)
        app.show_frame("Thankspage")


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start or Stop Voting", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Start Voting", command=lambda: self.start())
        button2 = tk.Button(self, text="End Voting", command=lambda: controller.show_frame("Tallypage"))
        button1.pack()
        button2.pack()

    def start(self):
        global started
        started = True
        app.show_frame("LoginPage")

class Hackmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome. Hack away!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="HACK", command=lambda: self.hack())
        button2 = tk.Button(self, text="Don't HACK", command=lambda: controller.show_frame("LoginPage"))
        button1.pack()
        button2.pack()

    def hack(self):
        race1votes.append("Trump")
        race1votes.append("Trump")
        race1votes.append("Trump")
        race1votes.append("Trump")
        race2votes.append("Hill")
        race2votes.append("Hill")
        race2votes.append("Hill")
        race2votes.append("Hill")
        race3votes.append("Richer Rich People")
        race3votes.append("Richer Rich People")
        race3votes.append("Richer Rich People")
        race3votes.append("Richer Rich People")
        app.show_frame("Thankspage")



class Tallypage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Click show to see final results!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.race1label = tk.Label(self, text="Results of President Race", font=controller.title_font)
        self.race2label = tk.Label(self, text="Results of VP Race", font=controller.title_font)
        self.race3label = tk.Label(self, text="Results of Policy Poll", font=controller.title_font)

        showbutton = tk.Button(self, text="show", command=lambda: self.tally())
        showbutton.pack()
        self.race1label.pack()
        self.race2label.pack()
        self.race3label.pack()

        quitbutton = tk.Button(self, text="Quit", command=lambda: app.destroy())
        quitbutton.pack()

    def tally(self):
        race1final = Counter(race1votes)
        race2final = Counter(race2votes)
        race3final = Counter(race3votes)

        self.race1label.configure(text=race1final)
        self.race2label.configure(text=race2final)
        self.race3label.configure(text=race3final)

        print(race1final)
        print(race2final)
        print(race3final)

class Thankspage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Thanks for Voting", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("LoginPage"))
        button2.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("600x400")
    app.mainloop()

