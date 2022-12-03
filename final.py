import threading
import PySimpleGUI as sg

sg.theme_background_color("white")
s = (19,10)
n = "123456789"
winner = ["123","456","789","159","357","147","258","369"]

global state , values , window ,game , menu ,last
lay_list = ["menu","game"]
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

pop = [
        [sg.VPush(background_color="white"),sg.Push(background_color="white"),sg.Text(key="winner"),sg.VPush(background_color="white"),sg.Push(background_color="white")]

]

layout = [[sg.Column(menu,key="menu"),sg.Column(game,key="game",visible=False)]]

board =[
[6,6,6],
[6,6,6],
[6,6,6]
]




last = "O"




window = sg.Window('Introduction', layout)

while True:
    state, values = window.read()

    if state in n:
        if last == "X":
            last ="O"
            window[state].Update(image_filename="Pyhton\\TicTacToe\\img\\O.png")
            if int(state) < 4:              
                board[0][int(state)-1] = 0
            elif int(state) <7:
                board[1][int(state)-4] = 0
            else:
                board[2][int(state)-7] = 0
        else:
            last ="X"
            window[state].Update(image_filename="Pyhton\\TicTacToe\\img\\X.png")
            if int(state) < 4:              
                board[0][int(state)-1] = 1
            elif int(state) <7:
                board[1][int(state)-4] = 1
            else:
                board[2][int(state)-7] = 1
    elif state == "start" :
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow+1]].Update(visible = True)
        laynow+=1
    elif state == "back":
        window[lay_list[laynow]].Update(visible = False)
        window[lay_list[laynow-1]].Update(visible = True)
        laynow-=1
    print(state)
    if state in (None, 'Exit'):
        break




    




