import PySimpleGUI as G_u_i
from TextManager import FileProcessing as Fp

G_u_i.theme('BluePurple')   # G_u_i.theme_previewer() można sprawdzić
# All the stuff inside your window.

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis hendrerit non libero imperdiet condimentum."
text_dict = Fp.FileProcessing.get_data_from_xml()

"""
layout = [[G_u_i.Text('Siema świat!')],
          [G_u_i.Text('No weź coś napisz ;-;'), G_u_i.InputText(key="-IN-")],
          [G_u_i.Button('Jestem koksem'), G_u_i.Button('Jestem leszczem')]]
"""

# TODO
'''layout = [[G_u_i.Text(text_pack.text_list[0])],
          [G_u_i.Text(text_pack.text_list[1])],
          [G_u_i.Text(text_pack.text_list[2])],
          [G_u_i.Text(text_pack.text_list[3])]]
'''

# Create the Window
window = G_u_i.Window('Moje pierwsze GUI(nea pig)', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == G_u_i.WIN_CLOSED or event == 'Jestem leszczem':  # if user closes window or clicks cancel
        break
    else:
        print('Dobra z ciebie morda! Napisałeś ', values["-IN-"])

window.close()
