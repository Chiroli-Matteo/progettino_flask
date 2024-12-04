# Lista che memorizza gli elementi della spesa
lista_spesa = []


# Funzione per aggiungere un elemento alla lista
def aggiungi():
    x = str(input("Aggiungi un elemento alla lista \n"))  # Richiede all'utente di inserire un elemento
    lista_spesa.append(x)  # Aggiunge l'elemento alla lista


# Funzione per visualizzare tutti gli elementi della lista
def visualizza():
    for i in range(len(lista_spesa)):  # Itera su tutti gli indici della lista
        print(f"{i + 1}. {lista_spesa[i]}")  # Stampa l'indice (a partire da 1) e l'elemento corrispondente


# Funzione per rimuovere un elemento specifico dalla lista
def rimuovi():
    x = input("Inserisci elemento da rimuovere\n")  # Richiede all'utente di specificare l'elemento
    if x in lista_spesa:  # Verifica se l'elemento esiste nella lista
        lista_spesa.remove(x)  # Rimuove l'elemento
        print(f"L'elemento '{x}' è stato rimosso.")  # Messaggio di conferma
    else:
        print(f"L'elemento '{x}' non è presente nella lista.")  # Messaggio di errore se l'elemento non esiste


# Funzione per contare le occorrenze di ogni elemento nella lista
def conta():
    x = set(lista_spesa)  # Converte la lista in un set per eliminare i duplicati
    for i in x:  # Itera su ogni elemento unico
        occorrenze = lista_spesa.count(i)  # Conta quante volte l'elemento appare nella lista
        if occorrenze > 1:
            print(f"L'elemento '{i}' appare {occorrenze} volte.")
        else:
            print(f"L'elemento '{i}' appare {occorrenze} volta.")


# Funzione per svuotare completamente la lista
def svuota_lista():
    lista_spesa.clear()  # Elimina tutti gli elementi dalla lista
    print("La lista è stata svuotata.")  # Messaggio di conferma


# Ciclo principale del programma
while True:
    # Menu interattivo per l'utente
    print(" premi 0 per uscire,")
    print(" premi 1 per aggiungere un elemento,")
    print(" premi 2 per visualizzare la lista,")
    print(" premi 3 per eliminare un elemento,")
    print(" premi 4 per contare gli elementi della lista,")
    print(" premi 5 per svuotare la lista")
    
    # Legge la scelta dell'utente e la converte in un intero
    x = int(input(""))
    
    # Gestisce le varie opzioni in base all'input dell'utente
    if x == 0:
        break  # Esce dal ciclo e termina il programma
    elif x == 1:
        aggiungi()  # Chiama la funzione per aggiungere un elemento
    elif x == 2:
        visualizza()  # Chiama la funzione per visualizzare la lista
    elif x == 3:
        rimuovi()  # Chiama la funzione per rimuovere un elemento
    elif x == 4:
        conta()  # Chiama la funzione per contare gli elementi
    elif x == 5:
        svuota_lista()  # Chiama la funzione per svuotare la lista
    else:
        print("Opzione non valida. Riprova.")  # Messaggio di errore per input non valido
