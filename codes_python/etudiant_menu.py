import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from PIL import Image

primary_color="#133C55"
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("./TrojanBlue.json")  # Themes: "blue" (standard), "green", "dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

etudiant_menu=ctk.CTk()

etudiant_menu.title("CustomTkinter complex_example.py")
etudiant_menu.geometry("800x700")
logout_image=Image.open("../images/logout.png")
#ligne1 = ctk.CTkLabel(master=etudiant_menu text="Se déconnecter", width=600, height=20)
#ligne1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
logout=ctk.CTkButton(master=etudiant_menu,text="Se déconnecter",image= ctk.CTkImage(dark_image=logout_image,light_image=logout_image),corner_radius=32,border_width=2)
logout.grid(row=0, column=0, padx=(10,620), pady=10, sticky="nsew")

menu_commandes = ctk.CTkTabview(etudiant_menu, width=790,height=550)
menu_commandes.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
menu_commandes.add("Liste de voeux")
menu_commandes.add("Consulter les options")
menu_commandes.add("Consulter les résultats")

#titre1=ctk.CTkFrame(master=,bg_color="white",corner_radius=40)
Label1=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Liste des voeux", text_color="#c2620c", anchor="w",bg_color="white" ,
justify="center",font=("Constantia", 50)).pack(anchor="w", pady=20, padx=(230, 0))

choix1=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Option 1", text_color="white",font=("Constantia", 20),justify="left")
choix1.pack(padx=10, pady=(20, 5))

optionmenu_1 = ctk.CTkOptionMenu(menu_commandes.tab("Liste de voeux"), dynamic_resizing=True,values=["Intelligence Artificielle", "Data Science", "Fintech","Business Intelligence"])
optionmenu_1.pack(padx=20, pady=(20, 5))

choix2=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Option 2", text_color="white",font=("Constantia", 20),justify="left")
choix2.pack(padx=20, pady=(20, 5))

optionmenu_2 = ctk.CTkOptionMenu(menu_commandes.tab("Liste de voeux"), dynamic_resizing=True,values=["Intelligence Artificielle", "Data Science", "Fintech","Business Intelligence"])
optionmenu_2.pack(padx=20, pady=(20, 5))

choix3=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Option 3", text_color="white",font=("Constantia", 20),justify="left")
choix3.pack(padx=20, pady=(20, 5))

optionmenu_3 = ctk.CTkOptionMenu(menu_commandes.tab("Liste de voeux"), dynamic_resizing=True,values=["Intelligence Artificielle", "Data Science", "Fintech","Business Intelligence"])
optionmenu_3.pack(padx=20, pady=(20, 5))

choix4=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Option 4", text_color="white",font=("Constantia", 20),justify="left")
choix4.pack(padx=20, pady=(20, 5))

optionmenu_4 = ctk.CTkOptionMenu(menu_commandes.tab("Liste de voeux"), dynamic_resizing=True,values=["Intelligence Artificielle", "Data Science", "Fintech","Business Intelligence"])
optionmenu_4.pack(padx=20, pady=(20, 5))

choix5=ctk.CTkLabel(master=menu_commandes.tab("Liste de voeux"), text="Option 5", text_color="white",font=("Constantia", 20),justify="left")
choix5.pack(padx=20, pady=(20, 5))

optionmenu_5 = ctk.CTkOptionMenu(menu_commandes.tab("Liste de voeux"), dynamic_resizing=True,values=[""])
optionmenu_5.pack(padx=20, pady=(20, 5))
#choix1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
etudiant_menu.mainloop()
