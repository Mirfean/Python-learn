from Core import BasicClass
import PySimpleGUI as G_u_i
import TextManager.TextPrep as Tp

myBasicClass = BasicClass.BasicClass()
text_prep = Tp.TextPreparer()

# print(text_prep['Quest']['box']['id'])

boxes = text_prep.create_box_list()

current_box = boxes[0]

# GUI preparation
G_u_i.theme('BluePurple')

layout = [[G_u_i.Text(current_box.description)],
          [G_u_i.Text(current_box.answers[0].text)],
          [G_u_i.Text(current_box.answers[1].text)],
          [G_u_i.Text(current_box.answers[2].text)]]


window = G_u_i.Window('First Quest', layout)

while True:
    event, values = window.read()
    if event == G_u_i.WIN_CLOSED or event == 'Jestem leszczem':  # if user closes window or clicks cancel
        break
    else:
        print('Dobra z ciebie morda! Napisałeś ', values["-IN-"])

window.close()
