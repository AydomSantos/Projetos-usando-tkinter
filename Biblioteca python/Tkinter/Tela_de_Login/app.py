import tkinter as tk 
from tkinter import messagebox

# Cores
cores_um = "#F39421"  # laranja
cores_dois = "#F4F8F9"  # branco
cores_quatro = "#FFFFFF"  # branco

# Criação da janela principal
root = tk.Tk()

# funções do app

# valida nome de usuario e senha 
def valida_login():
    user_name = "Aydom"
    user_senha = "12345"

    if root_input_name.get() == user_name and root_input_senha.get() == user_senha:
       messagebox.showinfo(title="Login Success", message="Voçê esta Logado !")
    else:
        messagebox.showerror(title="Erro", message="Acesso negado !! verifique se as informações estão corretas")

# Título da Aplicação
root.title("Login Form")

# Define a largura e a altura da janela
root.geometry("500x760")

# Cor de fundo da aplicação
root.configure(bg=cores_dois)

# Configuração das colunas e linhas da janela principal para centralização
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Construção do app

# Criar um frame (container) com largura e altura definidas
frame_container = tk.Frame(root, width=280, height=300, padx=10, pady=10, bg=cores_quatro)
frame_container.grid(row=0, column=0)  # Centralizar o frame na janela principal
frame_container.grid_propagate(False)  # Evitar que o frame se redimensione automaticamente

# Criação do campo do formulário de login
root_label = tk.Label(frame_container, text="Login", font=("Helvetica", 20, "bold"), bg=cores_quatro)
root_label_name = tk.Label(frame_container, text="Username", bg=cores_quatro)
root_input_name = tk.Entry(frame_container)
root_label_senha = tk.Label(frame_container, text="Password", bg=cores_quatro)
root_input_senha = tk.Entry(frame_container, show="*")
root_button = tk.Button(frame_container, text="Login", bg=cores_um, fg=cores_dois, relief=tk.FLAT, 
                        width=20, height=2, command=valida_login)

# Posicionamento dos elementos dentro do frame
root_label.place(relx=0.5, rely=0.1, anchor="center")
root_label_name.place(relx=0.3, rely=0.37, anchor="center")
root_input_name.place(relx=0.7, rely=0.37, anchor="center")
root_label_senha.place(relx=0.3, rely=0.5, anchor="center")
root_input_senha.place(relx=0.7, rely=0.5, anchor="center")
root_button.place(relx=0.5, rely=0.8, anchor="center")

# Chamada do app
root.mainloop()
