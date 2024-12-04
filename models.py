from flask_sqlalchemy import SQLAlchemy

# Inizializza SQLAlchemy
# SQLAlchemy è una libreria che fornisce strumenti per interagire con il database in modo ORM (Object Relational Mapping)
db = SQLAlchemy()

# Modello per la tabella "ListaSpesa"
# Ogni modello in SQLAlchemy rappresenta una tabella nel database
class ListaSpesa(db.Model):  
    # Definizione delle colonne della tabella:
    id = db.Column(db.Integer, primary_key=True)  
    # "id" è un intero che funge da chiave primaria. È unico per ogni riga nella tabella
    
    elemento = db.Column(db.String(100), nullable=False)  
    # "elemento" è una stringa con un massimo di 100 caratteri. Non può essere nullo (campo obbligatorio)
