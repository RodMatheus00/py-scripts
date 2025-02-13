import customtkinter
import webbrowser

# Configuração do tema
customtkinter.set_appearance_mode("dark")  # Tema escuro
customtkinter.set_default_color_theme("dark-blue")

# Criar a janela principal
window = customtkinter.CTk()
window.geometry("1400x900")
window.title("Tela de Login")

def click():
    print("Logado!")

def abrir_link():
    webbrowser.open("https://www.seusite.com")  # Altere para seu link desejado

# Criar um frame centralizado (quadrado de 700x450)
frame = customtkinter.CTkFrame(window, width=700, height=450, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame

# Título
text = customtkinter.CTkLabel(frame, text="Tela de Login", font=("Montserrat", 46))
text.place(relx=0.5, rely=0.15, anchor="center")

# Campo de e-mail
email = customtkinter.CTkEntry(frame, placeholder_text="Username", width=300, font=("Montserrat", 16))
email.place(relx=0.5, rely=0.35, anchor="center")

# Campo de senha
senha = customtkinter.CTkEntry(frame, placeholder_text="Password", show="*", width=300, font=("Montserrat", 16))
senha.place(relx=0.5, rely=0.45, anchor="center")

# Checkbox "Remember login"
checkbox = customtkinter.CTkCheckBox(frame, text="Remember", font=("Montserrat", 16))
checkbox.place(relx=0.37, rely=0.55, anchor="center")

# Link clicável
link = customtkinter.CTkLabel(frame, text="Esqueceu a senha?", text_color="darkblue", cursor="hand2", font=("Montserrat", 16))
link.place(relx=0.5, rely=0.6, anchor="center")
link.bind("<Button-1>", lambda e: abrir_link())  # Associa o clique ao link

# Botão de login
botao = customtkinter.CTkButton(frame, text="Sign in", text_color="light", bg_color="darkblue", command=click, width=200)
botao.place(relx=0.5, rely=0.7, anchor="center")

# Iniciar a aplicação
window.mainloop()
