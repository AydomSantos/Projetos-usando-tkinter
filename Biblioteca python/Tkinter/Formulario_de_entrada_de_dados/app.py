import tkinter as tk
from tkinter import ttk

# Define constantes de cores
cores_um = "#F39421"  # Laranja
cores_dois = "#F4F8F9"  # Branco
cores_quatro = "#FFFFFF"  # Branco

# Inicialize o estilo

# Cria a janela principal
root = tk.Tk()
root.title('Formulário de Entrada de Dados')
root.geometry("700x560")  # Define as dimensões da janela
root.configure(bg=cores_dois,  pady=20)  # Define a cor de fundo

# Configura colunas e linhas para centralização
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Cria um frame de container
frame_container = tk.Frame(root, bg=cores_quatro, padx=20, pady=20)
frame_container.pack()

# Cria um frame com rótulo para informações do usuário
frame_label_userInfo_container = tk.LabelFrame(frame_container, text="Informações do Usuário", padx=16, pady=16, bg=cores_quatro)
frame_label_userInfo_container.grid(row=0, column=0)

# Rótulos para nome e sobrenome
frame_label_nameFirst = tk.Label(frame_label_userInfo_container, text="Nome", bg=cores_quatro)
frame_label_nameFirst.grid(row=0, column=0)

frame_label_lastName = tk.Label(frame_label_userInfo_container, text="Sobrenome", bg=cores_quatro)
frame_label_lastName.grid(row=0, column=1)

# Campos de entrada para nome e sobrenome
frame_label_nameFirst_input = tk.Entry(frame_label_userInfo_container)
frame_label_nameFirst_input.grid(row=1, column=0)

frame_label_lastName_input = tk.Entry(frame_label_userInfo_container)
frame_label_lastName_input.grid(row=1, column=1)

# Rótulo e combobox para título
title_label = tk.Label(frame_label_userInfo_container, text="Título", bg=cores_quatro)
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(frame_label_userInfo_container, values=["", "Sr.", "Sra.", "Dr."])
title_combobox.grid(row=1, column=2)

# Rótulo e spinbox para idade
age_label = tk.Label(frame_label_userInfo_container, text="Idade", bg=cores_quatro)
age_label.grid(row=2, column=0)

age_spinbox = tk.Spinbox(frame_label_userInfo_container, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

# Rótulo e combobox para nacionalidade
nationality_label = tk.Label(frame_label_userInfo_container, text="Nacionalidade", bg=cores_quatro)
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(frame_label_userInfo_container, values=["", "Afegão", "Albanês", "Argelino", "Andorrano", "Argentino", "Australiano", "Austríaco"])
nationality_combobox.grid(row=3, column=1)

# Ajusta o espaçamento interno dos widgets
for widget in frame_label_userInfo_container.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tk.LabelFrame(frame_container, bg=cores_quatro)
courses_frame.grid(row=1, column=0, sticky="news", pady=10)

registered_label = tk.Label(courses_frame, text="Status de Registro", bg=cores_quatro)
registered_label.grid(row=0, column=0)

registered_check = tk.Checkbutton(courses_frame, text="Atualmente Registrado", bg=cores_quatro)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="# Completed Courses", bg=cores_quatro)
numcourses_label.grid(row=0, column=1)

numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(courses_frame, text="# Semesters", bg=cores_quatro)
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_spinbox.grid(row=1, column=2)



for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Inicia o programa
root.mainloop()
