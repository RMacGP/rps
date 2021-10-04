def determine_moves():
    global user_idx, computer_idx2, computer_move2, user_move2
    user_idx = -1
    computer_idx2 = randint(0, 2)
    while user_idx == -1:
        basic.show_string("A=R, B=P, A+B=S")
    computer_move2 = choices[computer_idx2]
    user_move2 = choices[user_idx]

def on_button_pressed_a():
    global user_idx
    user_idx = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def user_won():
    computer_move = ""
    user_move = ""
    if user_move == "R" and computer_move == "P":
        return True
    elif user_move == "R" and computer_move == "R":
        return True
    elif user_move == "R" and computer_move == "S":
        return False
    elif user_move == "P" and computer_move == "P":
        return True
    elif user_move == "P" and computer_move == "R":
        return True
    elif user_move == "P" and computer_move == "S":
        return False
    elif user_move == "S" and computer_move == "P":
        return True
    elif user_move == "S" and computer_move == "R":
        return False
    elif user_move == "S" and computer_move == "S":
        return True
    return True

def on_button_pressed_ab():
    global user_idx
    user_idx = 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global user_idx
    user_idx = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

user_move2 = ""
computer_move2 = ""
computer_idx2 = 0
user_idx = 0
choices: List[str] = []
computer_idx = 0
choices = ["R", "P", "S"]

def on_forever():
    basic.show_string("RPS!")
    basic.show_string("A=R, B=P, A+B=S")
    determine_moves()
    if user_won():
        basic.show_string(":)")
    else:
        basic.show_string(":(")
basic.forever(on_forever)
