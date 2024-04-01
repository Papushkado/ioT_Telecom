import os
from dotenv import load_dotenv
from fastapi import FastAPI

from client import Client

load_dotenv()

TOKEN = os.getenv('TOKEN')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/client/ticket")
def client_data_ticket(client : Client):
    client_mail_list = None # import and read file to make a list 
    if client.mail_adress in client_mail_list:
        return {"message": "He has a ticket"} # faire une requête à HA pour que le portique s'ouvre
    else:
        return {"message": "He hasn't a ticket"}

@app.post("/client/drunk")
def client_data_drunk(client : Client):
    return {"Client friend" : client.contact_name, "Client friend number" : client.contact_phone_number} 
    # donner les infos de la personne à contacter au staffeur

@app.post("/client/bar")
def client_data_drunk(client : Client):
    client_consumption = None # consommation actuelle du client
    if client_consumption + 1 > client.alcohol_threshold:
        return {"Message" : "No more alcohol for you, sorry"} # faire une requête à HA pour que la lumière change
    else:
        client_consumption += 1
        # modifier la conso du client dans la BDD
        return {"Message" : "Have a nice drink"}
