from flask import Flask, render_template, request, redirect, url_for

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
 return "Per ora funziona tutto"

#avvio dell'app Flask
if __name__ == '__main__':
 app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

lista_spesa = []
# Definisce una route per il percorso '/aggiungi', che accetta solo richieste POST
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:index>', methods=['POST'])
def rimuovi(index):
    if 0 <= index < len(lista_spesa):
        lista_spesa.pop(index)
    return redirect(url_for('home'))

@app.route('/svuota_lista', methods=['POST'])
def svuota_lista():
    lista_spesa.clear()  # Svuota la lista
    return redirect(url_for('home'))  # Reindirizza alla home

if __name__ == '__main__':
    app.run(debug=True)