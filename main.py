import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from personne import Personne

root = tk.Tk()
root.title("Person Database")
root.geometry("600x400")
root.configure(background="#F4F4F4")

db = Database('moun.db')

# Styling
style = ttk.Style()
style.configure("TButton", background="#FF6B6B", foreground="#4949c6")
style.configure("TLabel", background="#F4F4F4", foreground="#4949c6")
style.configure("TEntry", background="#FFFFFF", fieldbackground="#4949c6")
style.configure("TText", background="#FFFFFF", foreground="#4949c6")

# Input Form Interface
def switch_to_input_form():
    display_frame.pack_forget()
    input_frame.pack()

def ajouter_personne():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    age = age_entry.get()
    ville = ville_entry.get()
    
    if nom and prenom and age and ville:
        try:
            age = int(age)  # Make sure age is a valid integer
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid integer for age.")
            return
        db.ajouter_personne(nom, prenom, age, ville)
        result_label.configure(text="Les informations ont été sauvegardées avec succès dans la base de données 'personnes.db'.")
        clear_input_fields()
        switch_to_display_form()  # Refresh the display table
    else:
        result_label.configure(text="Veuillez remplir tous les champs.", foreground="red")

# In the Database class:
def clear_input_fields():
    nom_entry.delete(0, tk.END)
    prenom_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    ville_entry.delete(0, tk.END)

# Display Form Interface
def switch_to_display_form():
    input_frame.pack_forget()
    display_frame.pack()
    afficher_personnes()

def afficher_personnes():
    personnes = db.recuperer_personnes()

    for row in table.get_children():
        table.delete(row)

    for personne in personnes:
        table.insert("", "end", values=(personne.id, personne.nom, personne.prenom, personne.age, personne.ville))

    result_label.configure(text="Les informations ont été récupérées avec succès depuis la base de données 'personnes.db'.")

# Input Form
input_frame = tk.Frame(root, bg="#F4F4F4")
input_label = ttk.Label(input_frame, text="Nouvelle Personne", font=("Helvetica", 16), background="#F4F4F4")

input_label.pack(pady=5)
result_label = ttk.Label(input_frame, text="", background="#F4F4F4")
result_label.pack()

nom_label = ttk.Label(input_frame, text="Nom:", background="#F4F4F4")
nom_label.pack()
nom_entry = ttk.Entry(input_frame)
nom_entry.pack()

prenom_label = ttk.Label(input_frame, text="Prénom:", background="#F4F4F4")
prenom_label.pack()
prenom_entry = ttk.Entry(input_frame)
prenom_entry.pack()

age_label = ttk.Label(input_frame, text="Âge:", background="#F4F4F4")
age_label.pack()
age_entry = ttk.Entry(input_frame)
age_entry.pack()

ville_label = ttk.Label(input_frame, text="Ville:", background="#F4F4F4")
ville_label.pack()
ville_entry = ttk.Entry(input_frame)
ville_entry.pack()

ajouter_button = ttk.Button(input_frame, text="Ajouter", command=ajouter_personne)
ajouter_button.pack(pady=10)

switch_to_display_button = ttk.Button(input_frame, text="Afficher", command=switch_to_display_form)
switch_to_display_button.pack()

# Display Form
display_frame = tk.Frame(root, bg="#F4F4F4")

display_label = ttk.Label(display_frame, text="Personnes enregistrées", font=("Helvetica", 16), background="#F4F4F4")
display_label.pack(pady=10)

table_frame = ttk.Frame(display_frame)
table = ttk.Treeview(table_frame, columns=("ID", "Nom", "Prénom", "Âge", "Ville"), show="headings")
table.heading("ID", text="ID")
table.heading("Nom", text="Nom")
table.heading("Prénom", text="Prénom")
table.heading("Âge", text="Âge")
table.heading("Ville", text="Ville")

table.column("ID", width=20)
table.column("Nom", width=150)
table.column("Prénom", width=150)
table.column("Âge", width=80)
table.column("Ville", width=150)

table.tag_configure("oddrow", background="#E8E8E8")
table.tag_configure("evenrow", background="#FFFFFF")

table.pack(padx=10, pady=10)
table_frame.pack(padx=10, pady=5)

switch_to_input_button = ttk.Button(display_frame, text="Retour", command=switch_to_input_form)
switch_to_input_button.pack(pady=10)

# Other Functions
def on_quit():
    db.fermer_connexion()
    root.destroy()

# Quit Button
quit_button = ttk.Button(root, text="Quitter", command=on_quit)
quit_button.pack(pady=10)

# Start the program
switch_to_input_form()
root.mainloop()

print("Fin du programme.")
