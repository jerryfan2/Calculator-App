import PySimpleGUI as sg

bsize = (5, 1)
bfont = ("Franklin Gothic Book", 24)
regb_specs = {"size": bsize, "font": bfont, "button_color": "teal"}

left_layout = [[sg.Button("C", size=bsize, font=bfont, button_color="light green"),
                sg.Button("CE", size=bsize, font=bfont,
                          button_color="light green"),
                sg.Button("+", **regb_specs)],
               [sg.Button("7", **regb_specs), sg.Button("8", **regb_specs),
                sg.Button("9", **regb_specs)],
               [sg.Button("4", **regb_specs), sg.Button("5", **regb_specs),
                sg.Button("6", **regb_specs)],
               [sg.Button("1", **regb_specs), sg.Button("2", **regb_specs),
                sg.Button("3", **regb_specs)],
               [sg.Button("0", size=(11, 1), font=bfont, button_color="teal"),
                sg.Button(".", **regb_specs)]
               ]
right_column_layout = [
    [sg.Button("-", **regb_specs)],
    [sg.Button("/", **regb_specs)],
    [sg.Button("*", **regb_specs)],
    [sg.Button("=", size=(5, 3), font=bfont, button_color="red")]
]

layout = [
    [sg.Text("0", font=("Times New Roman", 48), size=(50, 1), justification='right',
             background_color="white", text_color="black", key="-DISPLAY-")],
    [sg.Column(left_layout, background_color="#6fd7dc"),
     sg.Column(right_column_layout, background_color="#6fd7dc")]
]

window = sg.Window("Simple Calculator", layout,
                   size=(464, 528), margins=(30, 30), background_color="#6fd7dc")


equation_text = ""


def num_operator(event):
    global equation_text
    equation_text += event

    window["-DISPLAY-"].update(equation_text)


def equal_pressed():
    global equation_text
    equation_text = str(eval(equation_text))

    window["-DISPLAY-"].update(equation_text)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', "+", "-", "*", "/", ]:
        num_operator(event)
    if event == "=":
        try:
            equal_pressed()
        except:
            equation_text = ""
            window["-DISPLAY-"].update("ERROR")
    if event == "C":
        equation_text = ""
        window["-DISPLAY-"].update("0")
    if event == "CE":
        equation_text = equation_text[:-1]
        window["-DISPLAY-"].update(equation_text)

window.close()
