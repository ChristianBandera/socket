import socket
import json

IP = "127.0.0.1"
PORTA = 5005
DIM_BUFFER = 1024

#creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP, PORTA))

    #metto la socket in ascolto per le connessioni in ingresso
    sock_server.listen()

    print(f"Server in ascolto su {IP}:{PORTA}")

    #Loop principale del server
    while True:
        #accetta le connessioni
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:

            #leggi i dati inviati dal client
            data = sock_client.recv(DIM_BUFFER).decode()

            data = json.loads(data)
            primoNumero = data["primoNumero"]
            operazione = data["operazione"]
            secondoNumero = data["secondoNumero"]

            #invio risposta al client
            reply = ""
            if operazione == "+":
                reply = int((primoNumero + secondoNumero))
            elif operazione == "-":
                reply = int((primoNumero - secondoNumero))
            elif operazione == "*":
                reply = int((primoNumero * secondoNumero))
            elif operazione == "/":
                reply = int((primoNumero / secondoNumero))

            #stampa il messaggio ricevuto e invia una risposta al client
            print("Calcoli arrivati dal client: ", primoNumero, operazione, secondoNumero)
            sock_client.sendall(str(reply).encode())