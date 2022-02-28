from tkinter import *
import random
from PIL import Image, ImageTk

def press_shuffle():
    global button_shuffle
    button_shuffle = Button(window, text='Press to shuffle cards', bg="light green", padx=25, pady=25,
                            font=("Helvatica", 14), command=shuffle_cards)
    button_shuffle.place(relx=0.5, rely=0.5, anchor=CENTER)

def shuffle_cards():
    global computer_hand, player_hand, computer_numbers, player_numbers
    cards_numbers = []
    for i in range(1, 101):
        cards_numbers.append(i)
    computer_numbers = sorted(random.sample(cards_numbers, 5))
    for i in computer_numbers:
        if i in cards_numbers:
            cards_numbers.remove(i)
    player_numbers = sorted(random.sample(cards_numbers, 5))
    computer_hand = []
    for i in computer_numbers:
        computer_hand.append("{}_card".format(i))
    player_hand = []
    for i in player_numbers:
        player_hand.append("{}_card".format(i))
    computer_button()
    button_shuffle.place_forget()
    show_cards_player()
    show_cards_computer(x_card)

def computer_button():
    global button_computer
    global label_computer_play
    button_computer = Button(window, image=computer_icon_button(), bg="green", bd=1, activebackground="green",
                             command=lambda: [computer_trow_card(), order_check_computer()], state=NORMAL)
    button_computer.place(relx=0.99, rely=0.5, anchor=E)
    label_computer_play = Label(window, text="""Computer throws card""", bg="yellow", font=("Helvetica", 12, "bold"))
    label_computer_play.place(relx=1, rely=0.41, anchor=E)

def show_cards_player():
    global photos_cards_player, photos_cards_computer, panel_0,  panel_1,  panel_2,  panel_3,  panel_4

    photos_cards_computer = []
    photos_cards_player = []

    for card in player_hand:
        resized_card = resize_cards(f'pictures/{card}.jpg')
        photos_cards_player.append(resized_card)
    for card in computer_hand:
        resized_card_r = resize_cards(f'pictures/{card}.jpg')
        photos_cards_computer.append(resized_card_r)

    panel_0 = Button(frame_cards_player, image=photos_cards_player[0], bg="green", bd= 0, fg="green",
                     command= lambda: [panel_0.grid_forget(), cards_in_the_middle(photos_cards_player[0]),
                                       order_check_player(0)], state= NORMAL)
    panel_0.grid(row=0, column=0)
    panel_1 = Button(frame_cards_player, image=photos_cards_player[1], bg="green", bd= 0,
                     command= lambda: [panel_1.grid_forget(), cards_in_the_middle(photos_cards_player[1]),
                                       order_check_player(1)], state= NORMAL)
    panel_1.grid(row=0, column=1)
    panel_2 = Button(frame_cards_player, image=photos_cards_player[2], bg="green", bd= 0,
                     command= lambda: [panel_2.grid_forget(), cards_in_the_middle(photos_cards_player[2]),
                                       order_check_player(2)], state= NORMAL)
    panel_2.grid(row=0, column=2)
    panel_3 = Button(frame_cards_player, image=photos_cards_player[3], bg="green", bd= 0,
                     command= lambda: [panel_3.grid_forget(), cards_in_the_middle(photos_cards_player[3]),
                                       order_check_player(3)], state= NORMAL)
    panel_3.grid(row=0, column=3)
    panel_4 = Button(frame_cards_player, image=photos_cards_player[4], bg="green", bd= 0,
                     command= lambda: [panel_4.grid_forget(), cards_in_the_middle(photos_cards_player[4]),
                                       order_check_player(4)], state= NORMAL)
    panel_4.grid(row=0, column=4)

def show_cards_computer(x):
    resized_card_computer = resize_cards(f'pictures/comp_card.png')
    panel_5 = Label(frame_cards_computer, image=resized_card_computer, bg= "green",fg="black")
    panel_5.grid(row=0, column=1)
    if x >= 1:
        panel_5.grid_forget()
        
    panel_6 = Label(frame_cards_computer, image=resized_card_computer,bg= "green")
    panel_6.grid(row=0, column=2)
    if x >= 2:
        panel_6.grid_forget()

    panel_7 = Label(frame_cards_computer, image=resized_card_computer,bg= "green")
    panel_7.grid(row=0, column=3)
    if x >= 3:
        panel_7.grid_forget()

    panel_8 = Label(frame_cards_computer, image=resized_card_computer,bg= "green")
    panel_8.grid(row=0, column=4)
    if x >= 4:
        panel_8.grid_forget()

    panel_9 = Label(frame_cards_computer, image=resized_card_computer,bg= "green")
    panel_9.grid(row=0, column=5)
    if x >= 5:
        panel_9.grid_forget()

def cards_in_the_middle(card):
    panel_0 = Label(frame_cards_middle, image= card, bg="black")
    panel_0.grid(row=0, column=0)

def computer_trow_card():
    global x_card
    try:
        panel_0 = Label(frame_cards_middle, image= photos_cards_computer[x_card], bg="black")
        panel_0.grid(row=0, column= 0)
        x_card += 1
        show_cards_computer(x_card)
    except:
        pass

def order_check_player(x):
    global frame_victory, num_win
    if len(computer_numbers) == 0 or len(player_numbers) == 0:
        frame_cards_middle.place_forget()
        frame_cards_player.pack_forget()
        frame_cards_computer.pack_forget()

        num_win += 1
        title(num_win, num_lose)

        frame_victory = Frame(window, bg='green')
        frame_victory.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_victory = Label(frame_victory, image=victory_photo_resized(f'pictures/victory.jpg'),
                              bg='green')
        label_victory.grid(row=0, column=0)
        again_label = Label(frame_victory, bg="green", text="Play again?", font=("Mincho", 40, "bold"))
        again_label.grid(row=1, column=0)
        again_button_yes = Button(frame_victory, image=thumb_resize_up(f'pictures/thumb_up.jpg'),
                                  command=play_again_victory, bg="green", bd=1, activebackground="green")
        again_button_yes.grid(row=1, column=1)
        again_button_no = Button(frame_victory, image=thumb_resize_down(f'pictures/thumb_down.jpg'),
                                 command=window.quit, bg="green", bd=1, activebackground="green")
        again_button_no.grid(row=1, column=2)
        button_computer["state"] = DISABLED
    else:
        card_number = int(player_hand[x].split("_", 1)[0])
        if card_number > min(player_numbers):
            game_over("wrong_card")
        elif card_number > min(computer_numbers):
            game_over("player")
            panel = Label(frame_cards_computer,
                          image=resize_cards(f'pictures/{min(computer_numbers)}_card.jpg'), bg="dark red")
            panel.grid(row=0, column=3)
        else:
            player_numbers.remove(min(player_numbers))

def order_check_computer():
    global frame_victory, num_win
    if len(computer_numbers) == 0 or len(player_numbers) == 0:
        frame_cards_middle.place_forget()
        frame_cards_player.pack_forget()
        frame_cards_computer.pack_forget()

        num_win += 1
        title(num_win, num_lose)

        frame_victory = Frame(window, bg='green')
        frame_victory.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_victory = Label(frame_victory, image=victory_photo_resized(f'pictures/victory.jpg'),
                              bg='green')
        label_victory.grid(row=0, column=0)
        again_label = Label(frame_victory, bg="green", text="Play again?", font=("Mincho", 40, "bold"))
        again_label.grid(row=1, column=0)
        again_button_yes = Button(frame_victory, image=thumb_resize_up(f'pictures/thumb_up.jpg'),
                                  command=play_again_victory, bg="green", bd=1, activebackground="green")
        again_button_yes.grid(row=1, column=1)
        again_button_no = Button(frame_victory, image=thumb_resize_down(f'pictures/thumb_down.jpg'),
                                 command= window.quit, bg="green", bd=1, activebackground="green", pady= 20)
        again_button_no.grid(row=1, column=2)
        button_computer["state"] = DISABLED
    else:
        if min(computer_numbers) > min(player_numbers):
            game_over("computer")
            panel = Label(frame_cards_computer,
                          image=resize_cards(f'pictures/{min(computer_numbers)}_card.jpg'), bg="dark red")
            panel.grid(row=0, column=3)
        else:
            computer_numbers.remove(min(computer_numbers))

def game_over(name):
    global frame_gameover, num_lose
    panel_0["state"] = DISABLED
    panel_1["state"] = DISABLED
    panel_2["state"] = DISABLED
    panel_3["state"] = DISABLED
    panel_4["state"] = DISABLED
    button_computer["state"] = DISABLED
    num_lose += 1
    title(num_win, num_lose)
    label_computer_play.place_forget()
    frame_cards_middle.place_forget()
    frame_gameover = Frame(window, bg="green")
    frame_gameover.place(relx=0.5, rely=0.5, anchor=CENTER)
    gameover_label = Label(frame_gameover, bg="green", text="GAME OVER", font=("Mincho", 40))
    gameover_label.grid(row=0, column=1)

    if name == "player":
        player_label = Label(frame_gameover, bg= "green", text=" COMPUTER HAD LOWER CARD {}".format(min(computer_numbers)),
                             font=("Mincho", 20), fg="dark red")
        player_label.grid(row=1, column=1)


    if name == "computer":
        lower_player_cards = [x for x in player_numbers if x < min(computer_numbers)]
        string = " & ".join(str(x) for x in lower_player_cards)
        computer_label = Label(frame_gameover, bg= "green", text=" YOU HAD LOWEST CARD(S): {}".format(string),
                         font=("Mincho", 20), fg="dark red")
        computer_label.grid(row=1, column=1)

    if name == "wrong_card":
        computer_label = Label(frame_gameover, bg= "green", text="YOU DIDN'T THROW YOUR LOWEST CARD",
                         font=("Mincho", 20), fg="dark red")
        computer_label.grid(row=1, column=1)

    again_label = Label(frame_gameover, bg="green", text="PLAY AGAIN?", font=("Mincho", 40))
    again_label.grid(row=3, column=1)
    again_button_yes = Button(frame_gameover, image=thumb_resize_up(f'pictures/thumb_up.jpg'),
                              command= play_again_lose, bg="green", bd=1, activebackground="green")
    again_button_yes.grid(row=3, column=2)
    again_button_no = Button(frame_gameover,image= thumb_resize_down(f'pictures/thumb_down.jpg'),
                             command= window.quit, bg= "green", bd= 1, activebackground= "green", pady= 20)
    again_button_no.grid(row=3, column=3)

def play_again_lose():
    global frame_cards_middle, x_card
    frame_gameover.place_forget()
    x_card = 0
    shuffle_cards()
    frame_cards_middle = Frame(window, bg='green')
    frame_cards_middle.place(relx=0.5, rely=0.5, anchor=CENTER)

def play_again_victory():
    global x_card, frame_cards_computer, frame_cards_middle, frame_cards_player
    frame_victory.place_forget()
    x_card = 0
    shuffle_cards()
    frame_cards_middle = Frame(window, bg='green')
    frame_cards_middle.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame_cards_computer.pack(side=TOP)
    frame_cards_player.pack(side=BOTTOM)

def resize_cards(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((160,230))
    global final_card
    final_card = ImageTk.PhotoImage(resized_image)
    return final_card

def computer_icon_button():
    entry_card = Image.open(f'pictures/computer_icon.png')
    resized_image = entry_card.resize((100,100))
    global final_button_comp
    final_button_comp = ImageTk.PhotoImage(resized_image)
    return  final_button_comp

def thumb_resize_down(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((50, 50))
    global final_thumb_down
    final_thumb_down = ImageTk.PhotoImage(resized_image)
    return final_thumb_down

def thumb_resize_up(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((50, 50))
    global final_thumb_up
    final_thumb_up = ImageTk.PhotoImage(resized_image)
    return final_thumb_up

def victory_photo_resized(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((300, 300))
    global photo_victory
    photo_victory = ImageTk.PhotoImage(resized_image)
    return photo_victory


def title(num_win, num_lose):
    window.title("From The Bottom Up  ||  WINS: {}   LOSES: {}".format(num_win, num_lose))

def about_game():
    window_ag = Tk()
    window_ag.geometry("900x150")
    window_ag.configure(background="light green")
    window_ag.iconbitmap(r'pictures/icon.ico')
    window_ag.title("About the Game")
    label_about = Label(window_ag, text= """ 
    The game From The Bottom Up is a simple card game where player can test his skills (or luck) of guessing computer cards. 
    
    The goal of the game is very simple. Sort cards from the smallest number to the largest number.
        
    Will player throw the next card or will the computer? The choice will result in victory or defeat. 

    """, font= ("Helvatica", 12), relief= "sunken", justify= "left", bg= "light green", bd= 0).pack(pady= 0, ipady= 0, ipadx= 0)

def how_to_play():
    window_htp = Tk()
    window_htp.geometry("900x200")
    window_htp.configure(background="light green")
    window_htp.iconbitmap(r'pictures/icon.ico')
    window_htp.title("How to play")
    label_about = Label(window_htp, text=""" 
    The deck contains cards numbered 1-100. At the beginning of each round, players and the computer get five cards. 
    
    The player must sort the cards from the smallest number to the largest, but he doesn't know which cards the computer has. 
    
    If the player wants to discard one of his cards, he presses it. 
    
    If player wants the computer to discard the card with the lowest number, he presses the computer button.
    
    If the smallest card is not thrown, the game stops.

        """, font=("Helvatica", 12), relief="sunken", justify="left", bg="light green", bd=0).pack(pady=0, ipady=0, ipadx=0)

    window_htp.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.geometry("1200x800")
    window.configure(background= "#008000")
    window.iconbitmap(r'pictures/icon.ico')
    info_menu = Menu(window)

    window.config(menu= info_menu)
    info_game = Menu(info_menu, tearoff= 0)
    info_menu.add_cascade(label= "Info", menu= info_game)
    info_game.add_command(label = "About the game", command= about_game)
    info_game.add_separator()
    info_game.add_command(label="How to play?", command= how_to_play)

    frame_cards_computer = Frame(window, bg="green")
    frame_cards_computer.pack(side=TOP)

    frame_cards_player = Frame(window, bg="green")
    frame_cards_player.pack(side=BOTTOM)

    frame_cards_middle = Frame(window, bg='green')
    frame_cards_middle.place(relx=0.5, rely=0.5, anchor=CENTER)

    title(0,0)
    press_shuffle()
    x_card = 0
    num_lose = 0
    num_win = 0

    window.mainloop()