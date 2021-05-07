from tkinter import *
from tkinter import ttk

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

PELICULA = StringVar()
HORA = StringVar()
FECHA = StringVar()
IDIOMA = StringVar()

def Inserte_Pelicula():
    PELICULA = entry_PELICULA.get()
    HORA = entry_HORA.get()
    FECHA = entry_FECHA.get()
    IDIOMA = entry_IDIOMA.get()
    cine_db = cine_database.MyDatabase()
    cine_db.insert_db(PELICULA, HORA, FECHA, IDIOMA)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="CINE LOVE",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="SALAS DE CINE", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_form.place(x=25, y=5)
label_PELICULA = Label(frame_form, 
              text="Sala:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_PELICULA.place(x=30, y=30)
entry_PELICULA = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_PELICULA.place(x=30, y=70)

label_HORA = Label(frame_form, 
              text="Butakas:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_HORA.place(x=30, y=100)
entry_HORA = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_HORA.place(x=30, y=140)

label_FECHA = Label(frame_form, 
              text="Boletos:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_FECHA.place(x=30, y=170)
entry_FECHA = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_FECHA.place(x=30, y=210)

label_IDIOMA = Label(frame_form, 
              text="Precio:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_IDIOMA.place(x=30, y=240)
entry_IDIOMA = Entry(frame_form, justify=LEFT, width=25,
               font=("Century Gothic", "14"))
entry_IDIOMA.place(x=30, y=280)

button_agregar = Button(frame_form, text="Crear sala", 
                        font=("Century Gothic", "14", "bold")),command=Inserte_Pelicula
button_agregar.place(x=110, y=350)

window.mainloop()