import customtkinter

# Criar a janela principal
window = customtkinter.CTk()
window.geometry("1400x900")

# Criar o texto da tela de cadastro
text = customtkinter.CTkLabel(window, text="Tela de Cadastro")
text.place(relx=0.5, rely=0.15, anchor="center")  # Centralizar o texto

# Criar os campos de entrada
fisrtname = customtkinter.CTkEntry(window, placeholder_text="First name")
fisrtname.place(relx=0.5, rely=0.25, anchor="center")

lastname = customtkinter.CTkEntry(window, placeholder_text="Last name")
lastname.place(relx=0.5, rely=0.30, anchor="center")

username = customtkinter.CTkEntry(window, placeholder_text="Username")
username.place(relx=0.5, rely=0.35, anchor="center")

emailone = customtkinter.CTkEntry(window, placeholder_text="Email")
emailone.place(relx=0.5, rely=0.40, anchor="center")

emailtwo = customtkinter.CTkEntry(window, placeholder_text="Confirm Email")
emailtwo.place(relx=0.5, rely=0.45, anchor="center")

password = customtkinter.CTkEntry(window, placeholder_text="Password")
password.place(relx=0.5, rely=0.50, anchor="center")

signup = customtkinter.CTkButton(window, text="Sign Up")
signup.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()
