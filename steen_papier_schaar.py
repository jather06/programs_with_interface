import tkinter as tk
import random
from time import sleep

# Dictionaries and vars
outcomes = {
    "steen": {"steen": 1, "papier": 0, "schaar": 2},
    "papier": {"steen": 2, "papier": 1, "schaar": 0},
    "schaar": {"steen": 0, "papier": 2, "schaar": 1}
}

comp_score = 0
player_score = 0

# Main Screen
master = tk.Tk()
master.title("steen papier schaar drip loool")
master.config(bg='#b399fd')
master.geometry('600x400')


# Functions
def converted_outcome(number):
    if number == 1:
        return "steen"
    elif number == 2:
        return "papier"
    elif number == 3:
        return "schaar"


# Defining who wins and printing it out
def outcome_handler(user_choice):
    print(user_choice)
    global comp_score
    global player_score
    random_number = random.randint(1, 3)
    computer_choice = converted_outcome(random_number)
    outcome = outcomes[user_choice][computer_choice]
    player_choice_label.config(fg="red", text="speler keuze: " + str(user_choice))
    computer_choice_label.config(fg="green", text="computer keuze : " + str(computer_choice))
    if outcome == 2:
        player_score = player_score + 1
        player_score_label.config(text="Speler: " + str(player_score))
        outcome_label.config(fg="#6b5b97", font=("Helvetica", 15), text="uitkomst : speler heeft gewonnen")
    elif outcome == 0:
        comp_score = comp_score + 1
        computer_score_label.config(text="Computer : " + str(comp_score))
        outcome_label.config(fg="#6b5b97", font=("Helvetica", 15), text="uitkomst : computer heeft gewonnen")
    elif outcome == 1:
        player_score = player_score + 0
        comp_score = comp_score + 0
        player_score_label.config(text="Speler: " + str(player_score))
        computer_score_label.config(text="Computer : " + str(comp_score))
        outcome_label.config(fg="#6b5b97", font=("Helvetica", 15), text="uitkomst : gelijkspel")


# Defines images and configures labels for them
steen = tk.PhotoImage(file='steen.png')
papier = tk.PhotoImage(file='papier.png')
schaar = tk.PhotoImage(file='scissors.png')

steen_label = tk.Label(master, image=steen)
papier_label = tk.Label(master, image=papier)
schaar_label = tk.Label(master, image=schaar)


# Places images
def rockimage():
    steen_label.grid(row=5)


def paperimage():
    papier_label.grid(row=5)


def scissorsimage():
    schaar_label.grid(row=5)


def removeimg():
    steen_label.grid_forget()
    papier_label.grid_forget()
    schaar_label.grid_forget()


# Labels
tk.Label(master, text="steen, papier, schaar", bg='#b399fd', font=("Helvetica", 14)).grid(row=0, sticky='N', pady=10, padx=200)
tk.Label(master, text="selecteer een optie", bg='#b399fd', font=("Helvetica", 12)).grid(row=1, sticky='N')
player_score_label = tk.Label(master, text="Speler: 0", bg='#b399fd', font=("Helvetica", 12))
player_score_label.grid(row=2, sticky='W')
computer_score_label = tk.Label(master, text="Computer : 0", bg='#b399fd', font=("Helvetica", 12))
computer_score_label.grid(row=2, sticky='E')
player_choice_label = tk.Label(master, font=("Helvetica", 12), bg='#b399fd')
player_choice_label.grid(row=3, sticky='W')
computer_choice_label = tk.Label(master, font=("Helvetica", 12), bg='#b399fd')
computer_choice_label.grid(row=3, sticky='E')
outcome_label = tk.Label(master, font=("Helvetica", 12), bg='#b399fd')
outcome_label.grid(row=3, sticky='N')

# Buttons
tk.Button(master, text="steen", bg='#D8CBFE', font=("Helvetica", 11), width=15, command=lambda:
[rockimage(), outcome_handler("steen")]).place(relx=0.1, rely=0.9)

tk.Button(master, text="papier", bg='#D8CBFE', font=("Helvetica", 11), width=15, command=lambda:
[paperimage(), outcome_handler("papier")]).place(relx=0.4, rely=0.9)

tk.Button(master, text="schaar", bg='#D8CBFE', font=("Helvetica", 11), width=15, command=lambda:
[scissorsimage(), outcome_handler("schaar")]).place(relx=0.7, rely=0.9)

tk.Button(master, text="nieuw spel", bg='#D8CBFE', font=("Helvetica", 11), width=15, command=lambda:
removeimg()).grid(row=2, sticky='N', pady=5)

master.mainloop()
