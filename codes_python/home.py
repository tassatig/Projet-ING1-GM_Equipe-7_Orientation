import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image

# Palette de couleurs
primary_color = "#0056b3"  # Couleur bleue primaire
secondary_color = "#ffffff"  # Couleur blanche

app = ctk.CTk()
app.title("CYTech Oriente")
app.geometry("800x700")

# Configurer les couleurs de l'interface
ctk.set_appearance_mode("light")  # Thème clair
ctk.set_default_color_theme("blue")  # Thème de couleur par défaut

# Ajouter le logo
logo_image = PhotoImage(file="../images/logo1.png")  # Assurez-vous que le chemin du logo est correct
logo_label = ctk.CTkLabel(master=app, image=logo_image, text="")
logo_label.pack(pady=20)


# Ajouter le titre
custom_font = ("Constantia", 30)
title_label = ctk.CTkLabel(master=app, text="CYTech Oriente", font=custom_font, text_color=primary_color, )
title_label.pack(pady=10)

        #title_label = ctk.CTkLabel(app, text="CYTech Oriente", font=custom_font, text_color=primary_color)
        #title_label.pack(pady=10)



# Ajouter les boutons

button_frame = ctk.CTkFrame(app)
button_frame.pack()

        # Créer un label dans le cadre des boutons
custom_font = ("Times New Roman", 20)
title_label = ctk.CTkLabel(master=button_frame, text="Vous êtes: ", font=custom_font, text_color="#2F3061")
title_label.pack(anchor="s", expand=True, pady=10, padx=30)


student_button = ctk.CTkButton(button_frame, text="Étudiant", width=90, height=40, font=("Helvetica", 16),corner_radius=30,border_width=3,border_color="#003d80", fg_color=primary_color, hover_color="#003d80")
student_button.pack(pady=10, padx=20)

admin_button = ctk.CTkButton(button_frame, text="Administrateur", width=90, height=40, font=("Helvetica", 16),corner_radius=30,border_width=3,border_color="#003d80", fg_color=primary_color, hover_color="#003d80")
admin_button.pack(pady=10, padx=20)
        #admin_button = ctk.CTkButton(master= button_frame, text="Administrateur", width=200, height=40, font=("Helvetica", 16), fg_color=primary_color, hover_color="#003d80")
        #admin_button.grid(row=0, column=1, padx=20, pady=10)
title_label = ctk.CTkLabel(master=app, text="", font=custom_font, text_color="#2F3061")
title_label.pack(anchor="s", expand=True, pady=10, padx=30)

logo2_image = PhotoImage(file="../images/Logo_CY_Cergy_Paris_Universite.png")  # Assurez-vous que le chemin du logo est correct

#logo2_label = ctk.CTkImage(dark_image=logo2_image, light_image=logo2_image)
logo2_label = ctk.CTkLabel(master=app, image=logo2_image, text="")
logo2_label.pack(pady=20)


#logo_image = PhotoImage(file="H:\\Desktop\\ING1\\projet_fin_annee\\Logo_CY_Cergy_Paris_Universite.png")  # Assurez-vous que le chemin du logo est correct
#logo_label = ctk.CTkLabel(master=app, image=logo_image, text="")
#logo_label.pack(pady=20)

app.mainloop()
