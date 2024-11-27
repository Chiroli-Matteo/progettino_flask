from flask import Flask
6.
7. #inizializza l'app Flask
8. app = Flask(__name__)
9.
10.#rotta principale
11.@app.route('/')
12.def home():
13. return "Per ora funziona tutto"
14.
15.#avvio dell'app Flask
16.if __name__ == '__main__':
17. app.run(debug=True)