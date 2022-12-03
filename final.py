import threading
import PySimpleGUI as sg

sg.theme_background_color("white")
s = (19,10)
n = "123456789"


global state , values , window ,game , menu ,last, winner
lay_list = ["menu","game","winpage"]
laynow = 0

menu = [
        [sg.Push(background_color = "white"),sg.Text("**********************Welcome**********************",background_color="white",text_color="black"),sg.Push(background_color = "white")],
        [sg.VPush(background_color="white"),sg.Push(background_color = "white"),sg.Button(key = "start",image_filename="Pyhton\\TicTacToe\\img\\Start.png",button_color="white",border_width=0),sg.Push(background_color = "white"),sg.VPush(background_color="white")]
    ]
game = [    
            [sg.Button("1",key="1",size=s,button_color=("black","white"),border_width=0),sg.Button("2",key="2",size=s,button_color=("black","white"),border_width=0),sg.Button("3",key="3",size=s,button_color=("black","white"),border_width=0)],
            [sg.Button("4",key="4",size=s,button_color=("black","white"),border_width=0),sg.Button("5",key="5",size=s,button_color=("black","white"),border_width=0),sg.Button("6",key="6",size=s,button_color=("black","white"),border_width=0)],
            [sg.Button("7",key="7",size=s,button_color=("black","white"),border_width=0,),sg.Button("8",key="8",size=s,button_color=("black","white"),border_width=0),sg.Button("9",key="9",size=s,button_color=("black","white"),border_width=0)],
            [sg.Push(background_color="white"),sg.Button("Return",key="back")]
    ]
win_lay = [
        [sg.VPush(background_color="black"),sg.Push(background_color="white"),sg.Text("",key="winner",text_color='black',background_color="white"),sg.Push(background_color="white"),sg.VPush(background_color="white")],
        

]


layout = [[sg.Column(menu,key="menu"),sg.Column(game,key="game",visible=False),sg.Column(win_lay,key="winpage",visible=False)]]


board =[
["","",""],
["","",""],
["","",""]
]
last = "O"




window = sg.Window('Introduction', layout)
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
        window["winner"].Update(f"{winner} wins!")


while True:
    state, values = window.read()

    if state in n:
        if last == "X":
            last ="O"
            window[state].Update(image_filename="Pyhton\\TicTacToe\\img\\O.png")
            if int(state) < 4:              
                board[0][int(state)-1] = 'O'
            elif int(state) <7:
                board[1][int(state)-4] = 'O'
            else:
                board[2][int(state)-7] = 'O'
        else:
            last ="X"
            window[state].Update(image_filename="Pyhton\\TicTacToe\\img\\X.png")
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

    logic()
    print(state)
    if state in (None, 'Exit'):
        break




    




