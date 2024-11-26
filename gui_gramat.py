import PySimpleGUI as sg
import gramatu_klase

class BookApp:
    def __init__(self):
        self.book = None
        
        
layout = [ [sg.Text("Grāmatas nosaukums:"), sg.InputText(key="title")],
         [sg.Text("Autors:"), sg.InputText(key="author")],
         [sg.Text("Lapu skaits:"), sg.InputText(key="pages")],
         [sg.Text("Izlases lapu skaits:"), sg.InputText(key="pages_read")],
         [sg.Button("Parādīt lappušu skaitu"), sg.Button("Pārbaudīt")],
         [sg.Button("Pabeigt")],
         [sg.Text("", key="output")],
        ]
        
window = sg.Window('Grāmatas pārvaldnieks',layout)



while True:   
    event,value = window.read() 
    print(value)
    if event == "Parādīt lappušu skaitu":
        print(value["title"])
        objekts1 = gramatu_klase.Book(value["title"],value["author"],value["pages"])
        objekts1.read_pages(value["pages_read"])

    if event == "Pārbaudīt":
        print(objekts1.is_long_book())

    if event == sg.WINDOW_CLOSED or "Pabeigt":
        break

window.close()


