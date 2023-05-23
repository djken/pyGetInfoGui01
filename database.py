import sqlite3
from personne import Personne

class Database:
    def __init__(self, db_name):
        self.connexion = sqlite3.connect(db_name)
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personnes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                age INTEGER,
                ville TEXT
            )
        ''')
        self.connexion.commit()

    def ajouter_personne(self, nom, prenom, age, ville):
            self.cursor.execute("""
                INSERT INTO personnes (nom, prenom, age, ville) VALUES (?, ?, ?, ?)
            """, (nom, prenom, age, ville))
            self.connexion.commit()
            
    def recuperer_personnes(self):
        self.cursor.execute('''
            SELECT * FROM personnes
        ''')
        rows = self.cursor.fetchall()
        personnes = []
        for row in rows:
            personne = Personne(*row)  # Constructing the Personne object
            personnes.append(personne)
        return personnes

    def fermer_connexion(self):
        self.connexion.close()
