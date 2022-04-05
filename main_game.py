from tkinter import *
from random import randint

player1_score = 0
computer_score = 0
best_of_three = 0

# Main Window ****************
mainRoot = Tk()
mainRoot.title("Simple Dice Game")
mainRoot.iconbitmap("dice.ico")


# Menu Functions *


def new_game():
    global computer_score
    global player1_score
    global best_of_three
    player1_score = 0
    computer_score = 0
    best_of_three = 0
    computer_total_score.config(text="Total Score: 0")
    computer_current_score.config(text="Current: 0")
    human_score_label.config(text='Total Score: 0')
    human_current_score.config(text='Current: 0')
    human_roll_button.config(text="Roll", command=human_player_one, state='active')


def about():

    about_window = Tk()
    about_window.iconbitmap("dice.ico")
    about_window.title("Dice Game Info")
    about_window.configure(bg='#CDCDC1')

    about_label1 = Label(about_window, text="This is a simple dice game that plays one player against a computer",
                         font="Arial, 15", bg='#CDCDC1')
    about_label1.grid(row=0, column=0)

    about_label2 = Label(about_window, text='Clicking the "Roll" button on the Human side will start the game and \n'
                                            'after you can click 3 times the game will end, since the game is based \n'
                                            'on best of 3 rounds',
                         font="Arial, 15", bg='#CDCDC1')
    about_label2.grid(row=1, column=0, pady=15)

    about_label3 = Label(about_window, text='Clicking the "Game" menu button on the top left corner will open up two \n'
                                            'options for "New" and "About": New just starts a new game after the first\n'
                                            'game is done and the "About" opens up this window.', bg='#CDCDC1',
                         font='Arial, 15')
    about_label3.grid(row=2, column=0, pady=15)

    about_label4 = Label(about_window, text="The game picks two numbers between 1 - 6 twice, since that's the limit for\n"
                                            "for dice, the game then takes those two numbers and adds them to the total\n"
                                            "score where it is then calumniated and whoever has the higher score wins.",
                         font="Arial, 15", bg='#CDCDC1')
    about_label4.grid(row=3, column=0, pady=15)

    about_window.mainloop()


# Menu options
main_menu = Menu(mainRoot)
mainRoot.config(menu=main_menu)

# Menu Items
game_menu = Menu(main_menu)
main_menu.add_cascade(label="Game", menu=game_menu)
game_menu.add_command(label="New", command=new_game)
game_menu.add_separator()
game_menu.add_command(label='About', command=about)


# Dice Roll Function H vs C


def computer_plays():
    global computer_score
    computer1 = plays()
    computer_score += computer1

    computer_total_score.config(text="Total Score: {}".format(computer_score))
    computer_current_score.config(text="Current: {}".format(computer1))

    print("-" * 45)
    print(f"Total Computer Score = {computer_score}")
    print(f"Current Score = {computer1}")


def plays():
    play1 = randint(1, 6)
    play2 = randint(1, 6)
    total = play1 + play2
    return total


def human_player_one():
    global player1_score
    global best_of_three
    global computer_score
    player1 = plays()

    if best_of_three < 3:
        player1_score += player1
        computer_plays()
        human_score_label.config(text="Total Score: {}".format(player1_score))
        human_current_score.config(text="Current: {}".format(player1))
        best_of_three += 1
        print('-' * 45)
        print(f"Total Human Score = {player1_score}")
        print(f"Current Human Score = {player1}")

    elif best_of_three == 3:
        if player1_score > computer_score:
            human_score_label.config(text="You Win!: {}".format(player1_score))
            computer_total_score.config(text="I Lost! {}".format(computer_score))
            human_roll_button.config(state='disabled')

        elif computer_score > player1_score:
            human_score_label.config(text="You Lose! {}".format(player1_score))
            computer_total_score.config(text="I Won! {}".format(computer_score))
            human_roll_button.config(state='disabled')

        elif player1_score == computer_score:
            human_score_label.config(text="It's a Tie {}".format(player1_score))
            computer_total_score.config(text="It's a Tie {}".format(computer_score))
            human_roll_button.config(state='disabled')


# ****************** Computer Frame and stuffs ******************
computer_frame = Frame(mainRoot, bg="#CDCDC1", height=500, width=350)
computer_frame.grid(row=0, column=0)

# ********* Computer label *********
computer_label = Label(computer_frame, bg="#CDCDC1", fg='black', text='Computer:', font="Arial,  50")
computer_label.grid(row=0, column=0, padx=15)

# ********* Computer Score Label *********
computer_total_score = Label(computer_frame, bg="#CDCDC1", fg='black', text='Total Score: 0', font="Arial,  20")
computer_total_score.grid(row=1, column=0)

# ********* Computer Score Label *********
computer_current_score = Label(computer_frame, bg='#CDCDC1', fg='black', text='Current: 0', font="Arial, 15")
computer_current_score.grid(row=2, column=0)


# ********* Computer Roll Button *********
computer_roll_button = Button(computer_frame, bg='#282828', fg='white', text='Roll:', font="Arial, 15", relief='sunken',
                              state='disabled')
computer_roll_button.grid(row=3, column=0, sticky=W, padx=15, pady=10)


# ****************** Human Frame and stuffs ******************
human_frame = Frame(mainRoot, bg="#EEE5DE", height=500, width=350)
human_frame.grid(row=0, column=1)

human_label = Label(human_frame, bg="#EEE5DE", fg='black', text='Human:', font="Arial,  50")
human_label.grid(row=0, column=0, padx=15)

# ********* Human Total Score Label *********
human_score_label = Label(human_frame, bg="#EEE5DE", fg='black', text='Total Score: 0', font="Arial,  20")
human_score_label.grid(row=1, column=0)

# ********* Human Score Label *********
human_current_score = Label(human_frame, bg='#EEE5DE', fg='black', text='Current: 0', font="Arial, 15")
human_current_score.grid(row=2, column=0)

# ********* Human Roll Button *********
human_roll_button = Button(human_frame, bg='#282828', fg='white', text='Roll:', font="Ariel, 15", relief='sunken',
                           command=human_player_one)
human_roll_button.grid(row=3, column=0, sticky=E, padx=15, pady=10)


mainRoot.mainloop()