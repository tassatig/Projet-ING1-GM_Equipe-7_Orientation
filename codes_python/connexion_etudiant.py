from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("600x480")
app.resizable(0,0)

side_img_data = Image.open("../images/side.jpg")
email_icon_data = Image.open("../images/email-icon.png")
password_icon_data = Image.open("../images/password-icon.png")


side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))


CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Bienvenue !", text_color="#133C55", anchor="w", justify="left", font=("Constantia", 30)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Connectez-vous à l'aide de vos identifiants ENT", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Identifiant", text_color="#386FA4", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#386FA4", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Mot de passe:", text_color="#386FA4", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#386FA4", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Login", fg_color="#386FA4", hover_color="#6A0136", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))



app.mainloop()
