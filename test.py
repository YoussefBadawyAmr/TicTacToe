import PySimpleGUI as sg


def main():
    column_to_be_centered = [[sg.Text('My Window')],
                             [sg.Input(key='-IN-')],
                             [sg.Text(size=(12, 1), key='-OUT-')],
                             [sg.Button('Go'), sg.Button('Exit')]]

    layout = [[sg.VPush()],
              [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
              [sg.VPush()]]

    # Create the window
    window = sg.Window(
        "Demo application",
        layout,
        size=(500, 500)
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        break

    window.close()


if __name__ == '__main__':
    main()