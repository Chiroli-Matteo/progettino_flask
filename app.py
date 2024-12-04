from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inizializza l'app Flask
app = Flask(__name__)

# Configurazione del database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  # Percorso del database SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabilita il tracking delle modifiche per migliorare le prestazioni

# Inizializza l'estensione SQLAlchemy per la gestione del database
db = SQLAlchemy(app)

# Definizione del modello per la tabella "ListaSpesa" nel database
class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Colonna ID come chiave primaria
    elemento = db.Column(db.String(100), nullable=False)  # Colonna "elemento" non nulla con un limite di 100 caratteri

# Creazione del database e delle tabelle corrispondenti ai modelli, se non esistono già
with app.app_context():
    db.create_all()

# Rotta per visualizzare la lista della spesa
@app.route('/')
def home():
    # Recupera tutti gli elementi dalla tabella "ListaSpesa" e li passa al template
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista=lista_spesa)

# Rotta per aggiungere un nuovo elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    # Recupera il valore dell'input dal form HTML
    elemento = request.form['elemento']
    if elemento:  # Verifica che l'elemento non sia vuoto
        nuovo_elemento = ListaSpesa(elemento=elemento)  # Crea un nuovo oggetto "ListaSpesa"
        db.session.add(nuovo_elemento)  # Aggiunge l'elemento al database
        db.session.commit()  # Salva le modifiche nel database
    return redirect(url_for('home'))  # Reindirizza alla pagina principale

# Rotta per rimuovere un elemento specifico dalla lista
@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    # Cerca l'elemento da rimuovere nel database tramite il suo ID
    elemento_da_rimuovere = ListaSpesa.query.get(id)
    if elemento_da_rimuovere:  # Verifica che l'elemento esista
        db.session.delete(elemento_da_rimuovere)  # Rimuove l'elemento dal database
        db.session.commit()  # Salva le modifiche nel database
    return redirect(url_for('home'))  # Reindirizza alla pagina principale

# Rotta per svuotare completamente la lista della spesa
@app.route('/svuota', methods=['POST'])
def svuota_lista():
    ListaSpesa.query.delete()  # Cancella tutti i record dalla tabella "ListaSpesa"
    db.session.commit()  # Salva le modifiche nel database
    return redirect(url_for('home'))  # Reindirizza alla pagina principale

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)  # Esegue l'app in modalità debug per facilitare lo sviluppo
