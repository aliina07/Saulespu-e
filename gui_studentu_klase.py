import PySimpleGUI as sg
import studentu_klase


layout = [
    
        [sg.Text("Studenta Informācija")],
        [sg.Text("Name"), sg.InputText(key="name")],
        [sg.Text("Student ID"), sg.InputText(key="student_id")],
        [sg.Text("Grade (0-10)"), sg.InputText(key="grade")],
        [sg.Button("Add grade"), sg.Button("Aprēķināt vidējo")],
        [sg.Text("", key="error", text_color="red")],
        [sg.Text("Average Grade:"), sg.Text("", key="average")],

]


window = sg.Window("Student Grades", layout)


while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Add Grade":
            try:
                grade = float(values["grade"])
                if not student:
                    student = student(values["name"], values["student_id"])

                student.add_grade(grade)
                window["error"].update("")  
            except ValueError:
                window["error"].update("Lūdzu, ievadiet derīgu atzīmei.")

window.close()
