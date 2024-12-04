from flask_sqlalchemy import SQLAlchemy

# Inizializza SQLAlchemy
db = SQLAlchemy()

# Modello per la tabella ListaSpesa
class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chiave primaria univoca
    elemento = db.Column(db.String(100), nullable=False)  # Colonna non nulla
