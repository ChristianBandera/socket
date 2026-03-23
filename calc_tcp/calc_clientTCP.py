#CLIENT
import socket
import json

HOST = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))

    while True:
        try:
            primoNumero = float(input("Inserisci il primo numero: "))
            break  
        except ValueError:
            print("Errore: devi inserire un numero valido, non lasciare vuoto o inserire lettere!")

    while True:
        operazione = input("Inserisci l'operazione (+, -, *, /): ")
        if operazione in ["+", "-", "*", "/"]:
            break
        else:
            print("Errore: operatore non valido.")

    while True:
        try:
            secondoNumero = float(input("Inserisci il secondo numero: "))
            break  # Se la conversione in float ha successo, esce dal ciclo
        except ValueError:
            print("Errore: devi inserire un numero valido, non lasciare vuoto o inserire lettere!")

    messaggio = {
        "primoNumero": primoNumero,
        "operazione": operazione,
        "secondoNumero" : secondoNumero
    }
    messaggio = json.dumps(messaggio)

    sock_service.sendall(messaggio.encode("UTF-8")) 
    data = sock_service.recv(BUFFER_SIZE)

print("Risultato", data.decode())