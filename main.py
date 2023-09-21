from tkinter import *
from tkinter import messagebox
from possible_combinations import possibilities
WHITE = "white"
winning_combinations = [123, 456, 789, 147, 258, 369, 159, 357]
all_locs = []
sign_color = ""
close_game = 0
num_of_occupied_locs = 0


def put_the_sign(loc, num_loc):
    global symbol, sign, x_combs, o_combs, x_locs, o_locs, game_ended, num_of_occupied_locs, sign_color, close_game
    num_of_occupied_locs = 0
    if sign % 2 == 0:
        symbol = "o"
        sign_color = "blue"
        o_locs += num_loc
        if len(o_locs) >= 3:
            o_combs = possibilities(o_locs)

    else:
        symbol = "x"
        sign_color = "red"
        x_locs += num_loc
        if len(x_locs) >= 3:
            x_combs = possibilities(x_locs)

    loc.config(text=symbol, fg=sign_color, font=("bold", 30), height=1, width=3)
    loc.place(x=loc.winfo_x() + 17, y=loc.winfo_y() + 10)

    for comb in o_combs:
        if comb in winning_combinations:
            game_ended = messagebox.askyesno("Game ended", "o won the game!!\nHard luck, x\nWanna play again?")
            close_game = 1

    for comb in x_combs:
        if comb in winning_combinations:
            game_ended = messagebox.askyesno("Game ended", "x won the game!!\nHard luck, o\nWanna play again?")
            close_game = 1

    if game_ended:
        create_screen()
        return

    else:
        if close_game == 1:
            quit()

    sign += 1

    for i in all_locs:
        if i.cget("text") == "":
            break

        else:
            num_of_occupied_locs += 1
            if num_of_occupied_locs == 9:
                game_ended = messagebox.askyesno("Game ended", "It's a draw\nWanna play again?")
                close_game = 1
                if game_ended:
                    create_screen()
                    return

                else:
                    if close_game == 1:
                        quit()


win = Tk()
win.config(bg="white")
win.title("TicTacToe")
win.minsize(400, 400)
canvas = Canvas(height=360, width=360, bg=WHITE, highlightthickness=0)
img = PhotoImage(file="img.png")
canvas.create_image(180, 180, image=img, anchor="center")
canvas.place(x=20, y=20)
AI_or_BOT = True


def create_screen():

    global sign, symbol, x_combs, o_combs, x_locs, o_locs, game_ended, all_locs, num_of_occupied_locs, AI_or_BOT, close_game
    AI_or_BOT = messagebox.askyesno("Start game", "If you want to play with a human press yes if you want to play with a bot press no")
    game_ended = False
    close_game = 0
    if AI_or_BOT:
        pass
    sign = 1
    num_of_occupied_locs = 0
    symbol = ""
    x_combs = []
    o_combs = []
    x_locs = ""
    o_locs = ""
    loc_1 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_1, "1"))
    loc_1.place(x=25, y=20)
    loc_2 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_2, "2"))
    loc_2.place(x=147, y=20)

    loc_3 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_3, "3"))
    loc_3.place(x=269, y=20)

    loc_4 = Button(text="", height=6, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_4, "4"))
    loc_4.place(x=25, y=150)

    loc_5 = Button(text="", height=6, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_5, "5"))
    loc_5.place(x=148, y=150)

    loc_6 = Button(text="", height=6, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_6, "6"))
    loc_6.place(x=269, y=150)

    loc_7 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_7, "7"))
    loc_7.place(x=25, y=269)

    loc_8 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_8, "8"))
    loc_8.place(x=147, y=269)

    loc_9 = Button(text="", height=7, width=14, bg=WHITE, border=0, activebackground=WHITE, command=lambda: put_the_sign(loc_9, "9"))
    loc_9.place(x=269, y=269)

    all_locs = [loc_1, loc_2, loc_3, loc_4, loc_5, loc_6, loc_7, loc_8, loc_9]


create_screen()
win.mainloop()
