import threading
import PySimpleGUI as sg

sg.theme_background_color("white")
s = (19,10)
n = "123456789"
winner = ["123","456","789","159","357","147","258","369"]
menu = [
        [sg.Push(background_color = "white"),sg.Text("**********************Welcome**********************",background_color="white",text_color="black"),sg.Push(background_color = "white")],
        [sg.VPush(background_color="white"),sg.Push(background_color = "white"),sg.Button(key = "start",image_filename="img\\Start.png",button_color="white",border_width=0),sg.Push(background_color = "white"),sg.VPush(background_color="white")]
    ]
game = [
            [sg.Button("1",key="1",size=s,button_color=("black","white"),border_width=0),sg.Button("2",key="2",size=s,button_color=("black","white"),border_width=0),sg.Button("3",key="3",size=s,button_color=("black","white"),border_width=0)],
            [sg.Button("4",key="4",size=s,button_color=("black","white"),border_width=0),sg.Button("5",key="5",size=s,button_color=("black","white"),border_width=0),sg.Button("6",key="6",size=s,button_color=("black","white"),border_width=0)],
            [sg.Button("7",key="7",size=s,button_color=("black","white"),border_width=0,),sg.Button("8",key="8",size=s,button_color=("black","white"),border_width=0),sg.Button("9",key="9",size=s,button_color=("black","white"),border_width=0)]
    ]
last = "O"
board =[
[6,6,6],
[6,6,6],
[6,6,6]
]


class app():
    def __init__(self):
        w = threading.Thread(target=self.windw)
        w.start()

        l = threading.Thread(target=self.logic)
        l.start()

        
    def windw(self):
        self.window = sg.Window('Introduction', game)
        while True:
            self.event, self.values = self.window.read()
            
            if self.event in (None, 'Exit'):
                break
    def logic(self):
        while True:
            if self.event in n:
                if last == "X":
                    last ="O"
                    self.window[self.event].Update(image_filename="img\\O.png")
                    if int(self.event) < 4:              
                        board[0][int(self.event)-1] = 0
                    elif int(self.event) <7:
                        board[1][int(self.event)-4] = 0
                    else:
                        board[2][int(self.event)-7] = 0
                else:
                    last ="X"
                    self.window[self.event].Update(image_filename="img\\X.png")
                    if int(self.event) < 4:              
                        board[0][int(self.event)-1] = 1
                    elif int(self.event) <7:
                        board[1][int(self.event)-4] = 1
                    else:
                        board[2][int(self.event)-7] = 1
        

app()