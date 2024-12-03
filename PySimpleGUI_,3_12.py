import PySimpleGUI as sg
import Api_trenin_uzd 

layout = [ 
   
       [sg.Text("Nospiediet pogu, lai ielādēt datus:")],
         [sg.Button("Ielādēt datus")],
         [sg.Text(key="result")],
        ]

window = sg.Window('dati',layout)

while True:
    event,values = window.read()
    if event == "Ielādēt datus":
    
     window["result"].update(Api_trenin_uzd.info())
    if event == sg.WINDOW_CLOSED:
        break

window.close()



 