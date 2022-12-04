import threading
import PySimpleGUI as sg
#Define some vals
main_color = "black"
text_color = "white"
sg.theme_background_color(main_color)
# size of the button
s = (23,11)
# number of buttons
n = "123456789"

#the path of the pics

OPath = 'Pyhton\\TicTacToe\\img\\O.png'
XPath = 'Pyhton\\TicTacToe\\img\\X.png'
BlackPath = 'Pyhton\\TicTacToe\\img\\black.png'
StartButton = 'Pyhton\\TicTacToe\\img\\Start.png'

#List of layouts
lay_list = ["menu","game","winpage"]
# the number of the layout that is active right now
laynow = 0


# the layouts for each window
menu = [
        [sg.Push(background_color = main_color),sg.Text("**********************Welcome**********************",background_color=main_color,text_color=text_color),sg.Push(background_color = main_color)],
        [sg.VPush(background_color = main_color),sg.Push(background_color = main_color),sg.Button(key = "start",image_filename=StartButton,button_color=main_color,border_width=0),sg.Push(background_color = main_color),sg.VPush(background_color=main_color)]
    ]
game = [    
            [sg.Button("1",key="1",size=s,button_color=("white",main_color),border_width=0),sg.Button("2",key="2",size=s,button_color=("white",main_color),border_width=0),sg.Button("3",key="3",size=s,button_color=("white",main_color),border_width=0)],
            [sg.Button("4",key="4",size=s,button_color=("white",main_color),border_width=0),sg.Button("5",key="5",size=s,button_color=("white",main_color),border_width=0),sg.Button("6",key="6",size=s,button_color=("white",main_color),border_width=0)],
            [sg.Button("7",key="7",size=s,button_color=("white",main_color),border_width=0,),sg.Button("8",key="8",size=s,button_color=("white",main_color),border_width=0),sg.Button("9",key="9",size=s,button_color=("white",main_color),border_width=0)],
            [sg.Push(background_color='white'),sg.Button("Return",key="back")]
    ]
win_lay = [[sg.VPush(background_color=main_color),sg.Push(background_color=main_color),sg.Text("",key="winner",text_color=text_color,background_color=main_color,font="PricedownBlack"),sg.Push(background_color=main_color),sg.VPush(background_color=main_color)],
           [sg.VPush(background_color=main_color),sg.Push(background_color=main_color),sg.Button("Retry",key="reset")]
        ]


layout = [[sg.Column(menu,key="menu"),sg.Column(game,key="game",visible=False,background_color='white'),sg.Column(win_lay,key="winpage",visible=False,size=(400,100))]]


#game board
board =[
["","",""],
["","",""],
["","",""]
]
#last one who played
last = "O"




window = sg.Window('TicTacToe', layout)

#the logic behind the game to find the winner
def logic():
    currentChar = board[0][0]
    winner = ""
    if currentChar != "" and board[0][1] == currentChar and board[0][2] == currentChar: # check first row
        print(f"{currentChar} wins!")
        winner = currentChar

    currentChar = board[1][0]
    if currentChar != "" and board[1][1] == currentChar and board[1][2] == currentChar: # check second row
        print(f"{currentChar} wins!")
        winner = currentChar

    currentChar = board[2][0]
    if currentChar != "" and board[2][1] == currentChar and board[2][2] == currentChar: # check third row
        print(f"{currentChar} wins!")
        winner = currentChar
    currentChar = board[0][0]
    if currentChar != "" and board[1][0] == currentChar and board[2][0] == currentChar: # check first column
        print(f"{currentChar} wins!")
        winner = currentChar
    currentChar = board[0][1]
    if currentChar != "" and board[1][1] == currentChar and board[2][1] == currentChar: # check second column
        print(f"{currentChar} wins!")
        winner = currentChar
    currentChar = board[0][2]
    if currentChar != "" and board[1][2] == currentChar and board[2][2] == currentChar: # check third column
        print(f"{currentChar} wins!")
        winner = currentChar
    currentChar = board[0][0]
    if currentChar != "" and board[1][1] == currentChar and board[2][2] == currentChar: # check first diagonal
        print(f"{currentChar} wins!")
        winner = currentChar
    currentChar = board[0][2]
    if currentChar != "" and board[1][1] == currentChar and board[2][0] == currentChar: # check second diagonal
        print(f"{currentChar} wins!")
        winner = currentChar
    if winner != "":
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow+1]].Update(visible = True)
        window["winner"].Update(f"{winner} IS THE WINNER!")
        window.move_to_center()
    if "" in board[0] or "" in board[1] or "" in board[2]:
        pass
    else:
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow+1]].Update(visible = True)
        window["winner"].Update("IT'S A DRAW")
        window.move_to_center()


while True:
    state, values = window.read()

    if state in n :
        if last == "X":
            last ="O"
            window[state].Update(image_filename=OPath)
            if int(state) < 4:              
                board[0][int(state)-1] = 'O'
            elif int(state) <7:
                board[1][int(state)-4] = 'O'
            else:
                board[2][int(state)-7] = 'O'
        else:
            last ="X"
            window[state].Update(image_filename=XPath)
            if int(state) < 4:              
                board[0][int(state)-1] = "X"
            elif int(state) <7:
                board[1][int(state)-4] = "X"
            else:
                board[2][int(state)-7] = "X"

    elif state == "start" :
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow+1]].Update(visible = True)
        laynow+=1
        window.move(100,100)
    elif state == "back":
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow-1]].Update(visible = True)
        laynow-=1
        for i in range(1,10):
            window[f"{i}"].Update(image_filename=BlackPath)
        board =[
        ["","",""],
        ["","",""],
        ["","",""]
        ]
        last = "O"
    elif state == "reset":
        board =[
        ["","",""],
        ["","",""],
        ["","",""]
        ]
        last = "O"
        window[lay_list[2]].Update(visible = False)
        window[lay_list[0]].Update(visible = True)
        laynow = 0
        for i in range(1,10):
            window[f"{i}"].Update(image_filename=BlackPath)

    logic()
    print(state)
    if state in (None, 'Exit'):
        break




    




