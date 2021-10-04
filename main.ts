function determine_moves () {
    user_idx = -1
    computer_idx2 = randint(0, 2)
    while (user_idx == -1) {
        basic.showString("A=R, B=P, A+B=S")
    }
    computer_move2 = choices[computer_idx2]
    user_move2 = choices[user_idx]
}
input.onButtonPressed(Button.A, function () {
    user_idx = 0
})
function user_won () {
    let computer_move = ""
    let user_move = ""
    if (user_move == "R" && computer_move == "P") {
        return true
    } else if (user_move == "R" && computer_move == "R") {
        return true
    } else if (user_move == "R" && computer_move == "S") {
        return false
    } else if (user_move == "P" && computer_move == "P") {
        return true
    } else if (user_move == "P" && computer_move == "R") {
        return true
    } else if (user_move == "P" && computer_move == "S") {
        return false
    } else if (user_move == "S" && computer_move == "P") {
        return true
    } else if (user_move == "S" && computer_move == "R") {
        return false
    } else if (user_move == "S" && computer_move == "S") {
        return true
    }
    return true
}
input.onButtonPressed(Button.AB, function () {
    user_idx = 2
})
input.onButtonPressed(Button.B, function () {
    user_idx = 1
})
let user_move2 = ""
let computer_move2 = ""
let computer_idx2 = 0
let user_idx = 0
let choices: string[] = []
let computer_idx = 0
choices = ["R", "P", "S"]
basic.forever(function () {
    basic.showString("RPS!")
    determine_moves()
    if (user_won()) {
        basic.showString(":)")
    } else {
        basic.showString(":(")
    }
})
