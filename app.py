from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inizializza l'app Flask
app = Flask(__name__)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db = SQLAlchemy(app)

# Modello per la tabella ListaSpesa
class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chiave primaria univoca
    elemento = db.Column(db.String(100), nullable=False)  # Colonna non nulla

# Creazione del database e delle tabelle
with app.app_context():
    db.create_all()

# Rotta per visualizzare la lista
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()  # Recupera tutti gli elementi dal database
    return render_template('index.html', lista=lista_spesa)

# Rotta per aggiungere un nuovo elemento
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento)
        db.session.commit()
    return redirect(url_for('home'))

# Rotta per rimuovere un elemento specifico
@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento_da_rimuovere = ListaSpesa.query.get(id)
    if elemento_da_rimuovere:
        db.session.delete(elemento_da_rimuovere)
        db.session.commit()
    return redirect(url_for('home'))

# Rotta per svuotare l'intera lista
@app.route('/svuota', methods=['POST'])
def svuota_lista():
    ListaSpesa.query.delete()  # Cancella tutti gli elementi dalla tabella
    db.session.commit()
    return redirect(url_for('home'))

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
