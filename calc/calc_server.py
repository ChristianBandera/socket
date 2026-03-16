import socket 
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

#creazione del socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di calcoli...")

while True:
    #ricezione dati
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal client {addr}: {data.decode()}")

    if not data:
        break
    
    data = data.decode() #decodifica il messaggio

    #serve a convertire una stringa di testo in formato JSON in un oggetto Python
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

    sock.sendto(str(reply).encode(), addr)