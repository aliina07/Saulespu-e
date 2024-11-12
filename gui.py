import PySimpleGUI as sg # vizuālās saskarsnes biblotēka
import ladite_OOP as ladite

#Funkcijas, klases
# Failā ladite_OOP.py
#Lietotāja saskarne priekš programas lādīte

sg.theme('DarkAmber') #saskarnes tēma
#izskārtojums
layout = [[sg.Text("Sveicināti")], #Vizuālā daļa
         [sg.Text('Vārds'),sg.InputText()],
         [sg.Text('Vēltījums'),sg.InputText()],
         [sg.Text('Augstums'),sg.InputText()],
         [sg.Text('Platums'),sg.InputText()],
         [sg.Text('Garums'),sg.InputText()],
         [sg.Text('Materiāla cenu (EUR/m2)'),sg.InputText()],
         [sg.Button("Prādīt rēķinu konsolē"),sg.Button("Saglabāt rēķinu")]
         ]

window = sg.Window('Rēķinu izveide',layout) #loga izveide

while True:   #saskarsnes darbības cikls
    event,Value = window.read() # notikumu un vērtību pārbaude
    if event == "Prādīt rēķinu konsolē":
        print(Value[0])
        rekins = ladite.Rekins(Value[0],Value[1],[int(Value[3]),int(Value[4]),int(Value[2])],int(Value[5]))
        rekins.izdrukat()
    if event == "Saglabāt rēkinu":
        rekins.saglabat()
    if event == sg.WINDOW_CLOSED:#ja aizver lodziņu
        break

window.close()