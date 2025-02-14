import customtkinter as ctk
from PIL import Image, ImageTk

# visual of the window
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

# geometry window
window = ctk.CTk()
window.geometry("1400x900")
window.title("Tela de Login")

# Load the background image
bg_image = Image.open("C:/Users/Matheus.Rodrigues/Desktop/vscode/python/my_content/financeiro/my_program/background.jpg")
bg_image = bg_image.resize((1400, 900), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = ctk.CTkCanvas(window, width=1400, height=900)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# functions
def click():
    print("Logado!")

# login window
frame = ctk.CTkFrame(window, width=700, height=450, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center") 

text = ctk.CTkLabel(frame, text="Tela de Login", font=("Montserrat", 46))
text.place(relx=0.5, rely=0.15, anchor="center")

email = ctk.CTkEntry(frame, placeholder_text="Username", width=300, font=("Montserrat", 16))
email.place(relx=0.5, rely=0.35, anchor="center")

senha = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=300, font=("Montserrat", 16))
senha.place(relx=0.5, rely=0.45, anchor="center")

checkbox = ctk.CTkCheckBox(frame, text="Remember", font=("Montserrat", 16))
checkbox.place(relx=0.37, rely=0.55, anchor="center")

forgot = ctk.CTkLabel(frame, text="forgot your password?", text_color="darkblue", cursor="hand2", font=("Montserrat", 16))
forgot.place(relx=0.6, rely=0.55, anchor="center")

button = ctk.CTkButton(frame, text="Sign in", text_color="white", bg_color="darkblue", command=click, width=200)
button.place(relx=0.5, rely=0.7, anchor="center")

# function metod to put windows in loop to work
window.mainloop()
